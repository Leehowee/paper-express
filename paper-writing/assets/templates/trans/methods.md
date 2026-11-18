# Trans Methods：从定义到算法的初稿模板

先选 A（目标与求解）或 B（框架与组件），再加入适用的理论、代价和关系模块。小节标题可以直接改成论文标题；段落说明不进入正文。公式槽位使用实际公式，不由句型推造算法。

## A. 目标构造—求解—性质

### A1. Problem formulation

> Let {{DATA_SYMBOL}} denote {{DATA_DEFINITION}}, where {{INDEX_AND_DIMENSION_DEFINITIONS}}. We observe {{AVAILABLE_INFORMATION}} and seek {{OUTPUT_OR_UNKNOWN}}. Unlike the standard setting in which {{STANDARD_ASSUMPTION}}, the present problem allows {{TARGET_CONDITION}}. The objective is to {{TASK_OBJECTIVE}} subject to {{TASK_CONSTRAINTS}}. Throughout this section, {{ESSENTIAL_ASSUMPTIONS}}.

> A direct formulation is {{BASELINE_FORMULATION}}. However, {{SPECIFIC_LIMITATION}} prevents it from {{REQUIRED_BEHAVIOR}}. We therefore treat {{NEW_VARIABLE_OR_RELATION}} as {{MODELING_ROLE}}, which allows {{INTENDED_INTERACTION}} to be represented within the learning objective.

### A2. Proposed objective

> We define the objective as
>
> \[
> {{OBJECTIVE_LATEX}}
> \]
>
> Here, {{VARIABLE_DEFINITIONS}}. The term {{FIRST_TERM}} measures {{FIRST_TERM_ROLE}}, and {{SECOND_TERM}} accounts for {{SECOND_TERM_ROLE}}. The coefficient {{COEFFICIENT}} controls {{TRADEOFF}}. The constraint {{CONSTRAINT}} is imposed because {{CONSTRAINT_REASON}}. Together, these terms encode {{DESIGN_PRINCIPLE}}.

> The use of {{KEY_TERM_OR_CONSTRAINT}} is motivated by {{SPECIFIC_DIFFICULTY}}. Without this term, {{MATHEMATICAL_CONSEQUENCE_OR_HYPOTHESIS}}. In comparison, {{PROPOSED_OPERATION}} changes {{PRECISE_BEHAVIOR}}. We distinguish this design rationale from its empirical effect, which is evaluated by {{ABLATION_REFERENCE}}.

如果没有已完成消融，最后一句改为待补位置。多个目标项不必按模板数量凑齐；只有单项目标时删去第二项与权重说明。

### A3. Reformulation and optimization

> Directly optimizing {{OBJECTIVE_REFERENCE}} is difficult because {{OPTIMIZATION_OBSTACLE}}. We address this by {{REFORMULATION_OR_SOLVER_STRATEGY}}. Under {{CONDITIONS}}, {{ORIGINAL_EXPRESSION}} is {{EXACT_OR_APPROXIMATE_RELATION}} to {{TRACTABLE_EXPRESSION}}. This relation permits {{COMPUTABLE_OPERATION}} while retaining {{PRESERVED_PROPERTY}}.

> With {{FIXED_VARIABLES}} fixed, the subproblem for {{UPDATED_VARIABLE}} becomes {{SUBPROBLEM}}. We solve it using {{ACTUAL_SOLVER}}, yielding {{UPDATE_EXPRESSION_OR_PROCEDURE}}. The update satisfies {{SUPPORTED_CONSTRAINT_PROPERTY}} because {{REASON_OR_REFERENCE}}. We use {{NUMERICAL_TREATMENT}} when {{EDGE_CONDITION}}.

