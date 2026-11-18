# 完整示例：更新何时使目标不增

本例是人为构造的标量二次问题，用来展示从请求、数学证明、Lean 到 Methods 文字的完整路径。没有实验数据，也不声称复现来源论文或构成新的研究贡献。

## 1. 两种入口

独立调用：

> 使用 paper-theory，分析实数更新 `x_next=(1-η)x+ηa` 在什么步长范围内使 `f(x)=(x-a)²` 不增。给出假设、命题、证明、Lean 源码和可用的正文。

Methods 调用：

```yaml
request_id: T-demo
caller: methods
claim_ids: [C-descent]
research_question: "所给更新是否使同一个目标逐步不增？"
purpose: "确定步长条件并约束 Methods 的理论表述"
objects_and_notation:
  - "a, x0, eta 为实数，f(x)=(x-a)^2"
algorithm_version:
  objective: "f(x)=(x-a)^2"
  update: "x[t+1]=(1-eta)*x[t]+eta*a"
  initialization: "任意实数 x0"
  stopping_rule: "任意有限步数；定理覆盖每个自然数步"
  source_or_revision: "本例 assets/lean-project/PaperTheory/Example.lean"
candidate_statement: "确定 eta 的条件，使每一步目标不增"
assumptions: ["精确实数运算"]
implementation_gap: ["尚未分析浮点计算"]
requested_analysis: [assumption_audit, proof_or_counterexample, lean_formalization, draft]
placement:
  route: trans
  statement: methods
  proof: main_text
```

## 2. 假设与命题

**A1（对象与运算）。** `a,x0,η∈ℝ`，采用精确实数更新。这里的步长是已写出的更新系数；若改成对 f 的梯度下降，需注意 `f'(x)=2(x-a)` 带来的步长换算。

**A2（步长）。** `0≤η≤2`。

**命题。** 对任意 `t∈ℕ`，若 `x[t+1]=(1-η)x[t]+ηa`，则 `f(x[t+1])≤f(x[t])`。

**证明。** 更新给出 `x[t+1]-a=(1-η)(x[t]-a)`，因此

`f(x[t+1])=(1-η)² f(x[t])`。

由 A2 得 `(1-η)²≤1`，而平方目标非负，故命题成立。论证对每个实数 x 都成立，将其代入递归轨迹即可得到所有步的结论。

**条件检查。** 如果要求该性质对所有初值成立，取 `x≠a` 可知必须有 `(1-η)²≤1`，即 `0≤η≤2`。这段必要性为解析补充，当前 Lean 入口仅证明充分性。

**结论边界。** 在 η=2 且 `x0≠a` 时，轨迹在 a 两侧反射，故一步不增不能直接改写为变量收敛。本例也没有浮点误差保证或任何测试性能保证。

## 3. Lean 对应

| 数学内容 | 真实源码对象 |
| --- | --- |
| `f(x)=(x-a)²` | `PaperTheory.quadratic` |
| 精确更新 | `PaperTheory.quadraticStep` |
| 初值与递归轨迹 | `PaperTheory.run` |
| 一步不增 | `PaperTheory.quadratic_step_descent` |
| 每步不增 | `PaperTheory.quadratic_run_descent` |

证明见 [Example.lean](../assets/lean-project/PaperTheory/Example.lean)，运行定义见 [Core.lean](../assets/lean-project/PaperTheory/Core.lean)。形式化包含真实目标、更新和代数推导；没有把一步下降直接列为这个实例的假设。构建及公理依赖的实际状态见 [验证记录](validation.md)。

这与通用 `run_descent` 有区别：后者接受任意目标和更新，将“当前更新的一步下降”列为应用条件；它本身不能替所有新算法完成该条件。

## 4. 可直接使用的正文

> We analyze the update in exact real arithmetic. Let f(x) = (x − a)² and xₜ₊₁ = (1 − η)xₜ + ηa, where a is fixed and 0 ≤ η ≤ 2. The following proposition establishes that the update does not increase this objective.
>
> **Proposition.** For every initialization x₀ ∈ ℝ and every t ≥ 0, f(xₜ₊₁) ≤ f(xₜ).
>
> **Proof.** The update gives xₜ₊₁ − a = (1 − η)(xₜ − a), and hence f(xₜ₊₁) = (1 − η)²f(xₜ). Since 0 ≤ η ≤ 2 implies (1 − η)² ≤ 1 and f(xₜ) ≥ 0, the desired inequality follows.
>
> This result guarantees objective descent for the specified update. It does not by itself establish convergence of the iterates; at η = 2, nonstationary iterates alternate around a. The analysis concerns exact real arithmetic and does not quantify floating-point error.

会议版本可以保留同一命题并压缩解释；证明只有三行，没有为了展示附录模板而强行移走。长证明确需放入附录时，正文保留全部必要条件和真实附录引用。

## 5. 回传与接收

- `mathematical_status: proved` 对应上面的一步与逐步不增命题。
- `lean_status` 从真实验证记录填写；不要仅复制示例中的预期值。
- `semantic_mapping` 对本例的标量实数目标与更新成立；不覆盖另一种算法、浮点实现或概率风险。
- `application_obligations` 对本例只需确认实际使用的系数处于给定范围，且声明的是该精确更新。
- `unsupported_extensions` 包括仅凭当前命题宣称变量收敛、全局学习保证或实验性能提升。

Methods 接收后直接使用上述命题与正文。若论文的实际更新不同，应重新定义并证明；不能保留示例的通过状态而仅替换方法名称。
