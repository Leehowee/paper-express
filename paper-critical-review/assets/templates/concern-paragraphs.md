# 可直接填写的审稿意见套路

先核实触发条件，再选一个与实际缺口匹配的段落。每段外接 issue_id、主张编号、位置和分级；大括号内容必须替换为稿件事实。严重程度由影响决定，不由套路名称预设。每条可填一项有效解决路径，不强迫作者同时完成补实验、补理论与改写。

## 1. 创新差异未建立

适用：已核实近邻工作，但论文对与之相关的差异解释不足。没有完成文献核实时不使用“已有工作已经做过”。

> 本文在 {{LOCATION}} 将 {{CLAIM}} 作为贡献。与已核实的 {{PRIOR_WORK_AND_LOCATION}} 相比，两者在 {{SHARED_SETTING}} 下均采用 {{SHARED_OPERATION}}，当前文字尚未解释 {{POSSIBLE_DIFFERENCE}} 怎样带来新的能力或结论。建议围绕 {{RELEVANT_DIMENSION}} 明确比较，并用 {{MINIMAL_ANALYSIS_OR_CONTROL}} 检验差异是否具有实质作用。如果创新主要在 {{NARROWER_CONTRIBUTION}}，应据此重写贡献，而不维持 {{OVERBROAD_NOVELTY}} 的表述。

## 2. 重要性尚未连接到研究终点

> {{LOCATION}} 将 {{PROBLEM}} 描述为重要瓶颈，但现有 {{MOTIVATION_EVIDENCE}} 只说明它在 {{CONDITION}} 下出现，尚未说明它如何限制 {{TARGET_OUTCOME}}。建议补充 {{LOWEST_COST_RELEVANT_EVIDENCE}}，或以现有结果明确该问题影响的条件与对象。关闭本问题需要建立 {{PROBLEM_TO_OUTCOME_LINK}}，而非仅增加应用场景或强调技术复杂度。

## 3. 主比较受到协议混杂

> {{TABLE_OR_EXPERIMENT}} 中，本文方法与 {{BASELINE}} 同时在 {{CONFOUNDING_FACTOR}} 上存在差异。因此，{{OBSERVED_GAIN}} 目前不能全部归因于 {{PROPOSED_COMPONENT}}。建议在固定 {{MATCHED_CONDITIONS}} 后进行 {{MINIMAL_MATCHED_COMPARISON}}，或明确将结果解释为包含 {{EXTRA_RESOURCE}} 的完整系统比较。只有在 {{CLOSURE_EVIDENCE}} 得到支持后，才能保留当前归因。

## 4. 消融不能分离贡献来源

> {{ABLATION_LOCATION}} 同时改变了 {{FACTOR_A}} 和 {{FACTOR_B}}，因而 {{RESULT}} 不能区分两者的贡献。建议在可行条件下补充 {{CROSS_CONTROL}}，并保持 {{CONTROLS}} 一致；若某个组合不可实现，应解释依赖关系并限制归因。该问题的关键是区分 {{COMPETING_EXPLANATIONS}}，不要求罗列所有可能组件组合。

## 5. 观察不足以支持机制或因果

> {{FIGURE_OR_ANALYSIS}} 显示 {{OBSERVATION}}，这与 {{PROPOSED_EXPLANATION}} 一致，但 {{ALTERNATIVE_EXPLANATION}} 也可能产生相同现象。{{CLAIM_LOCATION}} 因此尚不能使用 {{CAUSAL_WORDING}}。若机制是核心贡献，建议进行 {{TARGETED_INTERVENTION}} 并核对 {{DISCRIMINATING_OUTCOME}}；若它只是解释性分析，可改写为 {{BOUNDED_INTERPRETATION}}，同时保留定量结果的原有范围。

## 6. 理论前提与算法不一致

> {{THEOREM_LOCATION}} 的结论依赖 {{ASSUMPTION}}，而 {{ALGORITHM_LOCATION}} 实际使用 {{IMPLEMENTED_OPERATION}}。目前缺少从这一实现到该假设的依据，故 {{THEORETICAL_RESULT}} 不能直接作为 {{IMPLEMENTED_METHOD_CLAIM}} 的保证。建议证明 {{APPLICATION_OBLIGATION}}、加入可核查的 {{ERROR_CONTROL}}，或把定理明确限定于 {{IDEALIZED_CASE}}。后者可以解决误用，但不构成对原实现的完整保证。

## 7. 命题存在有效反例

> {{STATEMENT_LOCATION}} 声称 {{EXACT_STATEMENT}}。取 {{COUNTEREXAMPLE_OBJECTS}} 时，{{ASSUMPTION_CHECK}} 满足其前提，而 {{COMPUTATION}} 与结论矛盾。因此需要修正该命题，不能仅补充措辞。建议检查是否缺少 {{POSSIBLE_CONDITION}}，并在新命题下重新证明；若不能恢复，则删除 {{DEPENDENT_CLAIM}} 并重新评估剩余贡献。该反例不涉及 {{UNAFFECTED_SCOPE}}。

## 8. Lean 检查与科学主张之间缺少映射

