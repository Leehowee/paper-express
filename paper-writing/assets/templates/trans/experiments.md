# Trans Experiments：可拼装的结果叙述

以下模块按论证需要组合成完整章节。默认先设置和主结果，再放能够区分贡献来源的控制，最后展开代价与边界。段落内的结果、解释与引用均需已有材料支持。

## 1. 章节开头

> We evaluate {{METHOD}} to answer three questions: whether {{PRIMARY_PERFORMANCE_QUESTION}}, whether {{DESIGN_OR_MECHANISM_QUESTION}}, and under which conditions {{BOUNDARY_QUESTION}}. We first describe the evaluation protocol and compare {{METHOD}} with {{BASELINE_FAMILIES}}. We then isolate {{KEY_DESIGNS}} through controlled experiments and examine {{COST_AND_ROBUSTNESS_FACTORS}}.

问题数量按实际内容调整，不为凑齐三问新增实验承诺。

## 2. Experimental setup

> We use {{DATASETS_AND_VERSIONS}}, covering {{RELEVANT_VARIATION}}. The data are split into {{TRAIN_VALIDATION_TEST_SPLITS}} using {{SPLIT_RULE}}. We apply {{PREPROCESSING}} and evaluate {{TARGET_OUTPUT}} with {{METRICS_AND_DIRECTIONS}}. {{SPECIAL_SETTING_DEFINITION}}.

> The comparison includes {{STRONG_BASELINES}}, {{CLOSEST_BASELINE}}, and {{SIMPLE_REFERENCE}}, selected to examine {{COMPARISON_PURPOSES}}. We use {{IMPLEMENTATION_SOURCES}} and align {{MATCHED_FACTORS}} across methods. Differences in {{EXTERNAL_DATA_OR_MODEL_OR_SUPERVISION}} are reported in {{PROTOCOL_LOCATION}} and treated as {{DIRECT_OR_REFERENCE_COMPARISON}}.

> Hyperparameters are selected using {{SELECTION_DATA_AND_RULE}}, with {{SEARCH_BUDGET}}. We repeat {{RANDOMIZED_OPERATION}} {{REPEAT_COUNT}} times and report {{AGGREGATE_AND_UNCERTAINTY_DEFINITION}}. Each repeat corresponds to {{INDEPENDENT_UNIT_OR_SEED_VARIATION}}. The experiments run on {{HARDWARE_AND_SOFTWARE}}, and {{COST_SCOPE}} is included in the resource measurements.

单次确定性实验不套“均值±标准差”。合成噪声任务可追加：

> To study {{CORRUPTION_OR_MISSINGNESS}}, we generate {{PERTURBATION}} by {{GENERATION_PROCESS}} at {{LEVELS}}. This process changes {{AFFECTED_INFORMATION}} while preserving {{CONTROLLED_INFORMATION}}. We distinguish these synthetic conditions from {{REAL_WORLD_CONDITION}}, evaluated separately on {{DATA_SOURCE}}.

## 3. Main results：选一种与结果相符的写法

**A. 总体改善，存在例外。**

> Table {{MAIN_TABLE}} compares {{METHOD}} with {{BASELINES}} under {{PROTOCOL}}. Across {{EVALUATION_SCOPE}}, {{AGGREGATE_FINDING}}. Relative to {{COMPARATOR}}, the change in {{METRIC}} is {{CHANGE_AND_UNCERTAINTY}}, with the largest gain observed in {{CONDITION}}. The trend is not uniform: {{EXCEPTION}}. These results support {{BOUNDED_CLAIM}}, particularly when {{SUPPORTED_SETTING}}.

**B. 任务效果相近，但成本不同。**

> {{METHOD}} attains {{PERFORMANCE_RESULT}} compared with {{BASELINE}} while requiring {{RESOURCE_RESULT}} under {{MATCHED_PROTOCOL}}. The difference in {{METRIC}} is {{MEASURED_DIFFERENCE}}, and the corresponding change in {{COST}} is {{MEASURED_COST_CHANGE}}. This trade-off is relevant when {{RESOURCE_CONSTRAINT}}. It does not establish an advantage for {{SETTING_WHERE_TRADEOFF_IS_UNFAVORABLE}}.

没有等效性分析时，不把“差值小”改成统计等效；最后一句只在存在相应范围问题时保留。

**C. 效果依赖条件。**

> The effect of {{METHOD}} depends on {{CONDITION_VARIABLE}}. As {{VARIABLE}} changes from {{RANGE_START}} to {{RANGE_END}}, {{OBSERVED_TREND}}. The method improves {{TARGET_METRIC}} in {{BENEFICIAL_REGION}}, but {{FAILURE_OR_NO_GAIN}} in {{OTHER_REGION}}. This pattern narrows the applicability claim to {{SUPPORTED_REGION}} and motivates the analysis of {{POSSIBLE_EXPLANATION}} below.

## 4. 核心消融

