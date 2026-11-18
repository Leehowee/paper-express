# Trans Introduction：连续段落套路

每套段落可以直接填充后连成引言。引用槽位填实际文献。段落长度随证据调整，不按固定数量硬凑。

## A. 现有假设在目标场景中失效

**段 1：任务、能力与已有基础。**

> {{TASK}} aims to {{TASK_OBJECTIVE}} and underpins {{CONCRETE_USE_OR_SCIENTIFIC_VALUE}}. In {{SETTING}}, this requires {{REQUIRED_CAPABILITY}}. Existing methods achieve this through {{COMMON_APPROACH}}, with progress in {{ESTABLISHED_ADVANCES}} {{CITATIONS}}. These developments provide a basis for {{KNOWN_CAPABILITY}}, but their applicability depends on {{ASSUMPTION}}.

**段 2：条件失效与后果。**

> The assumption of {{ASSUMPTION}} is difficult to maintain when {{REALISTIC_CONDITION}}. In particular, {{OBSERVATION_OR_DOCUMENTED_EXAMPLE}} {{EVIDENCE_REFERENCE}}. As a result, {{INTERMEDIATE_FAILURE}} affects {{TASK_LEVEL_CONSEQUENCE}}. This motivates the study of {{PRECISE_PROBLEM}}, where {{WHAT_IS_AVAILABLE}} is available but {{WHAT_IS_UNAVAILABLE}} cannot be assumed.

**段 3：最近方案及尚未解决的障碍。**

> A direct approach is to {{STRAIGHTFORWARD_SOLUTION}}. Related methods {{CLOSEST_WORK_BEHAVIOR}} {{CITATIONS}}, which addresses {{SOLVED_PART}}. However, {{REMAINING_OBSTACLE}} persists because {{TECHNICAL_REASON}}. Simply {{OBVIOUS_MODIFICATION}} does not resolve this issue: {{SUPPORTED_REASON}}. The central question is therefore how to {{RESEARCH_QUESTION}} while respecting {{CONSTRAINT}}.

**段 4：关键洞见与设计。**

> Our central idea is to {{KEY_IDEA}}. Instead of treating {{OBJECT}} as {{CONVENTIONAL_ROLE}}, we represent it as {{NEW_ROLE}}, allowing {{INTENDED_INTERACTION}}. Building on this idea, we develop {{METHOD}}. The method first {{OPERATION_1}}, then {{OPERATION_2}}, and finally {{OUTPUT_STEP}}. These operations address {{CHALLENGES_IN_CORRESPONDING_ORDER}}, respectively. {{DESIGN_RATIONALE_OR_THEORETICAL_CONNECTION}}.

“Instead of”句只用于确实存在的比较；方法不涉及对象角色变化时删去。操作数量按真实方法修改。

**段 5：支撑与贡献。**

> We investigate {{METHOD}} through {{ANALYSIS_AND_EVALUATION}}. The analysis establishes {{SUPPORTED_PROPERTY}} under {{ASSUMPTIONS}}, while the experiments examine {{EMPIRICAL_QUESTIONS}}. The results show {{MAIN_RESULT}} and identify {{BOUNDARY}}. The contribution is {{CONTRIBUTION_IN_TERMS_OF_PROBLEM_OR_CAPABILITY}}, supported by {{DECISIVE_EVIDENCE}}.

没有理论结果时删去分析句。贡献需要列表时，将末句替换为下方贡献模块，不重复保留两种总结。

## B. 理论条件不足或优化目标不匹配

**段 1：数学对象为什么关系到任务。**

> {{TASK}} is commonly formulated as {{STANDARD_FORMULATION}} {{CITATIONS}}. This formulation captures {{DESIRED_PROPERTY}}, and its solution determines {{TASK_OUTPUT_OR_BEHAVIOR}}. Existing analyses establish {{KNOWN_RESULT}} when {{KNOWN_ASSUMPTIONS}}. These results leave open {{PRECISE_UNRESOLVED_QUESTION}}, which matters when {{TARGET_SETTING}}.

**段 2：具体障碍。**

> The difficulty arises from {{MATHEMATICAL_OBSTACLE}}. Although {{STANDARD_TECHNIQUE}} can handle {{SUBPROBLEM}}, it does not establish {{MISSING_PROPERTY}} for {{FULL_OBJECT}} because {{REASON}}. Moreover, {{IMPLEMENTATION_CONSTRAINT}} prevents a direct use of {{IDEALIZED_SOLUTION}}. A useful formulation must therefore account for both {{THEORETICAL_REQUIREMENT}} and {{COMPUTATIONAL_REQUIREMENT}}.

**段 3：新观点与结果。**

