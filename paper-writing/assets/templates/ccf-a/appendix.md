# CCF-A Appendix：完整支持材料的正文模板

根据当前投稿规则和真实材料选择小节。正文与附录共用符号、命题和实验设置；模板中的节号在实际内容建立后绑定。使用规则见 [直接起草与润色](../../../static/core/drafting-and-polishing.md)。

## 总引导：说明内容与正文对应关系

> This appendix provides the supporting material for {{MAIN_TEXT_SCOPE}}. Section {{PROOF_SECTION}} proves {{THEOREM_LABELS}}; Section {{IMPLEMENTATION_SECTION}} specifies {{IMPLEMENTATION_DETAILS}}; and Section {{ADDITIONAL_RESULTS_SECTION}} extends the evaluation to {{ADDITIONAL_CONDITIONS}}. We use the notation and evaluation protocol of the main text unless explicitly stated otherwise.

只列实际存在的小节。短附录可以直接从内容开始，无需强制总引导。

正文中的配对引用：

> Appendix {{APPENDIX_SECTION}} provides {{SPECIFIC_SUPPORTING_CONTENT}} for {{CLAIM_OR_PROCEDURE}}.

## A. 完整证明

> **Restatement of {{THEOREM_LABEL}}.** {{EXACT_STATEMENT_WITH_ASSUMPTIONS}}.
>
> **Proof.** Let {{OBJECTS_AND_DOMAINS}}. By {{ASSUMPTION_OR_VERIFIED_RESULT}},
>
> \[
> {{FIRST_RELATION}}
> \]
>
> Applying {{JUSTIFIED_OPERATION}} yields {{INTERMEDIATE_RESULT}}. The key step is {{NONSTANDARD_STEP}}, which follows from {{COMPLETE_JUSTIFICATION}}. Therefore,
>
> \[
> {{FINAL_RELATION}}
> \]
>
> This establishes {{PRECISE_CONCLUSION}} under {{RELEVANT_CONDITIONS}}. □

这是一套证明叙述结构，不能替代实际推导。证明可以分成引理、分情况讨论或归纳，不得用“follows directly”省略核心步骤。若推导增加条件，先同步正文命题。按 [理论接口](../../../interfaces/theory.md) 核查具体命题及状态。

需要交代与实际算法的关系时：

> The result applies to {{MATHEMATICAL_OBJECT}} under {{ASSUMPTIONS}}. The implementation in Algorithm {{ALGORITHM_LABEL}} uses {{ACTUAL_APPROXIMATION_OR_DIFFERENCE}}. Consequently, {{EXACT_SUPPORTED_RELATION_TO_IMPLEMENTATION}}.

## B. 完整算法与实现

> **Algorithm.** The procedure takes {{INPUTS}}, initializes {{VARIABLES}} using {{INITIALIZATION}}, and repeats {{UPDATE_SEQUENCE}} until {{STOPPING_RULE}}. Within each iteration, {{IMPORTANT_SUBROUTINE_AND_APPROXIMATION}}. The final output is {{OUTPUT_RULE}}. Algorithm {{LABEL}} specifies the complete order of operations, including {{NONSTANDARD_BRANCH_OR_EDGE_CASE}}.

> **Implementation.** We implement {{METHOD}} using {{ACTUAL_SOFTWARE_AND_VERSIONS}}. {{ARCHITECTURE_OR_DATA_STRUCTURE}} is configured with {{CONFIGURATION}}. Training uses {{OPTIMIZER_AND_SCHEDULE}}, with {{RANDOMNESS_HANDLING}}. At inference, {{INFERENCE_PROCEDURE_AND_AVAILABLE_INFORMATION}}. The experiments run on {{HARDWARE}}, and {{MEASUREMENT_SCOPE}} is included in the reported computational cost.

若使用外部模型或 API，加入真实的模型版本、提示、采样及响应处理；上述字段不暗示每种方法都有训练阶段或神经网络结构。

## C. 数据与参数选择

> **Data protocol.** We use {{DATA_VERSION_OR_SOURCE}} with {{SPLIT_DEFINITION}}. Preprocessing consists of {{ORDERED_OPERATIONS}}. {{DATA_DEPENDENT_PREPROCESSING}} is fitted on {{PERMITTED_PARTITION}} and applied to {{OTHER_PARTITIONS}}. {{EXCLUSIONS_AND_SELECTION_CRITERIA}} determine the final evaluation set.

