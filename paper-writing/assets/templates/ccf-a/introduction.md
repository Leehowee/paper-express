# CCF-A Introduction：可直接写成正文的套路

选一套主线，再按需要加入贡献句或诊断图句。模板中的功能说明不进入正文；最近文献及证据引用按原材料填写。

## A. 现有假设—新问题—直接方案不足

**段 1。**

> {{TASK}} aims to {{OBJECTIVE}}. Existing methods achieve {{KNOWN_CAPABILITY}} by {{COMMON_APPROACH}} {{CITATIONS}}, but assume {{ASSUMPTION}}. In {{TARGET_SETTING}}, {{OBSERVED_OR_DOCUMENTED_FACT}} violates this assumption and causes {{SPECIFIC_CONSEQUENCE}}.

**段 2。**

> We study {{PROBLEM_NAME}}, defined as {{PRECISE_PROBLEM_DEFINITION}}. This setting differs from {{NEAREST_PROBLEM}} in {{DISTINGUISHING_INFORMATION_OR_CONSTRAINT}}. A straightforward solution is to {{DIRECT_APPROACH}}; however, {{TECHNICAL_OBSTACLE}} prevents it from {{TARGET_BEHAVIOR}}. Existing {{CLOSEST_ROUTE}} addresses {{SOLVED_PART}} but leaves {{REMAINING_PART}} unresolved {{CITATIONS}}.

**段 3。**

> Our key idea is to {{KEY_IDEA}}. We implement this idea in {{METHOD}}, which {{CORE_OPERATION}}. {{COMPONENT_1}} handles {{CHALLENGE_1}} by {{ACTION_1}}, while {{COMPONENT_2}} handles {{CHALLENGE_2}} through {{ACTION_2}}. The resulting procedure {{SUPPORTED_OR_INTENDED_BEHAVIOR}}, using only {{AVAILABLE_INFORMATION}}.

**段 4。**

> We evaluate {{METHOD}} on {{EVALUATION_SCOPE}} and isolate {{KEY_DESIGN}} using {{DECISIVE_CONTROL}}. The results show {{MAIN_FINDING}}, while {{BOUNDARY}} limits {{BROADER_INTERPRETATION}}. The main contribution is {{PRECISE_ADVANCE}}, supported by {{EVIDENCE_SUMMARY}}.

“新问题名”和两个模块均非必需；任务已有名称时沿用，不为了模板制造术语。

## B. 数学障碍—关键结果—实际含义

**段 1。**

> {{MATHEMATICAL_OBJECT}} governs {{TASK_BEHAVIOR}} in {{SETTING}}. Existing results characterize {{KNOWN_PROPERTY}} under {{ASSUMPTIONS}} {{CITATIONS}}. They do not determine {{OPEN_QUESTION}} when {{TARGET_CONDITION}}, leaving {{PRACTICAL_OR_THEORETICAL_CONSEQUENCE}} unclear.

**段 2。**

> The difficulty is {{SPECIFIC_OBSTACLE}}. Applying {{STANDARD_TECHNIQUE}} requires {{MISSING_CONDITION}}, while {{DIRECT_ALTERNATIVE}} incurs {{KNOWN_COST_OR_LIMITATION}}. We resolve {{RESOLVED_PART}} by {{KEY_ARGUMENT_OR_REFORMULATION}}. This gives {{EXACT_RESULT}} under {{ESSENTIAL_ASSUMPTIONS}}.

**段 3。**

> The result leads to {{ALGORITHM_OR_NEW_UNDERSTANDING}}. Its implementation {{CRITICAL_OPERATION}}, and {{THEORETICAL_OR_EMPIRICAL_EVIDENCE}} examines {{RELEVANT_PROPERTY}}. The contribution therefore consists of {{THEORETICAL_ADVANCE}} and {{SUPPORTED_CONSEQUENCE}}, with scope restricted to {{BOUNDARY}}.

## C. 统一观点—新实例—覆盖范围

**段 1。**

