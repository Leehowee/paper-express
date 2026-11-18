# CCF-A Methods：紧凑而完整的正文模板

选 A（设计与组件）或 B（数学主线）。正文保留定义、核心操作和关键条件，详细展开使用真实附录引用。

## A. 核心设计与组件

### Problem setup

> Given {{INPUT_DEFINITION}}, our goal is to {{TASK_OBJECTIVE}}. We have access to {{AVAILABLE_INFORMATION}}, but do not assume {{UNAVAILABLE_INFORMATION}}. Let {{KEY_SYMBOLS}} denote {{DEFINITIONS}}. The setting differs from {{STANDARD_SETTING}} in {{PRECISE_DIFFERENCE}}.

### Overview

> The key idea of {{METHOD}} is to {{KEY_IDEA}}. As illustrated in {{PIPELINE_FIGURE}}, {{FIRST_OPERATION}} produces {{INTERMEDIATE}}, which is used to {{SECOND_OPERATION}}. The method outputs {{FINAL_OUTPUT}} through {{OUTPUT_STEP}}. The following components implement this dependency.

### {{COMPONENT_1_TITLE}}

> {{OBSTACLE_1}} makes {{DIRECT_APPROACH}} unreliable under {{CONDITION}}. We therefore compute {{INTERMEDIATE_1}} as
>
> \[
> {{CORE_EQUATION_1}}
> \]
>
> where {{LOCAL_DEFINITIONS}}. {{KEY_DESIGN_CHOICE}} controls {{PRECISE_EFFECT}}. The output {{INTERMEDIATE_1}} enters {{NEXT_COMPONENT}} through {{CONNECTION}}.

### {{COMPONENT_2_TITLE}}

> To {{PURPOSE_2}}, we use {{INTERMEDIATE_1}} to {{OPERATION_2}}:
>
> \[
> {{CORE_EQUATION_2}}
> \]
>
> Here, {{LOCAL_DEFINITIONS}}. This operation changes {{ACTUAL_BEHAVIOR}} while preserving {{REQUIRED_PROPERTY}}. We use {{NONSTANDARD_IMPLEMENTATION_CHOICE}} because {{REASON}}; the full implementation is given in Appendix {{IMPLEMENTATION_SECTION}}.

组件数随实际方法调整。未生成方法图或附录时保留明确待补标签，不给不存在的对象编号。

### Training and inference

> We optimize {{TRAINABLE_PARTS}} using {{TRAINING_OBJECTIVE}}. Each iteration {{UPDATE_ORDER}}, with {{IMPORTANT_GRADIENT_OR_APPROXIMATION_CHOICE}}. At inference, {{TEST_INPUT}} is processed by {{INFERENCE_STEPS}} to obtain {{OUTPUT}}. {{TRAIN_ONLY_INFORMATION}} is not used at test time. The main computational cost is {{COST_WITH_SCALE_VARIABLES}}; Appendix {{CONFIG_SECTION}} lists the complete configuration.

测试时需要额外优化或模型调用时，替换为：

> At test time, we additionally {{TEST_TIME_OPERATION}} using {{AVAILABLE_TEST_INFORMATION}}. This adds {{MEASURED_OR_ANALYTICAL_COST}}, included in the comparison in {{COST_LOCATION}}.

## B. 目标—关键推导—可计算算法

### Formulation

> We formulate {{QUESTION}} as {{OBJECTIVE_DESCRIPTION}}, with {{VARIABLES_AND_DOMAINS}}:
>
> \[
> {{OBJECTIVE_EQUATION}}
> \]
>
> The formulation differs from {{CLOSEST_OBJECTIVE}} in {{KEY_CHANGE}}. This change captures {{DESIRED_RELATIONSHIP}}, but introduces {{OPTIMIZATION_OBSTACLE}}.

### Key result

> We resolve this obstacle through {{KEY_REFORMULATION}}. Under {{ESSENTIAL_ASSUMPTIONS}}, the following result relates {{ORIGINAL_OBJECT}} to {{TRACTABLE_OBJECT}}.
>
> **Proposition {{THEOREM_LABEL}}.** {{PRECISE_STATEMENT}}.
>
> The argument first {{KEY_PROOF_STEP_1}}, then {{KEY_PROOF_STEP_2}}. {{CRITICAL_NONSTANDARD_STEP_AND_REASON}}. The full proof appears in Appendix {{PROOF_SECTION}}. This result justifies {{SPECIFIC_ALGORITHMIC_STEP}}, rather than an unrestricted claim about {{UNCOVERED_BEHAVIOR}}.

按 [理论接口](../../../interfaces/theory.md) 的实际结果填写。若没有必要澄清的外推，删去最后的对比限定。理论本身是主贡献时，扩展关键证明步骤，不只留下证明指引。

### Optimization and applicability

> The resulting algorithm alternates {{ACTUAL_STEPS}} and terminates when {{STOPPING_RULE}}. We initialize {{VARIABLES}} with {{INITIALIZATION}}. In practice, {{APPROXIMATION}} replaces {{EXACT_OPERATION}}. Therefore, the guarantee above applies when {{APPLICABILITY_CONDITION}}; otherwise, {{ACCURATE_STATUS_OF_IMPLEMENTED_VARIANT}}. Algorithm {{ALGORITHM_LABEL}} in {{ACTUAL_LOCATION}} gives the full procedure.

## 可选：模块为何必要的一句话连接

> Without {{DESIGN}}, {{MATHEMATICAL_FAILURE_OR_TESTABLE_PREDICTION}}. We examine this prediction by {{ACTUAL_CONTROL}} in {{ABLATION_LOCATION}}.

## 润色 1：把冗长细节压到“为什么—怎样—去哪里核查”

原稿：

> {{COMPONENT}} has many operations. First we {{STEP_1}}. Then we {{STEP_2}}. Next we {{STEP_3}}. We repeat {{STANDARD_DETAIL}}. There are many parameters, including {{LONG_PARAMETER_LIST}}.

补充材料：这些操作的共同目的、决定性变化和已存在的配置位置。

改写：

> {{COMPONENT}} estimates {{OUTPUT}} from {{INPUT}} by {{KEY_OPERATION}}. The central choice is {{NONSTANDARD_CHOICE}}, which {{RATIONALE}}. We retain {{ESSENTIAL_PARAMETER_OR_CONDITION}} in the main formulation; Appendix {{DETAIL_SECTION}} specifies the remaining operations and configuration.

不能将决定方法含义的近似、监督或梯度操作藏进“remaining operations”。

## 润色 2：保留假设，缩短理论说明

原稿：

> We provide a theorem in the appendix. It proves that our method is correct and always converges.

补充材料：已完成的准确命题。

改写：

> Under {{ASSUMPTIONS}}, Proposition {{LABEL}} establishes {{EXACT_CONVERGENCE_OR_CORRECTNESS_PROPERTY}} for {{OBJECT}}. The key step is {{PROOF_IDEA}}; Appendix {{PROOF_SECTION}} provides the full argument.

没有命题材料时，用 `[待补：命题、前提与证明状态]`，不将笼统保证润色成更流畅的笼统保证。
