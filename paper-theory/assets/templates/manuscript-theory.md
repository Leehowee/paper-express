# 可直接写入 Methods 的理论段落

选取与实际结论相符的套路，填入已完成定义和证据。未证明的结论标为候选，不因模板使用 `establish` 或 `guarantee` 就自动成为定理。中文稿沿用相同逻辑写成自然中文。

## A. 约束与重参数化

> Direct optimization over {{ORIGINAL_SET}} is difficult because {{CONSTRAINT_OBSTACLE}}. We represent {{ORIGINAL_OBJECT}} as {{PARAMETERIZATION}}, where {{PARAMETERS_AND_DOMAINS}}. Proposition {{LABEL}} establishes that this construction preserves {{CONSTRAINTS}}. {{COVERAGE_STATEMENT}}. We therefore optimize {{TRANSFORMED_OBJECTIVE}} over {{PARAMETER_SET}}.

全域覆盖已证明时的衔接：

> Every feasible {{ORIGINAL_OBJECT}} admits this representation, and the objective value is unchanged. Thus, an optimum of the parameterized problem maps to an optimum of the original problem.

仅覆盖受限模型时的衔接：

> The representation covers {{RESTRICTED_CLASS}}. The resulting guarantee concerns this class; extending it to {{FULL_CLASS}} requires {{MISSING_COVERAGE_OR_ERROR_BOUND}}.

## B. 值函数与算法依据

> We absorb the inner optimization into the value function $J({{VARIABLE}})={{VALUE_FUNCTION}}$. Under {{ATTAINMENT_CONDITIONS}}, the inner optimum is attained. For each fixed {{INNER_VARIABLE}}, {{SLICE_PROPERTY}}; Proposition {{CONVEXITY_LABEL}} consequently establishes {{VALUE_PROPERTY}}. When {{DIFFERENTIABILITY_CONDITIONS}} hold, {{GRADIENT_FORMULA_AND_REFERENCE}}. This permits {{ACTUAL_OUTER_UPDATE}} under {{ALGORITHM_CONDITIONS}}.

出现非唯一活跃解而未建立可微性时，替换为：

> At {{DEGENERATE_CONDITION}}, the active solutions may give different derivatives. We therefore use {{JUSTIFIED_DIRECTIONAL_OR_SUBGRADIENT_RESULT}} and restrict the smooth analysis to {{SUPPORTED_REGION}}.

## C. 优化收敛

> Each update solves {{ACTUAL_SUBPROBLEM_OR_APPROXIMATION}} while keeping {{FIXED_VARIABLES}} fixed. The comparison with the previous feasible iterate yields {{ONE_STEP_INEQUALITY}}. Combining the updates gives {{FULL_ITERATION_RELATION}}. Since {{BOUND_OR_SUMMABILITY_CONDITION}}, the sequence of {{PRECISE_CONVERGENT_OBJECT}} {{EXACT_LIMIT_RESULT}}.

若仅建立目标值收敛，用目标值收束；若另有驻点或变量收敛定理，再补其条件与引用。不要自动接上“therefore reaches a global optimum”。

## D. 统计界与目标联系

> We measure generalization through {{DEFINED_RISK}}. The hypothesis class {{CLASS}} includes {{LEARNED_OBJECT}} under {{MEMBERSHIP_CONDITIONS}}. Theorem {{LABEL}} gives {{UNIFORM_OR_POINTWISE_BOUND}} with probability at least {{PROBABILITY}} over {{RANDOMNESS}}. Combining this result with {{PROVEN_OBJECTIVE_RISK_RELATION}} yields {{FINAL_BOUND}}. The analysis applies to {{DATA_AND_PREDICTION_SETTING}}.

## E. 近似与成本

> The implementation replaces {{EXACT_OBJECT}} with {{APPROXIMATION}}. Under {{CONDITIONS}}, the induced objective error is at most {{EPSILON}}, uniformly over {{DOMAIN}}. If the approximate problem is solved to accuracy {{ETA}}, Proposition {{LABEL}} bounds the original objective gap by {{ACTUAL_TRANSFERRED_BOUND}}. Computing the approximation requires {{PREPROCESSING_COST}}, followed by {{ITERATION_COST}} for each of {{ITERATION_COUNT}} iterations.

## Trans：展开完整证明的连接段

> We provide the proof in three steps. Lemma {{FIRST_LABEL}} establishes {{FIRST_PROPERTY}}. Lemma {{SECOND_LABEL}} uses this property to derive {{KEY_RELATION}}. The final step connects {{MATHEMATICAL_RESULT}} to {{METHOD_OPERATION}}, under {{APPLICABILITY_CONDITION}}.

步骤数量按实际修改，后接完整引理与推导。长理论可以独立成节，默认不依赖未启用的附录。

## 会议：命题、关键思想与附录指引

> Under {{ESSENTIAL_ASSUMPTIONS}}, Theorem {{LABEL}} establishes {{EXACT_RESULT}}. The key argument is {{NONSTANDARD_PROOF_STEP}}, which relates {{OBJECT_1}} to {{OBJECT_2}} through {{REASON}}. Appendix {{REAL_SECTION}} gives the complete proof and {{ADDITIONAL_DETAILS}}.

附录尚未创建时保留明确待补标签。理论本身为主要创新时，在正文充分展开决定性步骤。

## 润色示例

原稿：

> The objective decreases and is bounded, so our algorithm converges to the unique global optimum and guarantees better generalization.

已知材料只有一步下降关系与下界时：

> Each iteration satisfies $F(z^{t+1})\leq F(z^t)$, and $F$ is bounded below on the feasible set. Hence, the sequence of objective values converges. This result characterizes the optimization trajectory under the stated update conditions.

修改说明：删除未被材料支持的唯一性、全局最优和泛化结论。若用户确有相应定理，应补入独立证明及其条件。

## 形式化说明，可选

> We formalize {{ENCODED_STATEMENT}} in Lean {{VERSION}} using {{LOCKED_DEPENDENCY}}. The checked entry point is {{THEOREM_NAME}}. The formalization covers {{COVERAGE}}, with {{ASSUMPTIONS_OR_IMPLEMENTATION_LIMIT}}.

仅在有实际记录时使用。工程地址、命令和详细日志可放可复查材料中，正文重点解释数学意义。
