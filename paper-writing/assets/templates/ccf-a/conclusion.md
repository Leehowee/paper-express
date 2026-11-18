# CCF-A Conclusion：紧凑收束模板

通常选一段完成问题、答案和边界的收束。独立局限章节已存在时，在结论中保留影响中心判断的最关键条件，避免重复全部限制。

## A. 问题与方法贡献

> We studied {{QUESTION}} under {{SETTING}} and introduced {{METHOD}}, which {{CENTRAL_DESIGN_CHANGE}}. The results on {{TESTED_SCOPE}} support {{MAIN_SUPPORTED_FINDING}} and show {{SUPPORTED_DESIGN_INSIGHT}}. The approach remains limited by {{ESTABLISHED_BOUNDARY}}. A next step is to test {{CONCRETE_EXTENSION_OR_OPEN_QUESTION}}.

只保留有材料支持的句子。没有明确的后续研究方向时删去最后一句；没有边界材料时不凭空生成一种失败。

## B. 理论贡献

> This work establishes {{THEORETICAL_RESULT}} under {{ASSUMPTIONS}}, clarifying {{RELATIONSHIP_OR_LIMIT}}. The result leads to {{ACTUAL_ALGORITHMIC_OR_CONCEPTUAL_CONSEQUENCE}}, with {{EMPIRICAL_SUPPORT_IF_AVAILABLE}}. Extending the analysis to {{UNRESOLVED_SETTING}} remains open because {{SPECIFIC_OBSTACLE}}.

理论结论与实际算法的差异需要保留。没有实验时删除经验支持分句；未证明的扩展写成开放问题。

## C. 现象与见解贡献

> Our analysis identifies {{REPRODUCED_PHENOMENON}} in {{TESTED_SETTING}}. {{DISCRIMINATING_EVIDENCE}} supports {{BOUNDED_EXPLANATION}}, suggesting {{DESIGN_IMPLICATION}}. Whether this relationship holds under {{UNTESTED_CONDITION}} remains to be determined.

最后一句仅用于与贡献直接相关、确实未检验的条件，不把所有可能任务列为未来工作。

## 可选：单独的局限段

> **Limitations.** Our study covers {{ACTUAL_SCOPE}} and relies on {{ASSUMPTION_OR_RESOURCE}}. Under {{OBSERVED_FAILURE_CONDITION}}, {{ACTUAL_FAILURE}}. We have not evaluated {{RELEVANT_UNTESTED_SCOPE}}, so the current evidence supports {{LIMITED_CLAIM}}.

区分真实失败、成立前提和未评估范围。它们可分别成句，不要求三类都存在。

## 润色：从重复贡献清单改成回答研究问题

原稿：

> In this paper, we proposed a novel method with three modules. We conducted extensive experiments. Our method is effective and has great potential. In the future, we will improve it.

补充材料：真正解决的问题、核心操作、已支持结论及具体未解决事项。

改写：

> {{METHOD}} addresses {{PRECISE_QUESTION}} by {{KEY_OPERATION}}. Evidence from {{TESTED_SCOPE}} supports {{SPECIFIC_FINDING}}, with {{ACTUAL_CONDITION_OR_LIMIT}}. Future work will examine {{CONCRETE_UNRESOLVED_QUESTION}}.

没有这些输入时保留 `[待补：已支持的发现]` 等明确位置，不将“effective”改成无依据的强结论。使用规则见 [直接起草与润色](../../../static/core/drafting-and-polishing.md)。