> 提供的 {{LEAN_ARTIFACT_AND_STATUS}} 涉及 {{ENCODED_STATEMENT}}，而正文 {{LOCATION}} 声称 {{SCIENTIFIC_CLAIM}}。两者之间仍需建立 {{MISSING_SEMANTIC_OR_APPLICATION_LINK}}。因此即使所编码声明通过检查，也不能据此认定 {{STRONGER_CLAIM}} 已被验证。请提供 {{NEEDED_MAPPING_OR_PROOF}}，并分别报告构建状态、证明依赖和论文覆盖范围；若仅完成通用引理，应同步调整验证表述。

## 9. 统计结论超出已报告信息

> {{LOCATION}} 依据 {{REPORTED_SUMMARY}} 使用了 {{INFERENTIAL_WORDING}}，但缺少 {{DESIGN_OR_UNCERTAINTY_DETAIL}}，目前只能得出 {{DESCRIPTIVE_RESULT}}。建议先明确比较单位、聚合方式与 {{PAIRED_OR_UNPAIRED_DESIGN}}，再用适当的差值分析检验 {{TARGET_HYPOTHESIS}}；若原始数据不可得，应撤去相应推断并保留描述性比较。误差条重叠或未拒绝零假设均不能替代等效性证据。

## 10. 效率收益口径不完整

> {{EFFICIENCY_LOCATION}} 报告 {{MEASURED_COST}}，但 {{CLAIM_LOCATION}} 将其解释为 {{END_TO_END_CLAIM}}。当前计时未覆盖／尚未说明 {{COST_COMPONENT}}，且 {{QUALITY_OR_BUDGET_CONDITION}} 不明确。建议补充匹配条件下的 {{MINIMAL_COST_MEASUREMENT}}，或将结论限定为已测的 {{MEASUREMENT_SCOPE}}。核验应同时关注成本与输出质量，不能仅依据渐近复杂度或对数差值宣称速度倍数。

## 11. 图表与正文存在可复核矛盾

> 按 {{DEFINED_AGGREGATION}} 计算，{{INPUT_LOCATIONS_AND_VALUES}} 得到 {{RECOMPUTED_RESULT}}，而 {{TEXT_LOCATION}} 写为 {{REPORTED_RESULT}}。在 {{ROUNDING_TOLERANCE}} 内二者仍不一致，影响了 {{AFFECTED_CLAIM}}。请核对源数据、汇总代码与所有引用位置，并以 {{CONSISTENT_OUTPUTS}} 作为关闭依据。当前可确认的是这一内部矛盾，不能据此推断数据产生过程存在不端。

如果聚合口径不明确，改用：“现有信息允许 {{AGGREGATION_A}} 与 {{AGGREGATION_B}} 两种解释，分别得到 {{RESULTS}}。请先给出实际聚合定义；目前将其列为口径待澄清，不判定算术错误。”

## 12. 适用范围与失败条件被忽略

> {{RESULT_LOCATION}} 中，{{CONDITION_A}} 支持 {{CLAIM}}，但 {{CONDITION_B}} 出现 {{FAILURE_OR_REVERSAL}}。因此 {{UNIVERSAL_WORDING}} 超出了已经观察到的范围。建议保留完整条件结果，讨论 {{BOUNDARY}}，并把摘要与结论改为 {{SUPPORTED_CONDITIONAL_STATEMENT}}。只有希望保留更广的结论时，才需要进一步研究 {{UNTESTED_SCOPE}}。

## 13. 局部表达或标记影响理解

> {{LOCATION}} 的 {{LABEL_OR_DEFINITION}} 与 {{RELATED_LOCATION}} 不一致，使 {{LOCAL_READING}} 容易产生歧义。请统一为 {{VERIFIED_TERM_OR_UNIT}}，并核对图注及正文引用。本项在 {{CENTRAL_INTERPRETATION_UNCHANGED}} 的前提下列为次要问题；若核对发现它改变了数值含义，应重新评估严重程度。

## 14. 有价值但非必要的提升

> {{CURRENT_EVIDENCE}} 已支持 {{CURRENT_CLAIM}}。进一步研究 {{EXTENSION}} 可以回答 {{NEW_QUESTION}}，有助于增强 {{LONGER_TERM_VALUE}}。由于该问题超出当前主张范围，将其列为可选增强；不开展时，只需避免在正文暗示相关结论已经建立。

## 通用英文成段模板

> The manuscript claims {{CLAIM}} in {{CLAIM_LOCATION}}. However, {{EVIDENCE_LOCATION}} establishes {{OBSERVED_RESULT}} under {{CONDITIONS}}, which does not yet distinguish {{EXPLANATION_A}} from {{EXPLANATION_B}}. This matters because {{IMPACT_ON_CONCLUSION}}. A focused way to resolve the concern is to {{MINIMAL_ACTION}} while holding {{CONTROLS}} fixed. Alternatively, the authors could restrict the claim to {{SUPPORTED_SCOPE}} and revise the affected sections consistently. I would consider this concern resolved once {{VERIFIABLE_CLOSURE_TEST}}.

> A strength of this work is {{STRENGTH}}, supported by {{EVIDENCE_LOCATION}}. It enables {{CONCRETE_VALUE}} within {{SCOPE}}. The remaining question is {{UNCERTAINTY}}; this limits {{SPECIFIC_INTERPRETATION}} without negating {{ESTABLISHED_RESULT}}.
