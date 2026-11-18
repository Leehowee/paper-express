"""Maintainer checks for a release installed by copying its complete folder.

This is a packaging test, not a user installer. All output stays in a temporary
workspace. Users install with their agent's native extraction and file tools.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "paper-express"
MANIFEST = "PACKAGE-MANIFEST.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(folder):
    data = json.loads((folder / MANIFEST).read_text(encoding="utf-8"))
    assert data["name"] == NAME
    expected = set(data["files"])
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
    assert actual == expected | {MANIFEST}, "Unexpected or missing release files"
    for relative, record in data["files"].items():
        path = PurePosixPath(relative)
        assert not path.is_absolute() and ".." not in path.parts and "\\" not in relative
        file = folder.joinpath(*path.parts)
        assert not file.is_symlink() and file.resolve().is_relative_to(folder.resolve())
        assert file.stat().st_size == record["size"] and digest(file) == record["sha256"], relative
    return data


def validate_readmes(folder):
    profiles = []
    for name in ["README.md", "README_EN.md"]:
        file = folder / name
        text = file.read_text(encoding="utf-8")
        assert text.count("```") % 2 == 0
        anchors = re.findall(r'<a id="([^"]+)"', text)
        assert len(anchors) == len(set(anchors)) == 8
        local = []
        for target in re.findall(r"\]\(([^)]+)\)", text):
            path, _, anchor = target.partition("#")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", path):
                continue
            resolved = folder / unquote(path) if path else file
            assert resolved.exists(), (name, target)
            if anchor:
                assert f'id="{anchor}"' in resolved.read_text(encoding="utf-8"), target
            if path not in {"README.md", "README_EN.md"}:
                local.append(target)
        levels = [len(m.group(1)) for m in re.finditer(r"(?m)^(#{2,3}) ", text)]
        profiles.append((anchors, levels, sorted(local)))
    assert profiles[0] == profiles[1], "README structure or resources differ between languages"
    for name in ["README.md", "README_EN.md", "INSTALL.md", "RELEASE-NOTES.md"]:
        text = (folder / name).read_text(encoding="utf-8")
        assert "install.py" not in text and "--agent " not in text, name
    return {"matching_sections": True, "anchors_per_readme": 8, "shared_local_links": len(profiles[0][2]),
            "obsolete_installer_commands": 0}


def build():
    result = subprocess.run([sys.executable, str(ROOT / "packaging/build_release.py")],
                            capture_output=True, text=True, encoding="utf-8", check=True,
                            env=dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1"))
    return json.loads(result.stdout)


def main():
    metadata = build()
    archive = Path(metadata["archive"])
    assert build()["sha256"] == metadata["sha256"], "Build is not deterministic"
    # An unreviewed new file must not enter the installation bundle.
    with tempfile.NamedTemporaryFile(dir=ROOT, prefix=".unlisted-release-probe-", suffix=".txt") as probe:
        probe.write(b"Unlisted content must not be published.\n")
        probe.flush()
        assert build()["sha256"] == metadata["sha256"], "Unlisted source entered the release"
    parent = ROOT / ".build"
    parent.mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="paper-express-agent-install-", dir=parent))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name in z.namelist():
            path = PurePosixPath(name)
            assert path.parts[0] == NAME and ".." not in path.parts and "\\" not in name
        z.extractall(work / "解压 空格")
    bundle = work / "解压 空格" / NAME
    data = verify(bundle)
    assert not (bundle / "install.py").exists()
    entries = sorted(p.relative_to(bundle).as_posix() for p in bundle.rglob("SKILL.md"))
    assert entries == ["SKILL.md"]
    assert len(data["modules"]) == 5 and all((bundle / p).exists() for p in data["modules"].values())
    entry_name = re.search(r"(?m)^name: (.+)$", (bundle / "SKILL.md").read_text(encoding="utf-8")).group(1).strip()
    assert entry_name == bundle.name == data["name"]
    ui = (bundle / "agents/openai.yaml").read_text(encoding="utf-8")
    assert f"${NAME}" in ui and 'display_name: "Paper-Express"' in ui
    docs = validate_readmes(bundle)
    destinations = []
    for profile in [".agents/skills", ".claude/skills"]:
        dest = work / "示例 项目" / profile / NAME
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(bundle, dest)
        assert verify(dest) == data
        destinations.append(str(dest))
    # Verify that the artifact checker detects actual missing and changed content.
    altered = Path(destinations[-1]) / "paper-theory/GUIDE.md"
    original = altered.read_bytes()
    altered.write_bytes(original + b"\nchanged\n")
    try:
        verify(Path(destinations[-1]))
    except AssertionError:
        pass
    else:
        raise AssertionError("Changed file escaped integrity checking")
    altered.write_bytes(original)
    assert verify(Path(destinations[-1])) == data
    result = {"status": "passed", "archive": archive.name, "sha256": metadata["sha256"],
              "files": len(data["files"]), "local_markdown_links": metadata["local_markdown_links"],
              "discovery_entrypoints": 1, "modules": 5, "user_installer_in_package": False,
              "readmes": docs, "deterministic_build": True, "corrupted_file_detected": True,
              "unlisted_file_excluded": True,
              "copied_directories_verified": [Path(p).relative_to(work).as_posix() for p in destinations],
              "sandbox": work.relative_to(ROOT).as_posix(),
              "boundaries": ["Maintainer artifact checks; not an installer provided to users",
                             "Directory copies verified, not live host UI discovery",
                             "No global skill directories written",
                             "Scientific code and proofs require separate module validation"]}
    (parent / "agent-install-validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