> Approaches to {{TASK}} differ in {{DESIGN_DIMENSIONS}} {{CITATIONS}}. Despite these differences, they share {{COMMON_STRUCTURE}}. A common description of {{RELATIONSHIP}} would clarify {{SCIENTIFIC_OR_DESIGN_QUESTION}} and help determine {{DECISION}}.

**段 2。**

> We formulate {{FRAMEWORK}} around {{UNIFYING_OBJECT}}. Under {{CONDITIONS}}, it recovers {{VERIFIED_SPECIAL_CASES}}; selecting {{NEW_CHOICE}} yields {{NEW_INSTANCE}}. The key change is {{SUBSTANTIVE_DIFFERENCE}}, which addresses {{SPECIFIC_LIMITATION}}.

**段 3。**

> We analyze {{FORMAL_RELATIONSHIP}} and evaluate {{IMPLEMENTED_INSTANCES}} using {{MATCHED_PROTOCOL}}. {{MAIN_FINDING}}. These results establish {{SUPPORTED_VALUE}} across {{COVERED_SCOPE}}, while {{UNCOVERED_CASE}} remains open.

## D. 反常观察—竞争解释—区分性检验

**段 1。**

> Under {{CONTROLLED_SETTING}}, we observe {{PHENOMENON}} ({{EVIDENCE_REFERENCE}}). This differs from the expectation that {{EXPECTED_BEHAVIOR}}, motivating the question of {{RESEARCH_QUESTION}}. The observation concerns {{SCOPE}} and does not by itself identify its cause.

**段 2。**

> One explanation is {{HYPOTHESIS}}, whereas {{ALTERNATIVE_EXPLANATION}} could produce a similar pattern. We distinguish these explanations by {{DISCRIMINATING_TEST}}. The test changes {{INTERVENTION}} while holding {{CONTROLS}} fixed, so the two explanations predict {{DIFFERENT_PREDICTIONS}}.

**段 3。**

> The evidence {{SUPPORTED_OUTCOME_OF_TEST}}. Guided by this finding, we develop {{METHOD_OR_ANALYSIS}} to {{PURPOSE}}. {{VALIDATION_SUMMARY}}. The resulting conclusion is {{BOUNDED_MECHANISTIC_OR_EMPIRICAL_CLAIM}}.

没有完成区分性检验时，将最后一段保留待补或写为设计说明，不默认假说被支持。

## 可选：贡献句块

> Our contributions are: (i) {{PROBLEM_OR_INSIGHT_ADVANCE}}; (ii) {{METHOD_OR_THEORY_ADVANCE}}; and (iii) {{DISTINCT_EVIDENCE_CONTRIBUTION_IF_ANY}}.

只列真实新增内容，普通性能验证无需强行独立成一条。使用此块时替换原有贡献总结，避免重复。

## 可选：用动机图承接问题

> Figure {{MOTIVATION_FIGURE}} illustrates {{SPECIFIC_DIFFERENCE_OR_OBSERVATION}} under {{CONDITION}}. The relevant distinction is {{DISTINCTION}}, which determines {{METHOD_REQUIREMENT}}.

概念示意填 `illustrates`，实测证据可以用 `shows` 并写明测量条件。不要把示意图作为普遍性能结论。

## 润色：合并重复背景，保留问题边界

原稿：

> {{FIELD}} has developed rapidly. {{TASK}} is important in many applications. There are many methods for {{TASK}}. These methods are not good in complex real-world scenarios. We propose {{METHOD}} to solve this problem.

补充材料：失败条件、具体后果和核心操作。

改写：

> Existing methods for {{TASK}} rely on {{ASSUMPTION}} {{CITATIONS}}. When {{CONDITION}}, this assumption fails and {{CONSEQUENCE}}. We address the resulting {{PRECISE_PROBLEM}} with {{METHOD}}, which {{KEY_OPERATION}}. Its contribution is evaluated through {{DECISIVE_COMPARISON}} under {{SCOPE}}.

原稿没有具体问题时保留待补位置，不能把“复杂现实场景”直接扩写为未经验证的噪声、缺失或分布变化。
