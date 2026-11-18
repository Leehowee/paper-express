# 可填充图注、表注与正文衔接

从数据和方法材料填写 `{{字段}}`，删除不适用的句子。图注交代“展示了什么、怎样得到、怎样读”；正文说明“这对主张意味着什么”。没有实测结果时保留待补字段。`suggests`、`supports`、`demonstrates` 的选择取决于证据，不能只靠替换动词提高结论强度。

## 1. 动机实验：现象与条件

> **{{OBSERVED_PHENOMENON}}.** (a) {{METRIC}} of {{METHODS}} as {{FACTOR}} varies over {{RANGE}}, with {{CONTROLS}} held fixed. (b) {{DIAGNOSTIC_OR_INTERVENTION}} under {{MATCHED_SETTING}}. Points show {{STATISTIC}} and error bars indicate {{UNCERTAINTY}} across {{N}} independent {{UNIT}}. {{IMPORTANT_REVERSAL_OR_BOUNDARY}}.

正文：`Figure {{ID}} shows that {{OBSERVATION}} under {{CONDITION}}. This motivates {{RESEARCH_QUESTION}}, which we examine using {{FOLLOW_UP_CONTROL}}.`

布局：左侧主要现象 → 右侧诊断；如只有一个清楚的现象，可以只保留一个面板。使用 F01。不要把示意曲线写成测量。

## 2. 路线比较：共同对象与差异

> **Conceptual comparison of {{ROUTES}} for {{TASK}}.** Both routes receive {{SHARED_INPUT}} and produce {{SHARED_OUTPUT}}. The prior route requires {{PRIOR_ASSUMPTION}}; the proposed route introduces {{CHANGED_OPERATION_OR_INFORMATION}} at {{LOCATION}}. {{LINE_OR_COLOUR_KEY}}. The diagram describes information flow and assumptions; quantitative comparisons are reported in {{RESULT_LOCATION}}.

正文：`The distinction in Figure {{ID}} is {{PRECISE_DIFFERENCE}}, which changes {{CONSTRAINT_OR_COMPUTATION}}.`

布局：输入列对齐、对应处理列对齐、输出列对齐；新增信息单列标注。使用 D01。适用于确有路线差异的工作，不强行为每篇论文增加一张比较图。

## 3. 方法主图：总流程与局部展开

> **Overview of {{METHOD}}.** {{INPUTS}} are encoded into {{REPRESENTATIONS}}. The {{FOCAL_MODULE}} computes {{OBJECT}} using {{CONDITION}}, followed by {{OUTPUT_STAGE}}. The inset expands {{OPERATION}}, corresponding to Eq. {{EQUATION}}. Solid arrows indicate {{FORWARD_FLOW}}; dashed arrows indicate {{TRAINING_OR_UPDATE_FLOW}}. {{FROZEN_OR_TRAINABLE_KEY}}. At inference, {{TEST_TIME_PATH}}.

正文：`Figure {{ID}} follows the computation from {{INPUT}} to {{OUTPUT}}. The central design is {{MODULE}}, whose purpose is {{CLAIM_WITH_BOUNDARY}}.`

布局：两路输入 → 表征 → 核心模块及矩阵/算子展开 → 输出；训练目标独立一层。使用 D02。若没有反馈更新，删除返回箭头。

## 4. 主实验表：协议、统计与标记

> **{{TASK}} results on {{DATASETS}}.** Methods are grouped by {{COMPARISON_PROTOCOL}}. Entries report {{MEAN_OR_OTHER_STATISTIC}} {{UNCERTAINTY_NOTATION}} over {{N}} independent {{UNIT}}. Arrows indicate the preferred metric direction. Bold marks {{EXACT_BOLD_RULE}} within {{RANKING_SCOPE}}; {{TIE_RULE}}. {{MISSING_CODES_AND_REASONS}}. {{QUOTED_VS_REPRODUCED_RESULTS_AND_EXTRA_SUPERVISION}}.

