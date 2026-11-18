# Idea 审查与问题重写：可直接填写的模板

选择符合主要未知的一条路径，直接生成完成的审查与重构文字。`{{FIELD}}` 来自已有材料；缺少决定性信息时写 `[待核实：具体事项]`。各段可合并和删减，不要求每个 idea 都写成长报告。

## 共用判断段

> 当前建议是 {{推进/先验证/收窄/改路线/暂缓}}。这个构想希望回答 {{QUESTION}}，已有 {{EVIDENCE}} 支持 {{SUPPORTED_SCOPE}}，但 {{CRITICAL_UNKNOWN}} 仍决定其是否成立。从创新性看，{{VERIFIED_DELTA_OR_SEARCH_LIMIT}}；从重要性看，答案会改变 {{KNOWLEDGE_OR_DECISION}}；从可行性看，现有 {{RESOURCES}} 足以开展 {{FIRST_TEST}}，而 {{DEPENDENCY}} 尚需确认。优先建议 {{NEXT_ACTION}}，因为它能区分 {{ALTERNATIVES}}，并决定是否值得继续投入 {{LARGER_WORK}}。

## A. 问题驱动：从实际困难到可判断问题

> 在 {{OBJECT_AND_CONDITION}} 中，目标是实现 {{TASK_ENDPOINT}}。现有路线在 {{CONSTRAINT}} 下受到 {{BOTTLENECK}} 限制，其依据是 {{LOCATED_EVIDENCE}}。因此，值得研究的问题是：在保持 {{CONTROLLED_INFORMATION_OR_BUDGET}} 的条件下，{{PROPOSED_CHANGE}} 能否改善 {{MEASURABLE_ENDPOINT}}，代价与边界是什么？候选方案通过 {{ACTUAL_OPERATION}} 作用于该瓶颈；这一联系目前属于 {{OBSERVED_OR_HYPOTHESIZED}}。首个验证应比较 {{BASELINE_AND_VARIANT}}，固定 {{CONTROLS}}，同时测量 {{OUTCOME_AND_COST}}。若 {{FALSIFYING_RESULT}}，应重新定位瓶颈或缩小问题范围。

**问题成句**：在 {{CONDITION}} 和 {{RESOURCE_CONSTRAINT}} 下，如何改善 {{ENDPOINT}}，以及 {{CHANGE}} 是否能带来可归因、可重复的改善？

没有瓶颈证据时，将相关句改为“候选瓶颈是……，首先需要通过……确认”，不能把方案名称当作问题。

## B. 假说驱动：从现象到竞争解释

> 已有观察是在 {{CONDITIONS}} 下出现 {{OBSERVATION}}。该观察可能与 {{HYPOTHESIS_A}} 有关，也可能由 {{HYPOTHESIS_B_OR_DESIGN_FACTOR}} 解释。当前材料尚不能区分它们，因此核心问题是 {{DISCRIMINATING_QUESTION}}。两种解释对 {{CONTROLLED_CHANGE}} 的预测分别是 {{PREDICTION_A}} 和 {{PREDICTION_B}}。建议先确认观察的 {{REPEATABILITY_AND_MEASUREMENT}}，再进行 {{MINIMAL_DISCRIMINATING_TEST}}。若结果为 {{RESULT_A}}，支持 {{BOUNDED_A}}；若为 {{RESULT_B}}，削弱 {{CLAIM_TO_REVISE}}；若 {{INCONCLUSIVE_CASE}}，保留判断并说明缺少的证据。

**问题成句**：{{OBSERVATION}} 反映的是 {{EXPLANATION_A}}，还是 {{EXPLANATION_B}}，以及在 {{CONDITION}} 下哪些证据能够区分二者？

单次观察可以引出假说，不能直接写成稳定规律；有限测试未出现某行为，也不能推出其概率为零。

## C. 机制驱动：从关联到可干预关系

> 当前候选解释是 {{INPUT_OR_CONTEXT}} 通过 {{INTERMEDIATE_PROCESS}} 影响 {{OUTCOME}}。{{OBSERVATION}} 与该解释相容，但 {{CONFOUNDER_OR_ALTERNATIVE}} 也可能导致相同结果。拟研究的不是仅改变最终分数，而是检验 {{SPECIFIC_MECHANISM_LINK}}。建议在固定 {{CONTROLS}} 时干预 {{TARGET_FACTOR}}，同时观察 {{INTERMEDIATE_MEASURE}} 与 {{TASK_ENDPOINT}}。若二者按 {{PREDICTED_PATTERN}} 改变且主要替代解释得到排除，可以支持 {{CONDITIONAL_MECHANISM_CLAIM}}；若仅终点改善，则将结论保留为效果证据并重新检查机制。