> We then update {{NEXT_VARIABLE}} with {{OTHER_VARIABLES}} fixed. This step {{OPERATION_AND_PURPOSE}}. The complete procedure alternates these updates until {{STOPPING_RULE}}, starting from {{INITIALIZATION}}. Algorithm {{ALGORITHM_LABEL}} summarizes the execution order. The final {{OUTPUT}} is obtained by {{POSTPROCESSING_OR_INFERENCE_STEP}}.

仅有一个更新时合并最后两段。不要把“交替更新”自动接成“必然收敛”；该性质由理论模块单独决定。

### A4. Implementation choices

> The implementation differs from the idealized formulation in {{APPROXIMATION_OR_FINITE_PRECISION_CHOICE}}. In particular, {{ACTUAL_COMPUTATION}} replaces {{IDEAL_COMPUTATION}} to reduce {{COST}}. We use {{TOLERANCE_OR_BUDGET}} and handle {{DEGENERATE_CASE}} by {{FALLBACK}}. The implications of this approximation for {{THEORETICAL_PROPERTY}} are {{VERIFIED_IMPLICATION_OR_UNRESOLVED_STATUS}}.

实际没有该差异时删除整段。

## B. 整体框架—关键组件—训练与推理

### B1. Overview

> Given {{INPUT}}, {{METHOD}} produces {{OUTPUT}} through {{CORE_PRINCIPLE}}. As shown in {{PIPELINE_FIGURE}}, {{FIRST_COMPONENT}} computes {{INTERMEDIATE_1}}, which is used by {{SECOND_COMPONENT}} to obtain {{INTERMEDIATE_2}}. The final {{OUTPUT_COMPONENT}} converts {{INTERMEDIATE_2}} into {{OUTPUT}}. The design addresses {{CHALLENGES}} through {{CORRESPONDING_ACTIONS}}.

### B2. 核心组件段，可按实际依赖复用

> The purpose of {{COMPONENT}} is to {{SPECIFIC_PURPOSE}}. Given {{COMPONENT_INPUT}}, we compute {{COMPONENT_OUTPUT}} as {{COMPONENT_EQUATION}}. In this expression, {{LOCAL_SYMBOLS}}. {{KEY_CHOICE}} is used to {{REASON}}, whereas {{DIRECT_ALTERNATIVE}} would {{SUPPORTED_DIFFERENCE}}. The output enters {{DOWNSTREAM_OPERATION}} through {{EXPLICIT_CONNECTION}}.

> To prevent {{IDENTIFIED_DEGENERACY}}, we introduce {{ACTUAL_CONSTRAINT_OR_NORMALIZATION}}. This operation {{EXACT_EFFECT}}, rather than establishing an unrestricted guarantee of {{UNPROVEN_PROPERTY}}. Its practical role is examined in {{CONTROL_REFERENCE}}.

第二段只用于确实需要解释退化情形的组件；不必每个组件都补一段限制。

### B3. Training objective and inference

> We train {{TRAINABLE_PARTS}} by minimizing {{TRAINING_OBJECTIVE}} over {{TRAINING_DATA}}. During each iteration, {{ACTUAL_UPDATE_ORDER}}. The parameters of {{FROZEN_PARTS}} remain fixed, and gradients {{GRADIENT_FLOW_DESCRIPTION}}. We select {{MODEL_OR_HYPERPARAMETERS}} using {{SELECTION_PROTOCOL}}.

> At inference, the method receives {{TEST_INPUT}} and applies {{INFERENCE_STEPS}}. It does not require {{TRAIN_ONLY_INFORMATION}}. When {{TEST_TIME_UPDATE_OR_EXTERNAL_MODEL}} is used, {{ADDITIONAL_OPERATION_AND_COST}}. This distinction is reflected in the evaluation protocol in {{EXPERIMENT_SECTION}}.

“不需要某信息”必须由实际实现支持；没有冻结、截断或测试时更新就删除相应句子。

## 理论模块：命题、证明与方法含义

仅在 [理论接口](../../../interfaces/theory.md) 提供相应内容后填充。

