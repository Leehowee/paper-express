# Paper-Express：让智能体安装

[中文总览](README.md) · [English overview](README_EN.md)

把仓库链接、发布包路径或已解压目录交给 Codex、Claude Code 等智能体，让它读取本说明并完成安装。**技能安装只需获取文件、解压和复制目录，无需 Python 环境或专用安装脚本。**

官方仓库：[Leehowee/paper-express](https://github.com/Leehowee/paper-express)。发布包：[paper-express-3.0.0.zip](https://github.com/Leehowee/paper-express/raw/refs/heads/master/dist/paper-express-3.0.0.zip)；[SHA-256 校验文件](https://github.com/Leehowee/paper-express/blob/master/dist/paper-express-3.0.0.zip.sha256)。

发布版只有一个注册入口 `paper-express`，内部包含五个可独立使用的模块。安装时保留整个文件夹。

## 选择安装来源

| 你提供的来源 | 智能体如何处理 |
| --- | --- |
| 本项目仓库链接或本地维护源 | 先读 README，再取得 `dist/paper-express-3.0.0.zip` 中的发布目录 |
| `paper-express-3.0.0.zip` | 用系统解压工具解压到临时目录，核对其中的 `paper-express` 文件夹 |
| 已解压的 `paper-express` 目录 | 读取 `SKILL.md` 和 `PACKAGE-MANIFEST.json`，核对后复制 |

维护源根目录包含多个模块入口；发布目录已将子模块入口整理为 `GUIDE.md`，适合直接安装。仓库尚未提供发布包时，说明缺少的资源并请求可用来源；已有发布包可直接使用，无需执行维护源码的构建流程。

## Codex 安装提示词

```text
请将 Paper-Express 安装为我的 Codex 用户级技能。
来源：https://github.com/Leehowee/paper-express

先读取 README 和 INSTALL.md，使用发布目录中的完整技能内容。
检查当前 Codex 实际读取的用户级 skills 目录，将文件夹命名为 paper-express。
使用系统解压和文件工具完成安装，保留模块、模板、脚本、资产和许可文件。
已有副本先比较；内容相同则保留，有本地修改则保留修改并报告差异。
按 PACKAGE-MANIFEST.json 核对文件和 SHA-256，确认唯一的 SKILL.md 入口及五个模块完整。
报告最终绝对路径、检查结果，以及是否已在当前宿主中发现该技能。
```

常见用户目录为 `~/.agents/skills/`。已有环境可能使用 `$CODEX_HOME/skills` 或 `~/.codex/skills/`，应先检查当前环境并沿用实际生效的位置。项目安装使用项目内的 `.agents/skills/paper-express/`。路径和发现规则以 [Codex 官方说明](https://learn.chatgpt.com/docs/build-skills) 与实际配置为准。

## Claude Code 安装提示词

```text
请将 Paper-Express 安装为我的 Claude Code 用户级技能。
来源：https://github.com/Leehowee/paper-express

先读取 README 和 INSTALL.md，使用发布目录中的完整技能内容。
使用系统解压和文件工具，将完整目录安装到 ~/.claude/skills/paper-express/。
保留模块、模板、脚本、资产和许可文件。
已有副本先比较；内容相同则保留，有本地修改则保留修改并报告差异。
按 PACKAGE-MANIFEST.json 核对文件和 SHA-256，确认唯一的 SKILL.md 入口及五个模块完整。
报告安装路径、检查结果，并说明如何使用 /paper-express。
```

只在一个项目使用时，在提示词中指定项目路径和项目级范围，安装到该项目的 `.claude/skills/paper-express/`。个人与项目技能规则见 [Claude Code 官方说明](https://code.claude.com/docs/en/skills)。

## 其他智能体与手动复制

将同样的安装请求交给对应智能体，并让它核实当前支持的技能目录。也可以手动将完整的 `paper-express` 文件夹放进下表目录：

| 智能体 | 项目内技能目录 | 用户级技能目录 |
| --- | --- | --- |
| Codex | `.agents/skills` | `~/.agents/skills`，或当前环境已配置的位置 |
| Claude Code | `.claude/skills` | `~/.claude/skills` |
| Cursor | `.cursor/skills` | `~/.cursor/skills` |
| GitHub Copilot | `.github/skills` | `~/.copilot/skills` |
| Gemini CLI | `.gemini/skills` | `~/.gemini/skills` |
| OpenCode | `.opencode/skills` | `~/.config/opencode/skills` |

`~` 是当前用户的主目录。上表列出容纳技能的父目录，最终入口例如 `~/.claude/skills/paper-express/SKILL.md`。文件夹名与声明名均为 `paper-express`。

其他目录依据 [Cursor](https://cursor.com/docs/skills)、[GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)、[Gemini CLI](https://geminicli.com/docs/cli/skills/) 和 [OpenCode](https://opencode.ai/docs/skills/) 官方说明整理；核对日期为 2026-11-18。格式依据 [Agent Skills 规范](https://agentskills.io/specification)。宿主版本、管理策略和云端运行方式可能影响加载位置，最终以实际环境为准。

## 安装完成后核对什么

让执行安装的智能体完成以下检查并报告结果：

1. 最终目录名为 `paper-express`，根 `SKILL.md` 声明 `name: paper-express`。
2. 目录内只有一个 `SKILL.md`，五个模块的 `GUIDE.md` 及其引用资源存在。
3. `PACKAGE-MANIFEST.json` 中的文件、字节数与 SHA-256 对应安装文件。可使用 PowerShell `Get-FileHash`、`sha256sum` 或宿主已有文件工具。
4. 更新技能列表或打开新会话，检查宿主是否发现 `paper-express`；只验证了文件时，明确报告“文件安装完成，宿主加载待核实”。

清单用于检查内容完整性，不是发布者身份签名。出现已有修改或清单不匹配时，先保留内容并报告具体差异。文件校验通过不代表科研脚本依赖已经配置完成，也不代表云端账户已同步技能。

## 开始使用

在 Codex 中使用 `$paper-express`，在 Claude Code 中使用 `/paper-express`，或直接用自然语言指定模块：

| 模块 | 示例请求 |
| --- | --- |
| `idea` | 使用 paper-express 的 idea 模块，审查这个研究问题，比较问题驱动与理论驱动的完善路线。 |
| `writing` | 使用 paper-express 的 writing 模块，按 Trans 路线根据这些真实结果起草 Introduction。 |
| `theory` | 使用 paper-express 的 theory 模块，为这个目标建立假设、命题和证明，并如实报告 Lean 状态。 |
| `figures` | 使用 paper-express 的 figures 模块，根据原始 CSV 制作主结果表和消融图。 |
| `review` | 使用 paper-express 的 review 模块，从 TPAMI 和 CCF-A best paper 视角审查此稿。 |

`paper-theory` 等完整名称是内部模块名，五部分通过 `paper-express` 路由，不另行注册快捷命令。

## 科研功能的运行环境

安装后，写作、问题分析和审查指引可由智能体直接读取。需要执行科研代码时，再按模块要求准备环境：

| 能力 | 运行要求 |
| --- | --- |
| 文献或投稿规则核实 | 宿主已有检索工具；无法核实时保留待核实状态 |
| Python 绘图与制表 | Python 3.12+，依赖见 [requirements.txt](paper-figures-tables/requirements.txt)，详细步骤见 [运行说明](paper-figures-tables/references/running.md) |
| 编辑现成 PPTX / SVG | 支持相应格式的编辑器或宿主工具 |
| 重建原生 PPTX | Node.js 与可用的 `@oai/artifact-tool`；该库不随包分发，没有时直接编辑现成模板 |
| Lean 形式化核验 | Lean / Lake 及锁定的 Mathlib，详见 [Lean 工作方式](paper-theory/static/lean/workflow.md) |

模板先复制到论文工作目录，结果和运行日志也写入该目录。随包数据为合成示例；用于真实研究时，应替换数据、比较协议和说明。

## 更新与移除

更新时，把新发布包交给智能体，说明“比较当前安装与新版本，保留本地修改；如需替换，先把旧副本备份到技能扫描目录之外，完成后核对文件并报告结果”。相同内容无需重复复制。

移除时，指明实际安装路径，只移除该路径中的 `paper-express` 文件夹，再刷新宿主技能列表。不要将整个 skills 目录当作移除对象。

## 维护源与发布包

`paper-skills` 是维护输出目录名，`paper-express` 是发布与安装目录名。维护者可运行 `python packaging/build_release.py` 生成发布 ZIP，用 `python packaging/test_release.py` 检查结构和完整性；这些维护工具不随发布包分发。安装用户直接将发布包交给智能体即可。

发布包保留模块来源说明与第三方许可，其中绘图参考来源包含 CC BY-NC 4.0 材料。项目原创内容适用 [MIT 许可证](LICENSE)，第三方条款仍分别保留；详见 [NOTICE.md](NOTICE.md)。
