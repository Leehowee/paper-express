# 假设、命题与证明的可填充模板

`{{FIELD}}` 从实际研究材料取值。用户要求理论初稿时，填成完整命题与连续证明；材料不足的位置写 `[待补：具体定义或推导]`。不要求为每个方法填满全部类型。

## 1. 理论任务

> 本文研究 {{QUESTION}}。方法通过 {{OPERATION}} 改变 {{OBJECT}}。本节要建立的是：在 {{CONDITIONS}} 下，该操作能够保证 {{EXACT_PROPERTY}}，从而支持 {{CLAIM_ID_AND_MEANING}}。

| 项目 | 填写内容 |
| --- | --- |
| 对象 | 变量、空间、维度、范数、概率空间 |
| 目标 | 原始目标、代理目标、损失或势函数 |
| 算法 | 实际更新、输入信息、初始化、内层精度、停止规则 |
| 比较 | 旧解、最优解、原目标、基线或总体对象 |
| 命题性质 | 可行性、等价性、优化、统计、近似或成本 |
| 覆盖层 | 数学模型、理想更新、有限迭代、实现或最终输出 |

## 2. 假设表

| 编号 | 数学表述 | 作用与使用位置 | 状态或来源 | 在实际方法中的对应 |
| --- | --- | --- | --- | --- |
| A1 | {{DOMAIN_CONDITION}} | 确保 {{WELL_DEFINED_OPERATION}} | {{PROVEN_OR_ASSUMED}} | {{IMPLEMENTATION_CHECK}} |
| A2 | {{STRUCTURAL_CONDITION}} | 支撑 {{LEMMA_OR_STEP}} | {{SOURCE_OR_JUSTIFICATION}} | {{APPLICABILITY}} |
| A3 | {{ALGORITHMIC_CONDITION}} | 控制 {{UPDATE_OR_ERROR}} | {{CODE_OR_PROOF}} | {{ACTUAL_TOLERANCE}} |

可直接写入论文的假设段：

> **Assumption {{LABEL}} ({{SHORT_NAME}}).** {{OBJECTS_AND_DOMAINS}} satisfy {{PRECISE_CONDITION_WITH_QUANTIFIERS}}. This condition is used to {{PROOF_ROLE}}. In the proposed method, it is {{ENFORCED_VERIFIED_OR_MODELED_HOW}}.

“算法保证”“实测支持”和“建模假设”分别填写；经验检查不能被写成任意输入上的保证。假设序号用于跨文件对应，不固定为三条。

## 3. 确定性命题

> **Proposition {{LABEL}} ({{PROPERTY}}).** Let {{OBJECTS_WITH_DOMAINS}}. Assume {{EXPLICIT_ASSUMPTIONS}}. For every {{QUANTIFIED_OBJECT}}, {{EXACT_EQUALITY_INEQUALITY_OR_LOGICAL_STATEMENT}}.

明确结论涉及目标值、参数、子空间还是输出。若比较点为最优解，应先给出其存在条件；也可将结论写成对任意可行比较点成立。

## 4. 算法命题

> **Theorem {{LABEL}} ({{ALGORITHM_PROPERTY}}).** Let $z^0\in{{FEASIBLE_SET}}$ and define $z^{t+1}={{ACTUAL_UPDATE}}$. Under {{ASSUMPTIONS}}, for every $t\geq0$, {{ONE_STEP_CONCLUSION}}. If additionally {{LIMIT_ASSUMPTIONS}}, then {{PRECISE_LIMIT_CONCLUSION}}.

只保留已经证明的第二层结论。有限迭代结果另写 $T$、精度、残差及常数，不能用极限结论覆盖提前停止的输出。

## 5. 统计命题

> **Theorem {{LABEL}} ({{RISK_PROPERTY}}).** Let $S=(Z_1,\ldots,Z_n)$ follow {{SAMPLING_MODEL}}, with $n\geq1$. Let {{LOSS_AND_CLASS}} satisfy {{MEASURABILITY_INTEGRABILITY_AND_SIZE_CONDITIONS}}. For every $\delta\in(0,1)$, with probability at least $1-\delta$ over {{RANDOMNESS}}, the following holds {{UNIFORMLY_OR_FOR_FIXED_OBJECT}}: {{EXPLICIT_BOUND}}.

写清所有常数对样本量、维度、秩和参数的依赖。未知复杂度项可以保留其定义；不能为了给出整洁速率而假定其为常数。

## 6. 完整证明的组织

> **Proof.** We first establish {{INTERMEDIATE_PROPERTY}}. By {{DEFINITION_OR_CHECKED_LEMMA}}, {{FIRST_RELATION}}. Applying {{OPERATION}} under {{REQUIRED_CONDITION}} yields {{SECOND_RELATION}}. Since {{ASSUMPTION_USED_HERE}}, {{CRITICAL_ARGUMENT}}. Combining {{NAMED_RESULTS}} gives {{EXACT_CONCLUSION}}. □

上述是叙述模板，关键推导必须实际展开。逐行记录等式、不等式及所用条件；概率证明另记录事件和失败概率的合并。长证明可分为多个引理，不通过省略号跨越尚未完成的论证。

| 依赖 | 需要证明或引用的内容 | 状态 | 支持谁 |
| --- | --- | --- | --- |
| L1 | {{FEASIBILITY_OR_BOUNDEDNESS}} | {{STATUS}} | {{NEXT_LEMMA}} |
| L2 | {{CENTRAL_RELATION}} | {{STATUS}} | {{MAIN_THEOREM}} |
| T1 | {{FINAL_STATEMENT}} | {{STATUS}} | {{PAPER_CLAIM}} |

## 7. 反例或条件修订

> The proposed statement fails for {{CONSTRUCTION}}. This example satisfies {{ORIGINAL_ASSUMPTIONS}}, but {{COMPUTED_VIOLATION}}. A possible revision is {{REVISED_STATEMENT}} under {{REVISED_ASSUMPTION}}. Its proof {{ACTUAL_STATUS}}.

反例必须满足原命题的全部前提。修订条件尚未确定时，省略修订句并写清待解问题；不能从一个反例直接断定找到了充分或必要条件。原命题和修订命题分别记录状态。若仅说明某个一般推理步骤不成立，明确它不是具体论文完整模型的反例。

## 8. 理论回到方法

> The result justifies {{SPECIFIC_OPERATION_OR_CLAIM}} under {{CONDITIONS}}. The implemented method uses {{IMPLEMENTATION_DETAILS}}; its relationship to the analyzed procedure is {{VERIFIED_MAPPING}}. {{RELEVANT_LIMIT_OR_REMAINING_OBLIGATION}}.

最终保留真正影响解释的限制，删除不适用的导航与占位符。
