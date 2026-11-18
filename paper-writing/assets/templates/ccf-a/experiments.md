# CCF-A Experiments：核心证据的成段模板

按论文主张选择段落，正文保留决定性结果、关键对照及影响结论的边界。完整扫描和额外案例通过准确附录引用展开。实际写作规则见 [直接起草与润色](../../../static/core/drafting-and-polishing.md)。

## 开头与必要设置

> We evaluate whether {{METHOD}} {{CENTRAL_EMPIRICAL_CLAIM}} under {{TARGET_CONDITION}}. Our experiments examine {{MAIN_COMPARISON}}, isolate {{KEY_DESIGN}}, and assess {{IMPORTANT_BOUNDARY_OR_COST}}.

> **Setup.** We use {{DATASETS_AND_SPLITS}} and report {{METRICS_AND_DIRECTION}}. The comparison includes {{BASELINE_FAMILIES}} and {{CLOSEST_METHOD}}, with {{SHARED_INFORMATION_AND_RESOURCE_CONDITIONS}}. {{IMPORTANT_PROTOCOL_DIFFERENCE}}. Hyperparameters are selected using {{SELECTION_PROTOCOL}}. We report {{SUMMARY_STATISTIC}} over {{INDEPENDENT_REPEATS}}, with {{UNCERTAINTY_DEFINITION}}. Appendix {{SETUP_SECTION}} provides {{DETAILS_ACTUALLY_AVAILABLE}}.

没有重复实验时，删除统计句中没有依据的部分并如实说明单次结果。正文必须交代影响比较的信息和资源差异；不能把这些差异全部藏进附录。

有人工噪声、缺失或分布变化时加入：

> To control {{FACTOR}}, we generate {{PERTURBATION}} by {{GENERATION_RULE}} at {{LEVELS}}. This tests {{SPECIFIC_STRESS_CONDITION}}; {{RELATION_TO_REAL_WORLD_DATA}}. All methods are evaluated on {{MATCHED_REALIZATIONS_OR_OTHER_FAIR_PROTOCOL}}.

## 主结果 A：主要收益与适用范围

> **Main results.** {{MAIN_TABLE}} shows that {{METHOD}} {{VERIFIED_COMPARATIVE_RESULT}} under {{COMPARABLE_PROTOCOL}}. The gain is most pronounced on {{CONDITION}}, where {{VERIFIED_MAGNITUDE_OR_PATTERN}}. On {{EXCEPTION_OR_NEAR_TIE}}, {{ACTUAL_RESULT}}. These results support {{BOUNDED_EMPIRICAL_CONCLUSION}} over {{TESTED_SCOPE}}.

不存在明确例外时可以删去例外句；不得为填模板虚构失败。差异很小时，保留实际数值与不确定性，不强行写成“明显提高”。

## 主结果 B：效果与成本的权衡

> **Performance and cost.** At {{MATCHED_BUDGET}}, {{METHOD}} achieves {{VERIFIED_RESULT}} compared with {{BASELINE_RESULT}}. Reaching {{TARGET_QUALITY}} requires {{MEASURED_COST_COMPARISON}}, including {{COST_COMPONENTS}}. The comparison in {{RESULT_LOCATION}} therefore indicates {{SPECIFIC_TRADEOFF}} under {{EVALUATION_CONDITION}}.

若并未控制预算，改为准确披露条件：

> {{METHOD}} achieves {{QUALITY_RESULT}} with {{RESOURCE_USE}}, while {{BASELINE}} uses {{BASELINE_RESOURCE_USE}}. This comparison measures {{QUALITY_COST_TRADEOFF}} at the reported configurations; an equal-budget comparison remains {{ACTUAL_STATUS}}.

## 主结果 C：收益依赖某一条件

> **Dependence on {{FACTOR}}.** As {{FACTOR}} changes from {{RANGE_START}} to {{RANGE_END}}, {{OBSERVED_TREND}}. {{METHOD}} improves over {{BASELINE}} in {{SUPPORTED_REGION}}, but {{OBSERVED_BOUNDARY_RESULT}} in {{OTHER_REGION}}. This pattern limits the empirical claim to {{SUPPORTED_CONDITION}} and motivates the analysis below.

“没有显著差异”不能改写为等效；没有边界实验时不能把未检验范围写成已观察到的失败。

## 核心消融：只改变被检验设计

> **Effect of {{DESIGN}}.** We replace {{DESIGN}} with {{CONTROL}} while keeping {{MATCHED_FACTORS}} fixed. As shown in {{ABLATION_LOCATION}}, this changes {{METRIC}} from {{CONTROL_RESULT}} to {{FULL_RESULT}} under {{CONDITION}}. {{ADDITIONAL_MATCHED_CONTROL_RESULT_IF_AVAILABLE}}. The comparison supports {{PRECISE_COMPONENT_LEVEL_CONCLUSION}}, with {{REMAINING_CONFOUND_OR_SCOPE_LIMIT}}.