> To test whether {{DESIGN}} contributes to {{TARGET_EFFECT}}, we compare the full model with {{REMOVAL_OR_REPLACEMENT_VARIANT}}. The variants share {{CONTROLLED_FACTORS}} and differ only in {{INTENDED_DIFFERENCE}}. As shown in {{ABLATION_TABLE}}, {{OBSERVED_CHANGE_AND_UNCERTAINTY}}. This supports {{LOCAL_CONCLUSION}} within {{SETTING}}, while leaving {{ALTERNATIVE_EXPLANATION_OR_SCOPE}} unresolved.

**两个因素同时改变时的交叉对照。**

> The full method changes both {{FACTOR_A}} and {{FACTOR_B}}. We therefore evaluate all feasible combinations of {{A_LEVELS}} and {{B_LEVELS}} under {{MATCHED_BUDGET}}. Holding {{B}} fixed, {{A_EFFECT}}; holding {{A}} fixed, {{B_EFFECT}}. The joint configuration {{JOINT_RESULT}}. This distinguishes the contribution of {{FACTOR_A}} from {{FACTOR_B}} and indicates {{SUPPORTED_INTERACTION_STATEMENT}}.

不把非显著差异写成无作用；不可运行的组合应说明原因，不能补造对照。

## 5. 机制或中间量分析

> The proposed explanation predicts that {{MECHANISM_PREDICTION}}. We test this prediction by measuring {{DIRECT_QUANTITY}} while controlling {{CONFOUNDS}}. Figure {{MECHANISM_FIGURE}} shows {{OBSERVATION}}. Under the intervention {{INTERVENTION}}, {{CONTRASTING_OBSERVATION}}. Together, these findings {{SUPPORTED_INFERENCE_STRENGTH}} {{MECHANISM_CLAIM}}.

只有相关性或可视化时用较弱版本：

> Figure {{FIGURE}} shows that {{INTERMEDIATE_QUANTITY}} varies with {{OUTCOME}} in {{EVALUATED_SETTING}}. This is consistent with {{HYPOTHESIS}}, but does not distinguish it from {{PLAUSIBLE_ALTERNATIVE}}. We therefore interpret the visualization as {{LIMITED_ROLE}}.

## 6. 参数、稳健性与代价

> We vary {{PARAMETER}} over {{TESTED_RANGE}}, keeping {{FIXED_SETTINGS}} unchanged. The default value {{DEFAULT_VALUE}} is selected by {{SELECTION_RULE}}. Figure {{PARAMETER_FIGURE}} shows {{STABLE_OR_SENSITIVE_PATTERN}}, with degradation when {{SENSITIVE_REGION}}. The analysis supports {{RANGE_SPECIFIC_CONCLUSION}}, rather than insensitivity to arbitrary parameter choices.

> We measure {{RUNTIME_MEMORY_OR_COMMUNICATION}} on {{HARDWARE}} for {{DATA_SCALES}}, including {{INCLUDED_OPERATIONS}}. Under {{BUDGET_OR_STOPPING_RULE}}, {{COST_FINDING}}. The observed scaling is {{RELATION_TO_THEORETICAL_ANALYSIS}}. The main overhead comes from {{MEASURED_COMPONENT}}, which accounts for {{MEASURED_SHARE_OR_QUALITATIVE_BREAKDOWN}}.

## 7. 案例与失败

> We select {{CASE_SET}} using {{SELECTION_RULE}} to examine {{CASE_QUESTION}}. In {{SUCCESS_CASE}}, {{VISIBLE_BEHAVIOR}} corresponds to {{QUANTITATIVE_OR_KNOWN_REFERENCE}}. In contrast, {{FAILURE_CASE}} exhibits {{FAILURE_PATTERN}}. This suggests that {{BOUNDED_INTERPRETATION}}, and the frequency of this behavior is {{MEASURED_FREQUENCY_OR_NOT_ESTABLISHED}}.

没有频率估计时直接说明案例不代表总体发生率，不给出猜测比例。

## 8. 章节收束，可选

> The experiments establish {{PRIMARY_FINDING}} under {{EVALUATED_CONDITIONS}}. The controlled comparisons support {{DESIGN_LEVEL_FINDING}}, whereas {{IMPORTANT_FAILURE_OR_COST}} limits {{BROADER_CLAIM}}. These observations define the current scope of {{METHOD}}.

## 润色：从逐行报数变成结果段

原稿：

> On {{D1}}, we get {{R1}}. On {{D2}}, we get {{R2}}. On {{D3}}, we get {{R3}}. The results demonstrate the effectiveness of all our modules.

补充材料：表中全部比较、主要趋势、例外及实际消融。

改写：

> Across {{DATASETS}}, {{MAIN_COMPARATIVE_PATTERN}} (Table {{TABLE}}). The largest change occurs on {{DATASET_OR_CONDITION}}, where {{COMPARISON_AND_MAGNITUDE}}. By contrast, {{EXCEPTION}}. This comparison establishes {{OVERALL_METHOD_CLAIM}}; the roles of individual components are examined separately in {{ABLATION_LOCATION}}.

## 润色：把“因为”改成证据相称的解释

原稿：`The accuracy increases because our representations remove all noise.`

只有任务指标时：

> The method improves {{METRIC}} under {{NOISE_SETTING}}. The result supports its effectiveness in this setting, but the extent of noise removal has not been measured directly.

直接机制测量充分时，再补入该测量和相应范围，不沿用 `all noise`。
