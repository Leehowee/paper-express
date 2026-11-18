"""Build a relocatable, single-entry Agent Skills ZIP from the maintained sources.

Python 3.10+, standard library only. Build work stays in a fresh temporary folder.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "paper-express"
VERSION = "3.0.0"
MODULES = ["paper-idea-review", "paper-writing", "paper-theory",
           "paper-figures-tables", "paper-critical-review"]
INVENTORY = ROOT / "packaging/release-files.txt"
MANIFEST = "PACKAGE-MANIFEST.json"
LINK = re.compile(r"\[([^\]\n]*)\]\(([^)\n]+)\)")
TEXT = {".md", ".yaml", ".json", ".log"}


def mapped(relative: str) -> str:
    for module in MODULES:
        if relative == f"{module}/SKILL.md":
            return f"{module}/GUIDE.md"
    return relative


def transform(text: str, relative: str, external: list) -> str:
    source = ROOT / relative

    def link(match):
        label, target = match.groups()
        pathpart, sep, fragment = target.strip("<>").partition("#")
        if not pathpart or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", pathpart):
            return match.group(0)
        resolved = (source.parent / unquote(pathpart)).resolve()
        if resolved.is_relative_to(ROOT):
            new = mapped(resolved.relative_to(ROOT).as_posix())
            new_base = (ROOT / mapped(relative)).parent
            path = Path(os.path.relpath(ROOT / new, new_base)).as_posix()
            return f"[{label}]({path}{sep}{fragment})"
        try:
            provenance = resolved.relative_to(ROOT.parent).as_posix()
        except ValueError:
            provenance = resolved.name
        external.append({"document": mapped(relative), "source": provenance, "label": label})
        return f"{label}（来源文件：`{provenance}`；未随包分发）"

    if relative.endswith(".md"):
        text = LINK.sub(link, text)
    for module in MODULES:
        text = text.replace(f"{module}/SKILL.md", f"{module}/GUIDE.md")
        text = text.replace(f"${module}", f"{NAME} 的 {module} 模块")
    if relative == "architecture.md":
        text = text.replace("    SKILL.md", "    GUIDE.md")
        text = text.replace("paper-skills/", f"{NAME}/")
        text = "<!-- 发布版：五个子模块入口为 GUIDE.md；根 SKILL.md 是唯一注册入口。 -->\n\n" + text
    return text


def portable_skill() -> str:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
    for module in MODULES:
        text = text.replace(f"{module}/SKILL.md", f"{module}/GUIDE.md")
    text = text.replace("读取目标模块的 `SKILL.md`", "读取目标模块的 `GUIDE.md`")
    text = text.replace("本目录提供本地技能源文件，是否已被宿主安装或自动发现应以实际环境为准。", "")
    text = text.replace("\n面向不同 agent 的发布包、安装方式与模块调用例子见 [INSTALL.md](INSTALL.md)。维护目录保留各模块入口；安装时使用 `dist/` 中生成的标准技能 ZIP。\n", "")
    text += """
## 跨 agent 使用

本安装包只注册 `paper-express`，展示名为 Paper-Express。用户指定 idea / writing / theory / figures / review，或对应中文任务时，直接进入上表对应模块；`paper-idea-review` 等完整模块名也可用于路由。不要求注册其它技能，五部分均可独立完成任务。

文件链接相对于所在文档解析；命令中的模块内路径相对于该模块目录解析。调用脚本时使用实际安装路径，不假设当前目录就是技能目录。模板先复制到用户的论文工作目录，生成产物和验证报告也写入该工作目录。

读取与写作使用宿主已有工具；检索、Python、Lean 或 PPTX 构建工具只在任务确实需要时使用。工具不可用时保留相应未执行状态，并继续完成有证据支持的工作。已有模板与合成示例不构成用户论文的实验结果或形式化证明。

安装方法、运行依赖与模块调用例子见 [INSTALL.md](INSTALL.md)。包内历史验证记录只描述模板编制时的检查，不代表已在当前机器验证。没有随包分发的原文以来源记录标明；需要重核原文时，通过合法可用来源获取，不把缺失原文当成已读材料。
"""
    return text


def redact_history(value):
    if isinstance(value, str):
        normalized = value.replace("\\", "/")
        prefix = ROOT.parent.as_posix()
        if prefix in normalized:
            return normalized.replace(prefix, "build-workspace:")
        return value
    if isinstance(value, list):
        return [redact_history(v) for v in value]
    if isinstance(value, dict):
        return {redact_history(k): redact_history(v) for k, v in value.items()}
    return value


def collect() -> tuple[dict[str, bytes], list]:
    payload, external = {}, []
    entries = [line.strip() for line in INVENTORY.read_text(encoding="utf-8").splitlines()
               if line.strip() and not line.startswith("#")]
    if len({name.casefold() for name in entries}) != len(entries):
        raise ValueError("Duplicate or case-colliding release inventory paths")
    for name in sorted(entries):
        rel = PurePosixPath(name)
        if rel.is_absolute() or ".." in rel.parts or "\\" in name or ":" in name:
            raise ValueError(f"Invalid release path: {name}")
        path = ROOT.joinpath(*rel.parts)
        if (not path.is_file() or not path.resolve().is_relative_to(ROOT)
                or any(parent.is_symlink() for parent in [path, *path.parents] if parent != ROOT)):
            raise ValueError(f"Missing or nonportable release source: {name}")
        if name in {MANIFEST, "RELEASE-NOTES.md"}:
            raise ValueError(f"Generated file cannot be a release source: {name}")
        data = path.read_bytes()
        if path.suffix in TEXT:
            text = data.decode("utf-8-sig")
            text = transform(text, name, external)
            if name.endswith("verification.json"):
                history = json.loads(text)
                history = redact_history(history)
                history["distribution_note"] = ("Historical build record; build-workspace: paths "
                                                "are provenance placeholders, not runtime locations.")
                text = json.dumps(history, ensure_ascii=False, indent=2) + "\n"
            data = text.encode("utf-8")
        payload[mapped(name)] = data
    payload["SKILL.md"] = portable_skill().encode("utf-8")
    # Preserve source provenance after external local links have been made portable.
    provenance = ROOT / "references/distribution-sources.json"
    if provenance.exists():
        historical = json.loads(provenance.read_text(encoding="utf-8"))["sources"]
        external = historical + [item for item in external if item not in historical]
    external = [{**item, "document": mapped(item["document"])} for item in external]
    # Keep module-local frontmatter for documentation, without nested discovery files.
    payload["references/distribution-sources.json"] = (json.dumps({
        "note": "Optional source papers/archives are not distributed. Source labels and page references remain in the reading notes.",
        "sources": external,
    }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    payload["RELEASE-NOTES.md"] = f"""# Paper-Express {VERSION}

