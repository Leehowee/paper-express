# Trans Related Work：主题段与精确比较

## A. 每条研究路线一个主题段

**主题入口。**

> {{RESEARCH_FAMILY}} studies {{COMMON_PROBLEM}} under {{SHARED_SETTING}}. Early approaches {{EARLY_MECHANISM}} {{CITATIONS}}, while subsequent work incorporates {{LATER_ADVANCE}} to handle {{ADDITIONAL_REQUIREMENT}} {{CITATIONS}}. These methods differ mainly in {{COMPARISON_DIMENSION}}, which determines {{CONSEQUENCE_FOR_THE_TASK}}.

**与本文的关系。**

> Within this family, {{CLOSEST_METHOD}} is most closely related to our work because {{SHARED_COMPONENT_OR_GOAL}} {{CITATION}}. It assumes {{PRIOR_ASSUMPTION}} and optimizes {{PRIOR_OBJECTIVE}}. Our method retains {{INHERITED_ELEMENT}} but changes {{SUBSTANTIVE_DIFFERENCE}} to address {{TARGET_CONDITION}}. The effect of this change is examined in {{METHOD_OR_EXPERIMENT_SECTION}}.

对两到三个实际相关主题分别使用，不强制相同句式。历史不影响当前比较时，删去早期到后续的演进句。

## B. 以数学目标与求解方式组织

**共同定义与已有目标。**

> Let {{SHARED_NOTATION}} denote {{SHARED_OBJECTS}}. Under this notation, {{PRIOR_METHOD_FAMILY}} solves {{PRIOR_FORMULATION}} {{CITATIONS}}. The term {{TERM}} encodes {{MEANING}}, while the constraint {{CONSTRAINT}} enforces {{PROPERTY}}. The standard solution updates {{VARIABLES}} through {{SOLVER}}.

**差异及影响。**

> Our formulation differs in {{OBJECTIVE_OR_CONSTRAINT_CHANGE}}. This changes {{MATHEMATICAL_OR_ALGORITHMIC_CONSEQUENCE}}, so the existing {{SOLVER_OR_ANALYSIS}} cannot be applied directly without {{REQUIRED_ADAPTATION}}. Section {{METHOD_SECTION}} derives {{NEW_PROCEDURE}}, and Section {{EXPERIMENT_SECTION}} separates the effects of {{CHANGED_FACTORS}} through {{CONTROL_DESIGN}}.

“不能直接使用”需要明确理由；若已有算法可以直接使用，就准确说明沿用及新增部分。

## C. 互补关系，无须制造缺点

> {{RELATED_WORK}} focuses on {{THEIR_QUESTION}}, whereas this study examines {{OUR_QUESTION}}. The two settings share {{COMMON_GROUND}} but differ in {{INFORMATION_OR_SCOPE}}. Their findings provide {{USEFUL_FOUNDATION}} for our formulation. We adopt {{BORROWED_ELEMENT}} and investigate {{ADDITIONAL_QUESTION}}, which is not resolved by the original setting alone.

## 润色：从逐篇罗列改成主题比较

原稿：

> A proposed {{TECHNIQUE_A}}. B proposed {{TECHNIQUE_B}}. C proposed {{TECHNIQUE_C}}. Our method is different and better.

补充材料：这些工作的共同问题、差异维度、与本文最接近的工作。

改写：

> Existing approaches address {{COMMON_PROBLEM}} through {{SHARED_STRATEGY}} {{CITATIONS_A_B_C}}. They primarily differ in {{COMPARISON_DIMENSION}}: {{GROUPED_DIFFERENCES}}. Among them, {{CLOSEST_METHOD}} shares {{COMMON_COMPONENT}} with our method. We extend this component to {{NEW_CONDITION}} by {{SPECIFIC_CHANGE}}; the performance comparison is reported under {{MATCHED_SETTING}} in {{RESULT_LOCATION}}.

## 润色：收缩未经核实的“都不能”

原稿：`All previous methods fail to handle {{SETTING}}.`

在已核实最近文献的条件下改为：

> The methods considered here assume {{ASSUMPTION}} {{CITATIONS}}. Applying them to {{SETTING}} therefore requires {{ADAPTATION}}, which is not specified in their original formulations.

若并未核查其原始形式，保留 `[待核实：最近工作的具体适用条件]`，不用绝对判断填补比较。