正文：`Under {{MATCHED_SETTING}}, {{METHOD}} achieves {{RESULT}} on {{SPECIFIC_METRICS}} (Table {{ID}}). The exception on {{SETTING}} suggests {{BOUNDED_INTERPRETATION}}.`

使用 T01。默认代码的粗体只是“可比块内按显示精度并列的最优均值”，不表示统计显著。如需要论文中的统计检验标记，应另有原始结果、检验方案和实现，不能直接改表注。

## 5. 消融：改变什么以及影响多大

> **Effect of {{COMPONENT_OR_STRATEGY}}.** Each variant changes {{CONTROLLED_CHANGE}} while preserving {{FIXED_FACTORS}}. {{ON_OFF_OR_VARIANT_DEFINITION}}. The left panel reports {{METRIC}}; the right panel reports {{REFERENCE_MINUS_VARIANT}} for matched {{UNIT}}. Values and error bars denote {{STATISTIC_AND_UNCERTAINTY}}, with n = {{N}}. {{ALTERNATIVE_STRATEGY_OR_NEGATIVE_RESULT}}.

正文：`Removing {{COMPONENT}} changes {{METRIC}} by {{DELTA_WITH_UNIT}} under {{CONDITION}}. This supports {{FUNCTION}} within this setting, while {{EXCEPTION}} limits a broader necessity claim.`

使用 F04 / T02。对于目标函数与求解器同时变化的研究，将表格展开为“旧目标×旧求解器、旧目标×新求解器、新目标×旧求解器、新目标×新求解器”，说明哪些组合不可定义；不能把所有收益归因于其中一项。

## 6. 机制：分布、矩阵、权重或投影

> **{{DIAGNOSTIC_QUANTITY}} under {{CONDITION}}.** (a) {{GROUPS}} are compared using {{SHARED_BINS_OR_NORMALIZATION}}. (b) {{MATRICES_OR_REPRESENTATIONS}} use the same {{SAMPLE_IDS_AND_ORDER}} and {{COLOUR_SCALE_OR_PROJECTION_PROTOCOL}}. {{REFERENCE_ANNOTATION_SOURCE}}. The observed {{PATTERN}} is consistent with {{HYPOTHESIS}}; the intervention testing its contribution is reported in {{ABLATION_LOCATION}}.

使用 F05 / F06 / F12 / F13。补充字段：密度的样本单位与样本数；注意力的层/头/样本聚合；权重归一化；t-SNE/UMAP 的样本、随机种子、参数及联合/分别拟合方式。示例 F13 只是合成二维坐标，没有运行降维算法。多矩阵色条数量必须在图注中命名；热力图“更整齐”不直接证明效果原因。

## 7. 参数：测试范围与选择依据

> **Sensitivity to {{PARAMETERS}}.** {{OTHER_SETTINGS}} are fixed, and each point/cell corresponds to {{EVALUATION_UNIT}}. The tested values are {{VALUES_OR_RANGE}}; {{LINEAR_LOG_OR_DISCRETE_GRID}} spacing is used. The default {{VALUE}} is selected using {{VALIDATION_RULE}} and marked by {{MARK}}. {{UNCERTAINTY_AND_N}}. Grey cells denote {{FAILURE_OR_MISSING_REASON}}.

正文：`Performance varies by {{AMOUNT}} over {{TESTED_REGION}}, with deterioration at {{BOUNDARY}}. We use {{DEFAULT}} according to {{SELECTION_RULE}}; the result does not establish insensitivity outside the tested range.`

使用 F07 / F08 / T03。一个参数的两阶段边界不是两个任意可独立变化的参数；先明确可行域。离散热力图可用等宽单元格，但须写明是已测组合，不表示连续距离。

## 8. 稳健性：完整扰动范围

