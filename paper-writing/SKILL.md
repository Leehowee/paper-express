---
name: paper-writing
description: Draft complete research-paper prose from notes or polish existing text using fillable paragraph templates for Transactions journals and CCF-A conferences. Use for 论文初稿、成段写作、润色、重写、Trans/TPAMI 期刊写作、CCF-A 会议论文、摘要、引言、相关工作、方法、实验、结论、附录、正文压缩与中英文改写. Route mathematical claims and scientific figures/tables through explicit interfaces while preserving evidence and assumptions.
---

# 论文写作

围绕一个明确的研究问题组织论文，使问题、贡献、方法、证据和结论相互对应。将已完成的研究写清楚；对尚未建立的结论，保留其真实状态。支持整篇论文、单个章节和局部段落的独立写作。

用户要求写初稿时，从材料直接生成连续正文；要求润色时，直接交付修改稿。每节均提供可填充的完整段落、不同主线的写法及润色前后示例。默认交付实际文字，写作建议作为必要的补充。

## 选择路线

- **Trans 期刊**：默认在正文中完成主要论证、必要推导和系统实验分析。将增加的篇幅用于解释设计依据、成立条件、比较关系和适用边界。
- **CCF-A 会议**：在核实的正文限制内建立可独立判断的论证。正文保留核心设计、关键假设和决定性证据，附录承接详细证明、完整配置和扩展分析。

章节名称可以调整。`related-work` 可以与引言整合，局限可以独立成节；七类模板表示写作功能，不要求每篇论文使用七个同名标题。Trans 的 `appendix` 为条件入口，默认关闭。

## 加载顺序

按 [manifest.yaml](manifest.yaml) 选择材料，不一次性加载全部模板。

1. 读取 [基本原则](static/core/stance.md)、[写作流程](static/core/workflow.md) 和 [交付方式](static/core/output.md)。
2. 选择 [Trans 路线](static/routes/trans/overview.md) 或 [CCF-A 路线](static/routes/ccf-a/overview.md)，只加载当前章节。未确定投稿路线时，先完成共用主线和证据整理，章节篇幅与附录位置保留待定。
3. 起草、润色、重写、压缩或翻译时，读取 [直接起草与润色](static/core/drafting-and-polishing.md) 和下表中当前章节的“成段模板”，选一套适合材料的写法并完成填充与衔接。
4. 整篇写作、重组或问题定位需要时，读取 [论证路径](static/core/narrative-patterns.md)。
5. 涉及投稿格式、页数或正文压缩时，读取 [投稿约束与内容分配](static/core/venue-and-allocation.md)。涉及翻译或语言润色时，读取 [语言与段落](static/core/language.md)。
6. 出现数学结论或图表任务时，按下述接口传递上下文。已有合格结果可直接复用，不重复发起任务。

## 章节入口

| 功能 | Trans 期刊 | CCF-A 会议 |
| --- | --- | --- |
| Abstract | [章节指导](static/routes/trans/abstract.md) · [成段模板](assets/templates/trans/abstract.md) | [章节指导](static/routes/ccf-a/abstract.md) · [成段模板](assets/templates/ccf-a/abstract.md) |
| Introduction | [章节指导](static/routes/trans/introduction.md) · [成段模板](assets/templates/trans/introduction.md) | [章节指导](static/routes/ccf-a/introduction.md) · [成段模板](assets/templates/ccf-a/introduction.md) |
| Related Work | [章节指导](static/routes/trans/related-work.md) · [成段模板](assets/templates/trans/related-work.md) | [章节指导](static/routes/ccf-a/related-work.md) · [成段模板](assets/templates/ccf-a/related-work.md) |
| Methods | [章节指导](static/routes/trans/methods.md) · [成段模板](assets/templates/trans/methods.md) | [章节指导](static/routes/ccf-a/methods.md) · [成段模板](assets/templates/ccf-a/methods.md) |
| Experiments | [章节指导](static/routes/trans/experiments.md) · [成段模板](assets/templates/trans/experiments.md) | [章节指导](static/routes/ccf-a/experiments.md) · [成段模板](assets/templates/ccf-a/experiments.md) |
| Conclusion | [章节指导](static/routes/trans/conclusion.md) · [成段模板](assets/templates/trans/conclusion.md) | [章节指导](static/routes/ccf-a/conclusion.md) · [成段模板](assets/templates/ccf-a/conclusion.md) |
| Appendix | [条件入口](static/routes/trans/appendix.md) · [成段模板](assets/templates/trans/appendix.md) | [章节指导](static/routes/ccf-a/appendix.md) · [成段模板](assets/templates/ccf-a/appendix.md) |

## 直接使用

- 初稿：指定路线、章节和已有材料，例如“Trans Methods，按目标—求解套路直接写初稿”。
- 润色：给出现有文字，例如“CCF-A Introduction，按问题驱动结构润色，保留事实与引用”。
- 模板：需要自行填充时，直接返回选定套路及字段说明。

`{{FIELD}}` 从已有材料取值；缺失的必要信息写为 `[待补：具体内容]`。英文模板可以按同一逻辑输出中文。完整演示见 [材料→初稿→润色稿](references/worked-drafting-example.md)，其他请求示例见 [使用示例](references/usage-examples.md)。

## 模块接口

- [理论接口](interfaces/theory.md)：向 `paper-theory` 传递命题、算法与假设，接收数学分析、Lean 验证状态和可用于论文的结论。接口可独立使用。
- [图表接口](interfaces/figures-tables.md)：向 `paper-figures-tables` 传递主张、数据与版面要求，接收图表、图注、源文件和核查状态。接口可独立使用。
- [成稿审查接口](interfaces/review.md)：在用户要求审查或复审时，向 `paper-critical-review` 传递实际稿件与证据，接收定位明确的意见、修改动作和关闭标准。

[理论模块](../paper-theory/SKILL.md) 与 [图表模块](../paper-figures-tables/SKILL.md) 已实现，按接口调用并接收实际证明、生成与检查状态。图表可直接使用 [绘图、制表及可编辑模板](../paper-figures-tables/assets/template-catalog.md)。未找到被调用模块或缺少执行环境时，形成明确的任务说明并记录待完成项，继续处理不依赖该结果的文字；不得声称已运行 Lean、已生成图表或已完成核查。

## 来源参考

章节指导与成段模板均采用一般性写法。需要追溯提炼过程时，按需读取 [来源与阅读范围](references/source-index.md)、[期刊样本分析](references/xinwangliu-analysis.md)、[会议样本分析](references/xipeng-analysis.md) 或 [nature-skills 改编说明](references/nature-adaptation.md)。论文中的领域假设、参数和实验数值不作为新稿件默认值。