> We approach this problem by {{KEY_REFORMULATION}}. This exposes {{USEFUL_STRUCTURE}}, from which we derive {{THEOREM_OR_ALGORITHM}}. Under {{ESSENTIAL_ASSUMPTIONS}}, {{EXACT_CONCLUSION}}. The result concerns {{GUARANTEED_OBJECT}}; its implications for {{IMPLEMENTED_METHOD}} depend on {{APPLICABILITY_CONDITION}}.

**段 4：实现、验证与意义。**

> We implement the resulting procedure using {{ACTUAL_SOLVER_OR_APPROXIMATION}} and examine {{VALIDATION_QUESTIONS}}. {{EVIDENCE_SUMMARY}}. Together, the analysis and evaluation clarify {{NEW_UNDERSTANDING}} and provide {{BOUNDED_PRACTICAL_VALUE}}. {{LIMITATION_THAT_CHANGES_INTERPRETATION}}.

## C. 共同结构与统一框架

**段 1：看似不同的路线。**

> Research on {{TASK}} has developed several approaches, including {{FAMILIES}} {{CITATIONS}}. They differ in {{DESIGN_DIMENSIONS}} but share the goal of {{COMMON_GOAL}}. Their relationship is usually described through {{EXISTING_COMPARISON}}, leaving {{UNEXPLAINED_RELATIONSHIP}} unclear.

**段 2：统一对象。**

> We observe that these approaches can be compared through {{COMMON_OBJECT}}. Under {{CONDITIONS}}, {{SUPPORTED_RELATIONSHIP}}. This suggests studying {{UNIFYING_QUESTION}} rather than selecting each {{DESIGN_ELEMENT}} independently. The challenge is to preserve {{IMPORTANT_DIFFERENCES}} while expressing {{SHARED_STRUCTURE}}.

**段 3：框架与实例。**

> We introduce {{FRAMEWORK}}, which represents {{SHARED_STRUCTURE}} as {{FORMULATION}}. Setting {{CHOICE_1}} yields {{VERIFIED_SPECIAL_CASE_1}}, whereas {{CHOICE_2}} gives {{VERIFIED_SPECIAL_CASE_2}}. We further instantiate the framework with {{NEW_INSTANCE}} to address {{TARGET_LIMITATION}}. The distinction between the general formulation and the implemented instances allows us to examine {{COVERAGE_AND_NEW_VALUE}} separately.

**段 4：证据与边界。**

> Our analysis identifies {{THEORETICAL_RELATIONSHIP_AND_CONDITIONS}}. Experiments compare {{INSTANCES_AND_BASELINES}} under {{PROTOCOL}}, showing {{OBSERVED_VARIATION}}. These findings establish {{SUPPORTED_FRAMEWORK_CONTRIBUTION}} within {{SCOPE}}. {{UNCOVERED_CASE}} remains outside the present analysis.

## 可选：期刊扩展说明

> This article extends our earlier study {{PRIOR_CITATION}} by addressing {{NEW_QUESTION}}. The earlier formulation {{PREVIOUS_SCOPE}}, whereas the present work introduces {{SUBSTANTIVE_NEW_METHOD_OR_THEORY}}. We also add {{NEW_EVIDENCE}} to examine {{QUESTION_NOT_PREVIOUSLY_ANSWERED}}. These additions change {{CONCLUSION_OR_APPLICABILITY}}, rather than only increasing the number of evaluations.

只在确有前作时用；最后一句可以改为正面的具体新增结论，无须自评扩展价值。

## 可选：贡献列表

> The main contributions are as follows:
>
> - We formulate {{PRECISE_PROBLEM}} under {{DISTINGUISHING_CONDITIONS}}, making explicit {{PREVIOUSLY_UNRESOLVED_RELATIONSHIP}}.
> - We develop {{METHOD}}, whose {{KEY_OPERATION}} addresses {{SPECIFIC_OBSTACLE}} through {{MECHANISM}}.
> - We establish {{THEORY_RESULT}} under {{ASSUMPTIONS}} / provide evidence for {{EMPIRICAL_FINDING}} through {{DECISIVE_CONTROL}}.

选取真实贡献，删除不适用条目，不自动把三条当作必须完成的任务。

## 润色：从模块清单改成问题到设计的段落

原稿：

> We propose {{METHOD}} with modules {{A}}, {{B}}, and {{C}}. These modules are novel. They can extract better information and improve the results.

补充材料：每个模块的真实输入输出、所解决的困难和已有证据。

改写：

> The key difficulty is {{OBSTACLE}}. We address it by {{KEY_IDEA}}, implemented through {{CORE_OPERATION}}. {{A}} estimates {{INTERMEDIATE_OBJECT}}, which {{B}} uses to {{NEXT_OPERATION}}; {{C}} then produces {{FINAL_OUTPUT}}. This design connects {{DEPENDENT_STEPS}} so that {{INTENDED_BEHAVIOR}}. Its effect is evaluated by {{CONTROL_REFERENCE}}.

如果没有对照结果，把末句改成具体待补标记，不用“显著改善”代替缺失证据。