没有额外对照时删除对应句。若消融同时改变模型规模、训练步数或可用信息，先披露变化，再降低归因强度。

两个组件的关系是主张核心时加入：

> We additionally evaluate {{FOUR_ACTUAL_VARIANTS}} under the same protocol. {{FACTORIAL_RESULT}}. The contrast {{DEFINED_INTERACTION_CONTRAST}} is {{VERIFIED_VALUE_OR_DIRECTION}}, indicating {{SUPPORTED_RELATIONSHIP}} in this setting.

没有交互对照时，不因完整模型表现最好就声称两个组件具有协同作用。

## 机制分析：干预与观测分别表述

有能区分解释的实验时：

> **Testing {{HYPOTHESIS}}.** This hypothesis predicts {{PREDICTION}}, whereas {{ALTERNATIVE_EXPLANATION}} predicts {{ALTERNATIVE_PREDICTION}} under {{INTERVENTION}}. We therefore {{ACTUAL_TEST}} while controlling {{CONTROLLED_FACTORS}}. {{OBSERVED_RESULT}} in {{FIGURE_OR_TABLE}} supports {{SUPPORTED_INTERPRETATION}} within {{SCOPE}}.

只有可视化或相关性时：

> **Observed behavior.** {{FIGURE}} shows {{MEASURED_PATTERN}} alongside {{OUTCOME_PATTERN}}. This observation is consistent with {{INTERPRETATION}}, but the experiment does not isolate {{UNRESOLVED_DIRECTION_OR_FACTOR}}. We use it to characterize {{OBSERVED_BEHAVIOR}}.

## 参数、效率与边界：可独立插入的短段

> **Sensitivity.** We vary {{PARAMETER}} over {{RANGE}} using {{FIXED_SELECTION_PROTOCOL}}. {{RESULT_PATTERN}} in {{FIGURE}} identifies {{SUPPORTED_REGION_OR_SENSITIVITY}}. The reported setting {{CHOSEN_VALUE}} is selected by {{VALID_SELECTION_RULE}}, with the complete sweep in Appendix {{SWEEP_SECTION}}.

> **Efficiency.** We measure {{TIME_MEMORY_OR_CALLS}} on {{HARDWARE_OR_EXECUTION_ENVIRONMENT}} for {{WORKLOAD}}. The measurement includes {{INCLUDED_STAGES}} and uses {{REPETITION_AND_AGGREGATION}}. {{VERIFIED_COST_RESULT}}. {{QUALITY_AT_THIS_COST}} provides the corresponding performance context.

> **Failure analysis.** Under {{FAILURE_CONDITION}}, {{OBSERVED_FAILURE}}. {{EVIDENCE_LOCATION}} shows {{SUPPORTING_OBSERVATION}}, consistent with {{CAUTIOUS_EXPLANATION}}. This restricts {{SPECIFIC_CLAIM}} to {{SUPPORTED_SCOPE}}. Appendix {{CASE_SECTION}} provides {{ACTUAL_ADDITIONAL_CASES}} selected by {{SELECTION_RULE}}.

只有会改变中心结论或属于主要贡献的分析才在正文充分展开；其他部分保留关键发现和准确入口。删去没有真实材料的句子。

## 润色 1：将逐表复述改成一条结果判断

原稿：

> Table {{LABEL}} gives all results. Our method obtains {{VALUE_1}} on {{DATASET_1}} and {{VALUE_2}} on {{DATASET_2}}. There are also good results on other datasets. We are better than all methods.

补充材料：表中真实的比较范围、最接近基线、差值口径和例外。

改写：

> Across {{VERIFIED_SCOPE}}, {{METHOD}} {{PRECISE_COMPARISON_WITH_CLOSEST_BASELINE}} ({{TABLE}}). The largest gain occurs under {{CONDITION}}, while {{EXCEPTION}}. This pattern supports {{SCOPE_BOUND_CONCLUSION}}.

没有完整表格时，仅保留原文可核实的结果，标注 `[待补：比较范围与基线数值]`，不生成总体优势判断。

## 润色 2：压缩重复设置，保留关键差异

原稿：

> We use the same dataset as before. We use the same split as before. We use the same metric as before. For this experiment, we change {{FACTOR}}. More details are in the appendix.

补充材料：已存在的主实验协议位置、本实验唯一或全部变化、真实附录位置。

改写：

> We follow the protocol in {{MAIN_SETUP_SECTION}} and vary {{FACTOR}} over {{RANGE}}. {{OTHER_DIFFERENCE_IF_ANY}}. Appendix {{DETAIL_SECTION}} lists {{SPECIFIC_CONFIGURATION}}.

检查是否确实沿用主协议，不将数据、监督或资源变化省略成“same setup”。