> We next examine {{PRECISE_PROPERTY}} of {{MATHEMATICAL_OBJECT}}. The analysis assumes {{ASSUMPTIONS}}, which correspond to {{RELATION_TO_IMPLEMENTATION}}.
>
> **Proposition {{THEOREM_LABEL}} ({{PROPERTY_NAME}}).** Under {{COMPLETE_ASSUMPTIONS}}, {{PRECISE_STATEMENT_WITH_QUANTIFIERS}}.
>
> **Proof.** {{INITIAL_DEFINITION_OR_IDENTITY}}. Applying {{LEMMA_OR_ARGUMENT}} gives {{INTERMEDIATE_RESULT}}. Since {{REQUIRED_CONDITION}}, {{FINAL_STEP}}. Therefore, {{EXACT_CONCLUSION}}. □
>
> The proposition shows {{MEANING_FOR_METHOD}}. It applies to {{GUARANTEED_OBJECT}}; the corresponding claim for {{ACTUAL_APPROXIMATION_OR_OUTPUT}} requires {{ADDITIONAL_CONDITION_OR_EVIDENCE}}.

长证明展开为完整正文小节；不能以这几句骨架代替缺失推导。含占位步骤时标注证明未完成。Lean 状态按接口记录，不自动写入每段理论正文。

## 复杂度与实际代价

> Let {{SCALE_VARIABLES}} denote {{MEANINGS}}. Computing {{OPERATION_1}} requires {{COST_1}}, while {{OPERATION_2}} requires {{COST_2}} per iteration. With {{ITERATION_COUNTS}}, the total time complexity is {{TOTAL_COST}} and the storage requirement is {{MEMORY_COST}}. The dependence on {{PRIMARY_SCALE}} is {{SCALING_CLAIM}} when {{FIXED_QUANTITIES}} are held fixed. This accounting includes {{INCLUDED_COSTS}}; {{SEPARATE_COSTS}} are reported separately in {{COST_LOCATION}}.

## 与最近方法的关系

> Both {{METHOD}} and {{CLOSEST_METHOD}} use {{SHARED_ELEMENT}}. The difference lies in {{OBJECTIVE_OR_INFORMATION_OR_SOLVER_CHANGE}}. Under {{SPECIAL_CONDITION}}, {{VERIFIED_RELATIONSHIP}}. Outside this case, {{CONCRETE_DIFFERENCE}} leads to {{EXPECTED_OR_ESTABLISHED_CONSEQUENCE}}. We isolate this difference with {{CONTROL_DESIGN}}.

## 润色 1：给突然出现的公式补上推导职责

原稿：

> We introduce {{OBJECTIVE}}. {{FORMULA}}. {{SYMBOL}} is a parameter. We use {{SOLVER}} to solve it.

补充材料：目标针对的困难、每项的角色和真实求解方式。

改写：

> To address {{OBSTACLE}}, we optimize {{OBJECTIVE}}. The term {{TERM}} measures {{QUANTITY}}, while {{CONSTRAINT}} preserves {{REQUIRED_PROPERTY}}. The parameter {{SYMBOL}} controls {{TRADEOFF}}. Because {{SOLVER_RELEVANT_STRUCTURE}}, we solve the problem using {{SOLVER}}, with {{ACTUAL_UPDATE_AND_STOPPING_RULE}}.

## 润色 2：将经验收敛与理论结论分开

原稿：`The loss always decreases, proving that our algorithm reaches the global optimum.`

已知材料只有有限实验曲线时：

> In the evaluated runs, the objective {{OBSERVED_TRAJECTORY}} and stabilizes after {{OBSERVED_RANGE}} iterations. This documents the empirical behavior of the implemented algorithm. A global optimality claim would require a separate analysis of {{ACTUAL_OBJECTIVE_AND_SOLVER}}.

有理论结果时，用上述命题模块准确写出；不能仅把 `proving` 换成 `demonstrating` 保留同一过强结论。
