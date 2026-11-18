---
name: paper-critical-review
description: Critically review a developed research manuscript and produce evidence-located reviewer comments, revision priorities, and closure checks. Use for 成型论文审查、模拟审稿、投稿前自审、论文批判、Nature/Nature 子刊/TPAMI/CCF-A 审稿视角、best paper 水平检查、修改后复审. Supports full papers, sections, theory and Lean claims, experiments, and figures. Use for assessment rather than routine polishing or author rebuttal drafting.
---

# 成型论文批判审查

判断论文提出了什么新知识、现有证据能支持到哪里，以及哪些修改会改变对论文的评价。先准确重建作者的研究问题与贡献，再审查推理、比较和证据。严格程度体现在判断有依据、问题能定位、修改可核验，而不体现在否定措辞或意见数量。

默认交付实际审稿报告与修改方案。可独立调用，也可接收写作模块提供的成稿。未提供完整论文时，按已见材料完成局部审查，明确剩余范围；不把片段中未出现的内容认定为整篇论文缺失。

## 选择审查视角

| 视角 | 主要判断 | 加载材料 |
| --- | --- | --- |
| Nature | 发现的重要性、科学认识的推进、跨领域读者为何关心 | [Nature](static/lenses/nature.md) |
| Nature 子刊 | 对具体学科或交叉领域的重要推进、证据深度与目标读者 | [Nature 系列期刊](static/lenses/nature-family.md) |
| TPAMI | 问题与方法贡献、技术严谨性、系统证据及可复现性 | [TPAMI](static/lenses/tpami.md) |
| CCF-A 会议 | 明确的新知识、关键证据、正文与附录的论证分工 | [CCF-A](static/lenses/ccf-a.md) |
| Best paper 加严检查 | 洞见是否改变理解或实践、决定性证据是否充分、价值能否迁移 | [高水平贡献检查](static/lenses/best-paper.md) |

先评估共同的科学有效性，再应用目标视角。Best paper 是可叠加的研究质量检查，不是独立 venue、统一评奖标准或获奖预测。没有指定目标时，先完成共用审查，再简要比较上述视角下最影响评价的差距，不生成四份重复报告。

## 加载顺序

按 [manifest.yaml](manifest.yaml) 渐进加载。

1. 读取 [审查流程](static/core/workflow.md)、[证据与严重程度](static/core/evidence-and-severity.md)、[主张审计](static/core/claim-audit.md)。
2. 读取选定视角。需要真实投稿规则、评分表、页数或截止时间时，核实具体 venue、年份和稿件类型；本包不硬编码通用页数或录用阈值。
3. 出现相应主张时，加载 [理论与 Lean](static/audits/theory-and-lean.md)、[实验与统计](static/audits/experiments-and-statistics.md) 或 [图表与内部一致性](static/audits/figures-and-consistency.md)。未适用的检查不转化为补做要求。
4. 使用 [审稿报告](assets/templates/reviewer-report.md) 和 [意见段落套路](assets/templates/concern-paragraphs.md)，写成具体意见；用 [修改计划](assets/templates/revision-plan.md) 安排最小有效修改。
5. 复审时加载 [修改后核验](static/audits/revision-recheck.md) 与 [复审报告](assets/templates/recheck-report.md)，沿用原问题编号。
6. 需要落实修改时，按 [模块接口](interfaces/modules.md) 返回第一至第四部分。审查本身不自动运行大型实验、修改论文或提交外部评审。

## 输出要求

每份报告给出审查范围、对论文的准确概括、有证据的优点、主要问题、次要问题、尚不能判断的事项和修改优先级。没有依据的问题不写，某一类没有问题时直接说明。

每条重要意见至少包含：

- 稳定编号、受影响主张、原稿位置及证据位置。
- 已观察到的事实、据此作出的判断，以及仍不确定的部分。
- `major` 或 `minor`、是否阻断核心主张，以及严重程度的理由。
- 最小修改动作、合理替代方案，以及什么新证据可以关闭问题。

可选增强单独列出，不混入必须完成的事项。必须区分“没有证明”“证明存在缺口”“命题已被反例否定”；也区分“没有检测到差异”和“已证明等效”。技术成立、贡献大小、目标适配度分别判断，不用一个总分掩盖差别。

模板字段 `{{FIELD}}` 由实际材料填充。无法核实的必要字段写 `[待核实：具体内容]`；没有页码时使用已核实的章节、标题或短摘录定位，不编造页行号。中文报告可直接使用模板，英文报告按同一证据结构撰写。

## 多视角与独立审稿

默认是一份报告中的多视角分析，不声称多个独立审稿人达成共识。用户明确要求独立审稿小组、且实际支持隔离上下文时，使用 [独立审稿任务单](assets/templates/independent-brief.md)：先固定相同材料，各自完成并冻结报告，再比较异同。不能隔离时如实返回多视角审查。不得虚构审稿人身份或为了“多样性”分配不同结论。

## 直接使用

- “用 TPAMI 视角审查这篇成稿，重点查理论保证与算法实现是否一致，给出可执行修改方案。”
- “用 CCF-A 会议视角审查，并加上 best paper 检查；区分当前结论必须修复的问题与可选提升。”
- “仅检查表 2、图 4 和实验结论的一致性，其他部分不作判断。”
- “根据上一轮问题清单复审 v2，指出已解决、收缩后解决和仍未解决的问题。”

可复制 [请求格式](assets/templates/review-request.yaml)、[主张证据表](assets/templates/claim-evidence-ledger.csv)、[问题台账](assets/templates/issue-ledger.csv)；完整演示见 [合成稿件→审查→复审](references/worked-example.md)。这些表是可选的记录载体，小任务可直接用文字完成。

## 来源与限制

组织方式改编自本地 nature-reviewer，结合前四部分已建立的论文阅读记录和官方评审说明，重构为通用审查模板。查看 [来源依据](references/source-basis.md)、[改编说明](references/nature-adaptation.md)、[语料经验](references/corpus-lessons.md) 与 [验证记录](references/validation.md)。本模块提供作者侧模拟审查，不代替编辑决定，不保证接收或获奖。
