# Trans Abstract：可直接填充的段落

选择 A、B 或 C，写成一个摘要，不把三个版本拼接。作者导航不进入论文；`{{FIELD}}` 按真实材料填写，缺失信息保留明确待补标记。缺少结果的处理见 [起草与润色](../../../static/core/drafting-and-polishing.md)。

## A. 问题—限制—设计—证据

> {{TASK}} requires {{REQUIRED_CAPABILITY}} in {{SETTING}}. Existing approaches {{ESTABLISHED_APPROACH}}, but rely on {{ASSUMPTION}}, limiting their ability to {{TARGET_BEHAVIOR}} when {{FAILURE_CONDITION}}. We formulate {{RESEARCH_PROBLEM}} and propose {{METHOD}}, which {{KEY_IDEA}}. Specifically, {{OPERATION_1_AND_PURPOSE}}, while {{OPERATION_2_AND_PURPOSE}}. The resulting {{OBJECTIVE_OR_PROCEDURE}} connects {{PREVIOUSLY_SEPARATED_PARTS}} through {{CONNECTION}}. Experiments on {{EVALUATION_SCOPE}} show {{MAIN_RESULT_WITH_COMPARATOR}}, with {{IMPORTANT_QUALIFICATION}}. These results support {{BOUNDED_CONTRIBUTION}}.

“两个操作”和“连接原先分离的部分”仅在适用时保留。若主要贡献是一项直接设计，用一句准确操作说明代替这些句子。

## B. 数学问题—新结论—算法意义

> {{MATHEMATICAL_OBJECT}} is central to {{TASK}}, yet existing analyses require {{RESTRICTIVE_CONDITION}} or leave {{UNRESOLVED_PROPERTY}} unresolved. We study {{PRECISE_QUESTION}} under {{TARGET_ASSUMPTIONS}}. By {{KEY_REFORMULATION_OR_ARGUMENT}}, we establish {{THEORY_RESULT}}. This result leads to {{ALGORITHM_OR_DESIGN}}, in which {{CRITICAL_OPERATION}}. The analysis applies to {{GUARANTEED_OBJECT}} and requires {{ESSENTIAL_CONDITION}}. Evaluations on {{EVALUATION_SCOPE}} show {{EMPIRICAL_RESULT}}, clarifying {{PRACTICAL_IMPLICATION}}. The work provides {{SUPPORTED_ADVANCE}} within {{BOUNDARY}}.

没有实验的纯理论工作，用已证明的推论、反例或紧性结果替代评估句，不虚构验证。正文中尚未完成的命题不能填入 `establish` 后面。

## C. 共同结构—统一框架—实例与边界

> Existing approaches to {{TASK}} differ in {{VISIBLE_DIFFERENCE}}, although they share {{COMMON_STRUCTURE}}. The relationship between {{APPROACH_FAMILIES}} remains unclear under {{CONDITION}}. We introduce {{FRAMEWORK}}, which expresses {{COMMON_OBJECT}} through {{UNIFYING_FORMULATION}}. Under {{SPECIAL_CASE_CONDITIONS}}, the formulation recovers {{VERIFIED_SPECIAL_CASES}}; changing {{DESIGN_CHOICE}} yields {{NEW_INSTANCE}}. We derive {{AVAILABLE_ANALYSIS}} and evaluate {{IMPLEMENTED_INSTANCES}} on {{EVALUATION_SCOPE}}. The results show {{MAIN_RESULT_AND_VARIATION}}, supporting {{FRAMEWORK_VALUE}} while identifying {{BOUNDARY}}.

未证明精确包含关系时，将 `recovers` 改为与实际依据一致的关系描述；框架类比不能套成等价结论。

## 润色：从评价性语言变成可判断的摘要

原稿：

> {{TASK}} is very important and has received much attention. Existing methods have many limitations. We propose a novel and effective {{METHOD}}. Extensive experiments demonstrate its superiority.

补充材料：具体失效条件、实际操作、主要比较结果。

改写：

> {{TASK}} is limited by {{SPECIFIC_FAILURE}} under {{CONDITION}}. We address this limitation with {{METHOD}}, which {{CONCRETE_OPERATION}}. On {{EVALUATION_SCOPE}}, the method {{MEASURED_RESULT_WITH_COMPARATOR}}. The improvement is concentrated in {{SUPPORTED_SETTING}}, whereas {{IMPORTANT_EXCEPTION}} remains unresolved.

只有原稿、没有补充材料时，可用版本：

> We propose {{METHOD}} for {{TASK}}. [待补：现有方法的具体限制及本文关键操作。] [待补：支持主要结论的比较结果与适用范围。]

## 可替换的证据句

- 整体改善但有例外：`Across {{SCOPE}}, {{METHOD}} achieves {{AGGREGATE_RESULT}}, although {{EXCEPTION}}. The gain is largest when {{CONDITION}}.`
- 效果与成本权衡：`Relative to {{BASELINE}}, {{METHOD}} changes {{METRIC}} by {{ABSOLUTE_OR_RELATIVE_CHANGE}} at a cost of {{RESOURCE_CHANGE}}, under {{MATCHED_PROTOCOL}}.`
- 已有理论结果：`Under {{ASSUMPTIONS}}, we prove {{EXACT_RESULT}} for {{OBJECT}}, without extending the guarantee to {{UNCOVERED_OBJECT}}.` 最后限定只在确实需要澄清时保留。
