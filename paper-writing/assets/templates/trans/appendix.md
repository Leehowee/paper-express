# Trans 条件附录：正文扩展与补充材料模板

默认不启用附录。未启用时，将下述证明、实现与扩展分析放入正文相应章节；只有采用补充材料且目标允许时，才使用 Appendix 标题和正文指引。

## A. 较长证明放在正文

> We now prove Proposition {{THEOREM_LABEL}}. The proof proceeds by first establishing {{INTERMEDIATE_PROPERTY}} and then using it to derive {{TARGET_RESULT}}. Throughout the argument, {{ESSENTIAL_ASSUMPTIONS}}.
>
> **Step 1: {{FIRST_STEP_TITLE}}.** {{FULL_FIRST_ARGUMENT}}.
>
> **Step 2: {{SECOND_STEP_TITLE}}.** {{FULL_SECOND_ARGUMENT}}.
>
> Combining {{INTERMEDIATE_RESULTS}} yields {{EXACT_CONCLUSION}}. The proof uses {{ASSUMPTION}} at {{SPECIFIC_STEP}}, which explains why the result is restricted to {{APPLICABILITY_SCOPE}}.

每一步需要完整推导，标题不能替代证明；没有分步必要时写成连续证明。

## B. 已启用补充材料：总入口

> This supplementary material provides the complete derivation of {{THEORETICAL_RESULT}}, implementation details for {{METHOD}}, and additional evaluations of {{QUESTION}}. Sections {{PROOF_SECTION}}, {{IMPLEMENTATION_SECTION}}, and {{RESULT_SECTION}} support Sections {{CORRESPONDING_MAIN_SECTIONS}} of the main text, respectively. We retain the notation and evaluation protocol of the main text unless a difference is stated explicitly.

正文引用句：

> The main text establishes {{CENTRAL_RESULT}}; {{SUPPLEMENT_LOCATION}} provides {{SPECIFIC_SUPPORTING_MATERIAL}} for a more detailed examination of {{QUESTION}}.

## C. 完整实现

> We implement {{METHOD}} using {{SOFTWARE_VERSION}}. The input {{DATA}} is processed by {{PREPROCESSING_STEPS}} before {{CORE_OPERATION}}. We initialize {{VARIABLES}} with {{INITIALIZATION}} and use {{OPTIMIZER_OR_SOLVER}}, with {{COMPLETE_PARAMETERS}}. The stopping criterion is {{STOPPING_RULE}}. At test time, {{INFERENCE_DETAILS}}. These settings are shared across {{EXPERIMENTS}}, except for {{EXPLICIT_DIFFERENCES}}.

## D. 扩展分析

> Section {{MAIN_SECTION}} evaluates {{MAIN_CONDITION}}. Here, we extend the analysis to {{ADDITIONAL_CONDITION}} to test {{ADDITIONAL_QUESTION}}. We keep {{CONTROLS}} fixed and change {{VARIED_FACTOR}}. Table/Figure {{SUPPLEMENT_LABEL}} shows {{RESULT}}. This {{SUPPORTS_OR_LIMITS}} the conclusion that {{CLAIM}}, with {{QUALIFICATION}}.

## 润色：将笼统补充指引变成可定位关系

原稿：`More details and results are provided in the supplementary material.`

改写：

> Section {{EXACT_SUPPLEMENT_SECTION}} reports {{SPECIFIC_DETAILS_OR_RESULTS}} under {{ADDITIONAL_CONDITIONS}}, supporting the analysis of {{MAIN_TEXT_CLAIM}} in Section {{MAIN_SECTION}}.

若附录未启用，用正文实际位置替换，不能保留不存在的补充材料引用。理论验证状态和图表核查沿用原有接口。
