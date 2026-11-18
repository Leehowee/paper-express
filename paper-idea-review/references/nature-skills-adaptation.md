# 基于 nature-skills 的改编说明

本技能在 2026-11-17 基于用户提供的 `nature-skills-main.zip` 重构。保留来源中的问题、证据和主张约束，围绕“科研 idea 与科学问题审查”编写新的独立入口与五条研究路径；不将原包整体改名，也不要求使用者安装其他 `nature-*` 技能。

规范性文件采用一般性的研究原则与执行要求。入口负责路径选择，共同标准负责证据与评价，路径文件负责论证逻辑、专门审查和优化建议。具体论文、页码与分析过程保留在来源和案例材料中，按需查阅；个别研究结果不直接写成普遍规律。

## 读取的主要来源与具体用途

以下路径均以 zip 内的 `nature-skills-main/` 为根。文件摘要记录在 [corpus-manifest.json](corpus-manifest.json) 中，便于区分不同下载快照；未将该压缩包声称为上游最新版本。

| 原包文件 | 继承的具体思想 | 本技能中的落点与修改 |
| --- | --- | --- |
| `skills/nature-writing/SKILL.md` | 写作先明确问题、主张与已有材料，按需读取支持文件 | 改成研究决策入口；不进入论文全文起草 |
| `skills/nature-writing/static/core/stance.md` | 以证据约束主张，保持概念清楚 | 区分来源事实、作者解释、分析推断和待检验假设 |
| `skills/nature-writing/static/core/workflow.md` | 在成文之前检查材料和论证链 | 从“草稿可写性”转向“问题能否回答、下一步是否值得做” |
| `skills/nature-writing/static/fragments/paper_type/hypothesis.md` | 假说需要可检验条件和不同解释 | 单列假说与反常现象路径；允许负结果作为贡献 |
| `skills/nature-shared/core/nature-introduction.md` | 从重要问题走向具体未知，避免将未采用自己的方案当作缺口 | 问题驱动模板、方法名称删除检查、重要性审查 |
| `skills/nature-shared/core/reader-workflow.md` | 以论文原文、方法、证据和局限共同理解研究 | 建立六篇案例，定位页码；不只摘录 abstract 的贡献句 |
| `skills/nature-paper-card/references/research-idea-gates.md` | 研究启发需有来源、假说、差异、验证和失效条件 | 分开创新性、重要性和可行性，给出最小判别检验；未采用固定 Paper Card 输出结构 |
| `skills/nature-paper-xray/SKILL.md` 与 `references/deep-reading-protocol.md` | 拆解方法依赖、实验对照及可迁移启发 | 案例中解释为什么某个对照有判别力，而不是只列结果 |
| `skills/nature-paper-xray/references/evidence-boundary.md` | 原文事实、解释与阅读者推断分层 | 记录本地版本和实际阅读范围；不伪造作者研发时间线 |

本轮也参考了原包 `skills/nature-proposal-writer/SKILL.md` 的问题导向，但没有移植其完整提案工作流、评分或代理组织方式。技能编排与结构校验使用了环境中的 `skill-creator` 指南；这不构成对 `nature-skills` 的额外运行依赖。

## 本次新增的部分

1. **五种可选择的研究路径**：问题、假说与反常现象、机制、理论、统一框架。不强制将不同起点压成一种叙事。
2. **论文中可定位的审查经验**：能力与采样效率、局部与整体评价、机制干预与伴随变化、框架实例化、理论与真实算法的对应。
3. **可改变决策的下一步**：给出支持、反证和不确定三类结果如何影响研究方向，而非只输出抽象建议。
4. **对后续模块的有限交接**：研究问题和证据可交给写作；准确命题可交给理论；比较目的可交给绘图。本模块自身可独立使用。
5. **理论路径的来源声明**：结合用户需求与一般数学审查原则设计；不冒称六篇论文足以代表纯理论研究的全部范式。

原包中的 Nature 写作取向被用于提炼问题与论证要求，没有写成期刊官方录用标准，也没有要求所有问题必须是宏观应用或实验性能提升。

## 许可与归属

原压缩包根目录附有 Apache License 2.0，已原样保留为 [LICENSE.nature-skills](../LICENSE.nature-skills)。本文件标明改编来源与修改范围；原包中的署名和权利归属仍以其原始文件为准。

六篇研究论文是独立的分析来源，各自保留其出版许可。本包未包含论文全文或原图，也不以 `nature-skills` 的软件许可重新许可论文。案例和路径中的自拟公式示例、问题重构与教学输入已作区分。