一个标准 `SKILL.md` 入口，五个按需读取的 `GUIDE.md` 模块，全部模板、代码、合成数据、PPTX/SVG 和第三方许可随包提供。安装与调用见 [INSTALL.md](INSTALL.md)。

项目总览与示例见 [中文 README](README.md) 或 [English README](README_EN.md)。

安装时将仓库链接、发布 ZIP 或解压目录交给 Codex、Claude Code 等智能体，由其使用系统文件工具取得并复制完整技能目录。用户安装无需 Python，包内不提供专用安装脚本。

发布名称为 **Paper-Express**，注册标识与安装目录名为 `paper-express`。历史维护源目录名为 `paper-skills`；历史验证记录保留当时名称，不作为当前调用标识。

发布版由维护源生成：改写子模块入口和交叉引用；将包外原始论文/上游归档的链接改为来源文字；对历史 Lean 构建记录中的本机目录作显式脱敏。原始文件名及引用位置保存在各来源说明中，转换清单见 [distribution-sources.json](references/distribution-sources.json)。不随包分发原文 PDF、上游归档、运行时库或缓存。

代码与模板的科学边界不变。原生 PPTX 构建库是可选的特定环境依赖；现成可编辑模板不依赖该库。历史验证记录与本机安装校验分别记录，不把模板验证当作真实论文验证。

`PACKAGE-MANIFEST.json` 保存所有文件的 SHA-256 和字节数（清单自身除外）；ZIP 旁边提供整包 SHA-256。校验用于内容完整性，不提供身份签名。此包未自动安装到任何全局 agent 目录。
""".encode("utf-8")
    return payload, external


def validate(payload: dict[str, bytes]) -> dict:
    links = 0
    names = set(payload)
    if [n for n in names if n.endswith("SKILL.md")] != ["SKILL.md"]:
        raise ValueError("Expected exactly one root SKILL.md")
    for module in MODULES:
        if f"{module}/GUIDE.md" not in names:
            raise ValueError(f"Missing module: {module}")
    for name, data in payload.items():
        if name.endswith(".md"):
            for match in LINK.finditer(data.decode("utf-8")):
                target = match.group(2).strip("<>").split("#")[0]
                if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                normalized = os.path.normpath(str(Path(name).parent / unquote(target))).replace("\\", "/")
                if normalized not in names and not any(p.startswith(normalized.rstrip("/") + "/") for p in names):
                    raise ValueError(f"Missing or external release link: {name} -> {target}")
                links += 1
    return {"discoverable_skills": 1, "modules": 5, "local_markdown_links": links}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    payload, external = collect()
    checks = validate(payload)
    manifest = {"schema_version": 1, "name": NAME, "display_name": "Paper-Express", "version": VERSION,
                "format": "Agent Skills", "entrypoint": "SKILL.md",
                "modules": {m: f"{m}/GUIDE.md" for m in MODULES},
                "package_checks": checks,
                "files": {n: {"size": len(b), "sha256": hashlib.sha256(b).hexdigest()}
                          for n, b in sorted(payload.items())}}
    payload[MANIFEST] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    args.out.mkdir(parents=True, exist_ok=True)
    archive = args.out / f"{NAME}-{VERSION}.zip"
    # A fresh file in the output directory is replaced atomically after a complete ZIP is written.
    with tempfile.NamedTemporaryFile(dir=args.out, prefix=".release-", suffix=".zip", delete=False) as temp:
        temporary = Path(temp.name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for name, data in sorted(payload.items()):
                info = zipfile.ZipInfo(NAME + "/" + name, date_time=(2026, 11, 18, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, data)
        temporary.replace(archive)
    finally:
        temporary.unlink(missing_ok=True)
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{checksum}  {archive.name}\n", encoding="ascii")
    print(json.dumps({"archive": str(archive), "bytes": archive.stat().st_size,
                      "sha256": checksum, "files": len(payload),
                      "source_links_converted": len(external), **checks}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
