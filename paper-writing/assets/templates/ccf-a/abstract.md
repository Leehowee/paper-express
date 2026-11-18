# CCF-A Abstract：紧凑成段模板

每次选择一套，直接填成一个摘要。只保留最能区分贡献的设计和证据，正文页数较少不意味着必须省略影响结论的条件。

## A. 假设失效—核心变化—结果

> {{TASK}} relies on {{ASSUMPTION}}, which is violated when {{TARGET_CONDITION}}. We study {{PRECISE_PROBLEM}} and propose {{METHOD}}, whose key idea is to {{KEY_IDEA}}. The method {{CORE_OPERATION_AND_PURPOSE}}, allowing {{SUPPORTED_CAPABILITY}}. On {{EVALUATION_SCOPE}}, it {{MAIN_RESULT_WITH_COMPARATOR}}, with {{IMPORTANT_BOUNDARY}}.

## B. 理论问题—命题—意义

> Existing {{ANALYSES_OR_METHODS}} establish {{KNOWN_PROPERTY}} only under {{RESTRICTIVE_CONDITION}}. We examine {{PRECISE_QUESTION}} and derive {{NEW_RESULT}} under {{ESSENTIAL_ASSUMPTIONS}}. This yields {{ALGORITHMIC_OR_CONCEPTUAL_CONSEQUENCE}} through {{KEY_ARGUMENT_OR_OPERATION}}. {{EMPIRICAL_VALIDATION_OR_PROVEN_COROLLARY}} supports {{BOUNDED_CONTRIBUTION}}.

只使用已完成结果；理论未建立时先写问题与方案，命题位置保留待补。

## C. 关键洞见—简单方法—跨设置验证

> {{ESTABLISHED_APPROACH}} is poorly matched to {{TARGET_REQUIREMENT}} because {{SPECIFIC_MISMATCH}}. We introduce {{KEY_PERSPECTIVE}}, which represents {{OBJECT}} as {{NEW_FORMULATION}}. This leads to {{METHOD}}, a {{ACCURATE_METHOD_DESCRIPTION}} that {{CORE_OPERATION}}. Evaluations across {{TESTED_SETTINGS}} show {{RESULT_AND_VARIATION}}, indicating {{SUPPORTED_GENERALITY}}.

“跨设置验证”只涵盖实测范围，不自动写 arbitrary、universal 或 all tasks。

## D. 暂无实验结果的可用草稿

> {{TASK}} becomes challenging when {{CONDITION}} because {{OBSTACLE}}. We propose {{METHOD}} to address this problem through {{KEY_IDEA}}. It {{ACTUAL_DESIGN}}. [待补：决定性比较结果、验证范围和关键边界。]

如果用户要求无占位文字，保留前三句并在正文外说明尚缺结果；不能把实验计划写成结果。

## 润色：压缩并保留贡献差异

原稿：

> With the rapid development of {{FIELD}}, {{TASK}} has attracted much attention. Many methods have achieved good results, but there are still challenges. Our {{METHOD}} contains {{LONG_MODULE_LIST}}. We conduct extensive experiments.

补充材料：具体问题、主要操作和最关键的实际结果。

改写：

> {{TASK}} is limited by {{SPECIFIC_OBSTACLE}} under {{CONDITION}}. {{METHOD}} addresses this obstacle by {{KEY_OPERATION}}, linking {{IMPORTANT_INPUT}} to {{TARGET_OUTPUT}}. On {{SCOPE}}, it {{MEASURED_RESULT_WITH_COMPARATOR}}. {{BOUNDARY_IF_NEEDED}}.

删掉泛背景和次要模块，不能删掉导致结论改变的比较条件。
