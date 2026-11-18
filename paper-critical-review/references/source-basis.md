# 来源依据与适用范围

编制与核查日期：2026-11-18。来源分为官方公开说明、本地模板、已有论文专题记录和本模块的设计扩展。以下简述仅用于说明依据；具体投稿要求在实际任务中按 venue、年份和稿件类型重新核查。

## 官方说明

| 来源 | 本次可核实的要点 | 使用范围与访问限制 |
| --- | --- | --- |
| [Nature：Editorial criteria and processes](https://www.nature.com/nature/for-authors/editorial-criteria-and-processes) | 原创研究、重要科学意义和跨学科读者相关性；技术成立与编辑取舍应区分 | 本地快照及本次官方搜索索引结果互相参照；直连遇身份跳转，未据此宣称当前全文抓取成功 |
| [Nature Communications：Guide to authors](https://www.nature.com/ncomms/submit/guide-to-authors) | 对特定领域专家有意义的重要推进，不要求与 Nature 相同的科学覆盖广度 | 依据本次官方页面索引内容；直连身份跳转。只代表该刊，不外推所有子刊 |
| [Nature Communications：Writing your report](https://www.nature.com/ncomms/for-reviewers/writing-your-report) | 评价贡献与证据，准确概括论文及其学科意义 | 检索到官方说明，直连受限；不复制其报告格式为所有期刊规定 |
| [IEEE Computer Society：Reviewer resources](https://www.computer.org/publications/reviewer-resources) | 评价方法、分析、结果、技术意义和准确性；引用要求需与工作相关 | 本次官方搜索索引可见，直连返回 403；这是学会共用资源，不是 TPAMI 专属评分表 |
| [TPAMI 官方期刊页面](https://www.computer.org/csdl/journal/tp) | 计算机视觉、模式分析与识别、机器智能等研究范围 | 官方搜索索引；用于界定范围，不用于推导固定实验或理论要求 |
| [ICLR 2026：Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide) | 审查具体问题、动机、证据和知识价值；价值不必等同于 SOTA；区分关键意见与额外建议 | 已打开并读取评审步骤。这里只用其研究判断原则，不照搬年份日程或政策到其他会议 |
| [ICML 2026：Reviewer Instructions](https://icml.cc/Conferences/2026/ReviewerInstructions) | 成立性与影响分开；创新可体现为组合、应用或假设放宽；判断需有依据 | 已打开并读取主要评审原则与表单说明。不是 CCF-A 全部会议的统一标准 |

没有采用网帖、聚合站或论文排名来替代以上规则。官方页面以后可能变化，本文件记录的是编制时所见内容；实际评分或投稿约束应重新核实。

## 本地来源

- `nature-skills-main.zip` 中 `nature-reviewer` 的入口、来源说明、评审维度、技术问题分类、核查清单及一致性审计内容，另参考 `nature-shared/core/consistency-sweep.md`。
- 前四部分已经建立的专题阅读记录，特别是 [图表来源索引](../../paper-figures-tables/references/source-index.md) 与 [理论来源索引](../../paper-theory/references/source-index.md)。本轮复用并核对相关记录，未重新逐字阅读全部 22 篇 PDF，也未新增论文实验复现。
- 通用技能组织与结构验证参考主机的 `skill-creator`。最终模块不依赖主机的私有绝对路径。

具体文件散列、读取范围与来源关系见 [source-manifest.json](source-manifest.json)。

## 本模块自行设计的内容

四种 venue 视角的工作化问题、best paper 加严检查、P0/P1/P2 修改顺序、跨模块协议、14 类意见段落、复审关闭状态和合成示例均为本包设计。它们借鉴来源原则，不代表官方量表，也不是对获奖或录用概率的建模。

没有从已发表论文身份推导其所有做法都正确。案例用于提炼审查问题，其结论仍需在新稿材料中独立核实。具体映射见 [语料经验](corpus-lessons.md)。