> **Robustness to {{STRESSOR}}.** {{STRESSOR_DEFINITION}} is varied from {{LOW}} to {{HIGH}} using {{GENERATION_PROTOCOL}}. All methods share {{MATCHED_SPLITS_PATTERNS_OR_BUDGETS}}. Points show {{STATISTIC}} across {{N}} independent {{UNIT}}, with {{UNCERTAINTY}}. {{CROSSOVER_OR_EXTREME_FAILURE}}.

使用 F09。正文限定为已测噪声/缺失机制；不能将一种随机缺失结果推广到所有非随机缺失。

## 9. 过程与效率：目标、性能和成本分开

> **Optimization trajectory and task performance.** (a) {{OBJECTIVE}} and (b) {{TASK_METRIC}} across {{ITERATIONS_OR_TIME}}, using {{MATCHED_INITIALIZATION_AND_BUDGET}}. The vertical marker indicates {{PHASE_CHANGE}}. {{STATISTIC_AND_N}}. These trajectories describe observed optimization behaviour; the theoretical convergence statement is given in {{THEOREM_AND_ASSUMPTIONS}}.

> **Quality–cost trade-off under {{PROTOCOL}}.** Cost is measured as {{UNIT_AND_SCOPE}} on {{HARDWARE_SOFTWARE_BATCH_PRECISION_INPUT}}. Points and error bars show {{STATISTIC_AND_UNCERTAINTY}} over {{N}} independent {{UNIT}}. The dashed line connects nondominated mean measurements among the tested methods; it does not imply interpolation or statistical dominance. {{OOM_TIMEOUT_AND_EXCLUSIONS}}.

使用 F10 / F11 / T04。如果横轴是 log(time)，注明对数底；相对“对数时间”的数值不能作为速度倍率。

## 10. 案例：选择、对应与失败

> **Qualitative examples selected by {{SELECTION_RULE}}.** Rows correspond to {{SAMPLE_IDS_OR_STRATA}}; columns show {{INPUT_BASELINES_PROPOSED_REFERENCE}}. The same {{CROP_TIME_RANGE_QUERY_CRITERION}} is used for each comparison. {{COLOUR_ROI_OR_RANK_KEY}}. {{FAILURE_ID}} illustrates {{OBSERVED_FAILURE}}. {{ANNOTATION_SOURCE_AND_UNVERIFIED_MODEL_EXPLANATION_NOTE}}. These examples illustrate behaviour and do not estimate its prevalence.

使用 F14 / D03 / D04。检索可以填入 `rank before → rank after`、相关性标注来源和候选全集；图像恢复需保持裁剪、色阶、显示增强和放大区域一致。

## 11. 润色示例

原文：`Our method is clearly the best and robust to all parameters. The attention map proves our mechanism.`

可填充修改稿：`Under {{MATCHED_PROTOCOL}}, the method attains {{RESULT}} on {{METRICS}}, with {{EXCEPTION}}. Performance remains within {{RANGE}} over the tested {{PARAMETER_VALUES}}. The attention pattern is consistent with {{HYPOTHESIS}}; its functional contribution is assessed by {{INTERVENTION}}.`

修改的重点是补齐比较范围、异常与证据层级。缺少相应数据时保留待补标记，不替作者写出胜负或机制结论。

## 12. 已填充的合成示例

对应 [F04 配置](../examples/configs/F04-ablation.json) 与 [原始三次运行](../examples/data/F04-ablation.csv)：

> **Synthetic demonstration of component ablation.** The left panel reports mean accuracy, and the right panel reports the full model minus each variant for three matched synthetic seeds. Error bars indicate sample standard deviations (n = 3). The full model has a mean accuracy of 81.0%, compared with 76.0% without reliability and 78.0% without adaptation. The frozen-update alternative reaches 82.0%; this adverse comparison is retained. These values demonstrate the template and are not experimental findings.

这个例子同时说明：性能差使用百分点；配对差的 SD 从逐次差计算；替代策略可能优于完整模型；示例必须保留合成标识。
