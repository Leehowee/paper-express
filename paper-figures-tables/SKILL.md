---
name: paper-figures-tables
description: Design, code, revise and audit scientific figures and tables for research papers. Use for 科研绘图、做表、引言动机实验图、方法路线对比图、主流程图、主实验结果表、消融、机制分析、参数敏感性、稳健性、收敛、效率、案例和失败分析. Provide data-driven Python plots, LaTeX tables, editable PPTX/SVG templates, captions and provenance. Works independently or from Introduction, Methods, Experiments and Appendix.
---

# 科研图表

让图表回答一个明确的问题。先确定读者需要比较、辨认或理解什么，再选择图形、表格与版面。将观察、方法示意和解释分别表述，使图中的对象、数字和结论都能回到对应材料。

制作任务默认交付实际图表、图注与可修改源文件。已有数据时直接填充模板并生成成品；缺少数据时完成可确定的结构，保留准确的待补位置。润色任务直接修改图表及图注，并说明影响结论的改动。

## 加载顺序

按 [manifest.yaml](manifest.yaml) 渐进加载，不一次性读取所有路线。

1. 读取 [基本原则与流程](static/core/workflow.md) 和 [数据与统计口径](static/core/data-contract.md)。复用已有主张、数据和版面信息。
2. 按下表选择当前路线，再从 [模板目录](assets/template-catalog.md) 选择可运行配置、SVG 或 PPTX 页。
3. 制作时读取 [运行与替换数据](references/running.md)；调整风格时读取 [样式与导出](static/core/style-export.md)。图注直接使用 [可填充图注与正文衔接](assets/templates/captions.md)。
4. 交付前按 [核查与返回](static/core/quality-output.md) 检查数据、语义、最终尺寸和可编辑性。需要追溯规则时才读取论文分析。

## 选择路线

| 任务 | 路线 | 直接可用资产 |
| --- | --- | --- |
| 引入现象、指出问题 | [动机图](static/routes/motivation.md) | F01；D03；D06 |
| 对比已有路线、说明方法 | [方法图](static/routes/schematics.md) | D01、D02；PPTX 第 1–2 页 |
| 主实验与精确结果比较 | [结果表](static/routes/results-tables.md) | T01–T04；LaTeX/CSV；PPTX 第 5–9 页 |
| 组件、目标或求解器的作用 | [消融](static/routes/ablation.md) | F04；T02 |
| 内部机制、分布和表示 | [机制分析](static/routes/mechanism.md) | F05、F06、F12、F13 |
| 参数变化与默认值 | [敏感性](static/routes/sensitivity.md) | F07、F08；T03 |
| 噪声、缺失、规模等条件变化 | [稳健性](static/routes/robustness.md) | F09；T01 条件分块变体 |
| 训练过程与优化行为 | [收敛与过程](static/routes/convergence.md) | F10 |
| 质量与时间、通信、内存的权衡 | [效率](static/routes/efficiency.md) | F11；T04 |
| 重建、检索、对齐和失败案例 | [案例](static/routes/cases.md) | F14；D03、D04 |

F、T、D 是模板库编号，实际论文编号由稿件决定。所有附带数值示例均为明确标注的合成数据；D 类是可填充示意模板。不得将示例结果、示意矩阵或占位案例用于支持研究结论。

## 直接使用

- “用 F01，基于这份逐次运行结果生成引言动机图，突出预算变化下的反转。”
- “用 D01 和 D02，把我的方法描述改成同输入的路线对比和主流程图，输出可编辑 PPTX、SVG。”
- “用 T01，读取实验 CSV，生成均值±SD 的主结果三线表，并导出 LaTeX。”
- “审查这组消融与案例，保留不利结果，按双栏正文尺寸重新排版并润色图注。”

独立调用无需先完成全文或其他模块。写作方调用使用 [统一接口](interfaces/writing.md)，返回图表文件、稳定标签、数据映射、图注、可支持的结论与核查状态。Methods 中的理论保证沿用 [paper-theory](../paper-theory/SKILL.md) 的实际验证状态，不能由收敛曲线替代证明。

## 来源与实现

通用套路来自三组本地论文的图表专题阅读，代码与样式在 `figures4papers-main.zip` 基础上重新组织。具体观察、改编和限制见 [来源索引](references/source-index.md)、[Gao Huang 分析](references/gaohuang-analysis.md)、[Xi Peng 分析](references/xipeng-analysis.md)、[Xinwang Liu 分析](references/xinwangliu-analysis.md)、[上游改编](references/upstream-adaptation.md) 和 [验证记录](references/validation.md)。不把个别论文的版面、统计方式或参数当作通用规范。