**问题成句**：在 {{CONDITION}} 下，改变 {{FACTOR}} 是否通过 {{PROCESS}} 影响 {{OUTCOME}}，其必要条件和主要替代解释是什么？

仅有注意力图、权重、投影或相关曲线时，不把模板中的“通过”写成已确立因果关系。

## D. 理论驱动：从笼统保证到精确命题

> 对 {{MATHEMATICAL_OBJECT}}，已有结论在 {{KNOWN_ASSUMPTIONS}} 下建立 {{KNOWN_PROPERTY}}；当前希望明确 {{UNRESOLVED_RELATION}}。候选命题是：对所有／存在 {{QUANTIFIED_OBJECTS}}，在 {{ASSUMPTIONS}} 下有 {{PRECISE_CONCLUSION}}。首先检查 {{DEGENERATE_OR_LOW_DIMENSION_CASE}}，再研究 {{KEY_LEMMA}} 是否成立。若出现满足前提的反例，则将命题修订为 {{WEAKER_OR_CONDITIONAL_STATEMENT}}；若该条件已知且无新增结果，则将其定位为方法依据，而不单独宣称理论创新。结论的研究价值在于 {{DESIGN_OR_KNOWLEDGE_IMPLICATION}}。

**问题成句**：{{PROPERTY}} 对 {{OBJECT}} 在什么条件下成立；哪些条件可以放宽，哪些反例或界限说明它不能继续推广？

所写“已有结果”需要文献核实。仅为当前作者未知时，不将其称为领域未解问题。优化后的命题及证明任务可交给理论模块。

## E. 统一框架驱动：从共同形式到实质联系

> {{PROBLEMS_OR_METHODS}} 共享 {{VERIFIED_COMMON_STRUCTURE}}，但在 {{IMPORTANT_DIFFERENCES}} 上不同。拟建立 {{UNIFYING_FORMULATION}}，保持 {{INVARIANTS}}，并通过 {{ADAPTERS_OR_ASSUMPTIONS}} 处理差异。框架的可检验承诺是 {{NEW_RELATION_OR_CAPABILITY}}。先在 {{INITIAL_INSTANCE}} 上给出明确实现，再用 {{DISTINCT_INSTANCE_OR_BOUNDARY}} 检查是否需要改变核心原则。若只能通过重新设计核心算法完成新实例，应收缩统一性的含义；若共有结构产生了 {{DERIVED_INSIGHT}}，则据此说明其知识增量。

**问题成句**：哪些共同结构能够统一 {{OBJECTS}}，由此能推出什么新关系或设计原则，其不可覆盖的情况是什么？

框架类比与严格包含关系分别表述；“恢复为特例”需要实际映射或证明，不能由术语相似推出。

## 最小验证表

| 检验对象 | 固定条件 | 改变因素或待证步骤 | 观测量或数学结论 | 支持结果 | 削弱／否定结果 | 无法判断的情况 | 资源与依赖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{CLAIM_ID_AND_TEXT}} | {{CONTROLS}} | {{CHANGE}} | {{TARGET}} | {{SUPPORT}} | {{FALSIFY_OR_NARROW}} | {{INCONCLUSIVE}} | {{AVAILABLE_AND_MISSING}} |

理论任务可将实验列换成假设、关键引理与反例检查。验证是计划时明确写“拟开展”，不得预填预计成绩、证明通过或显著性。

## 交接给写作的主线段

> 本研究关注 {{QUESTION}}。已核实的缺口是 {{GAP_WITH_SOURCE}}，候选解决思路是 {{DESIGN}}。目前证据支持 {{ESTABLISHED_RESULT}}，尚待检验 {{HYPOTHESIS_OR_LIMIT}}。初稿可以写清 {{READY_CONTENT}}；{{UNAVAILABLE_RESULT}} 保留待补。若关键检验得到 {{POSSIBLE_RESULT}}，再相应调整贡献与结论范围。

候选设计、现有事实和未来工作使用不同语气。真正交付时选取所需段落并填成连贯结论，不把五套空白模板全部返回给用户。