> **Model selection.** We search {{PARAMETER_SPACE}} using {{SELECTION_DATA_AND_METRIC}} and allocate {{SEARCH_BUDGET}} to {{METHODS_COVERED}}. The selected configuration is {{CONFIGURATION_LOCATION}}. {{PROTOCOL_DIFFERENCES}}. Test results are used for {{ACTUAL_ROLE_OF_TEST_RESULTS}}.

准确陈述测试数据用途；不能因为规范模板通常要求独立测试，就将已有测试集调参改写为没有发生过。

## D. 扩展实验

> **{{ADDITIONAL_QUESTION}}.** Section {{MAIN_SECTION}} establishes {{MAIN_TEXT_FINDING}} under {{ORIGINAL_CONDITION}}. Here, we extend the evaluation to {{ADDED_CONDITION}} while retaining {{SHARED_PROTOCOL}}. We change {{ACTUAL_DIFFERENCES}} and report {{METRICS_AND_AGGREGATION}} in {{SUPPLEMENTARY_FIGURE_OR_TABLE}}. The results show {{VERIFIED_RESULT}}, which {{SUPPORTS_OR_LIMITS}} the conclusion that {{UPDATED_CLAIM}}.

需要补充失败或反例时：

> The conclusion does not extend to {{OBSERVED_FAILURE_SETTING}}: {{ACTUAL_RESULT}}. {{SUPPORTING_ANALYSIS}} suggests {{CAUTIOUS_EXPLANATION}}. The main text therefore limits {{CLAIM}} to {{SUPPORTED_SCOPE}}.

扩展结果改变中心结论时，实际回写正文，不只在附录声明应该修改。若只是未检验范围，不能用该失败模板。

## E. 完整扫描与案例

> **Parameter sweep.** We vary {{PARAMETER}} over {{FULL_RANGE}} with {{OTHER_SETTINGS}} fixed. Each configuration is evaluated using {{REPEAT_AND_AGGREGATION_PROTOCOL}}. {{SUPPLEMENTARY_LOCATION}} reports the complete results, including {{OBSERVED_UNFAVORABLE_REGION}}. The trend {{PRECISE_INTERPRETATION}} within the examined range.

> **Additional cases.** We select cases by {{SELECTION_RULE}} from {{EVALUATION_POOL}} and display {{SHOWN_VARIABLES}}. In {{CASE_LABEL}}, {{OBSERVATION}}; in {{CONTRASTING_CASE}}, {{CONTRASTING_OBSERVATION}}. These examples illustrate {{LOCAL_BEHAVIOR}}. The aggregate evaluation of {{RELATED_CLAIM}} appears in {{QUANTITATIVE_RESULT_LOCATION}}.

删除无材料支持的分句。图注与作图请求按 [图表接口](../../../interfaces/figures-tables.md) 传递，不将精选案例写成总体统计。

## 可选：实际完成的形式化记录

> **Formal verification.** We formalize {{ENCODED_STATEMENT}} in {{LEAN_VERSION}} using {{DEPENDENCY_VERSIONS}}. The artifact at {{ARTIFACT_LOCATION}} was checked with {{ACTUAL_COMMAND}}, producing {{ACTUAL_VERIFICATION_STATUS}}. The correspondence with {{PAPER_STATEMENT}} is {{SEMANTIC_ALIGNMENT_RESULT}}, with {{DISCLOSED_ASSUMPTIONS_AND_LIMITS}}.

仅在已有可核查记录时使用此段。未运行、存在占位证明或语义映射未审查时，按真实状态描述；不能将“工程能编译”自动填成“论文方法已证明正确”。

## 润色：将无定位的补充信息改成可复核段落

原稿：

> More experiments are presented here. We use similar settings and get similar results. These results further prove the effectiveness of our method.

补充材料：扩展的具体条件、协议差异、结果及其对应的正文判断。

改写：

> We extend the experiment in Section {{MAIN_SECTION}} to {{NEW_CONDITION}}, retaining {{SHARED_SETTINGS}} and changing {{EXACT_DIFFERENCE}}. {{RESULT_LOCATION}} shows {{VERIFIED_FINDING}}. This supports {{BOUNDED_CLAIM}} under {{EXPANDED_SCOPE}}.

未提供结果时改写已知设置，并保留 `[待补：扩展结果及其对主张的影响]`。
