---
name: paper-theory
description: Develop and audit mathematical assumptions, theorem statements, proofs, counterexamples, and Lean 4 formalizations for research methods. Use for 方法理论分析、假设与命题、等价性、值函数、收敛性、泛化界、近似误差、Lean 形式化证明，以及 Methods 的理论调用. Return usable manuscript text and verification artifacts, with explicit coverage of the implemented algorithm. Supports independent use without a full manuscript.
---

# 数学理论与 Lean 形式化

从论文需要解释的关系出发，明确对象、条件和结论，完成推导或构造反例，再将已建立的命题编码为 Lean。理论应回答方法为何成立、在哪些条件下成立，以及结论覆盖实际方法的哪一部分。

独立调用与 Methods 调用采用同一套流程。用户仅提供一个公式、算法或候选命题时，直接处理该对象，不要求先完成整篇论文或 Idea 审查。

## 加载顺序

1. 读取 [基本原则](static/core/stance.md)、[研究流程](static/core/workflow.md) 和 [交付方式](static/core/output.md)。
2. 按 [manifest.yaml](manifest.yaml) 和下表选择当前证明路线，只读取相关文件。一个主张可由数条路线组成，结论须逐层衔接。
3. 建立 [假设与命题契约](assets/templates/theory-contract.md)，完成实际定义、推导和反例检查。
4. 需要形式化时，读取 [Lean 工作方式](static/lean/workflow.md) 与 [语义和依赖审查](static/lean/integrity.md)，使用 [形式化模板](assets/templates/lean-formalization.md) 及附带的 Lean 工程。
5. 需要论文文字时，使用 [可直接起草的理论段落](assets/templates/manuscript-theory.md)。Methods 调用按 [请求与返回协议](interfaces/methods.md) 回传。

## 证明路线

| 路线 | 适用问题 | 主要交付 |
| --- | --- | --- |
| [可行性、等价性与表示](static/routes/well-posedness.md) | 定义是否有效、约束是否可满足、重参数化是否保留问题 | 存在条件、可行性命题、映射与覆盖关系 |
| [值函数与正则性](static/routes/value-functions.md) | 内层优化如何定义外层目标，何时凸、连续、可微 | 极值存在、包络性质、梯度或次梯度条件 |
| [优化与收敛](static/routes/optimization.md) | 一步更新、交替优化、近似求解、停止条件 | 下降关系、目标值或变量收敛的准确层级 |
| [统计误差与泛化](static/routes/statistical-bounds.md) | 训练目标如何联系样本外风险 | 函数类、概率事件、一致界及算法代入条件 |
| [近似、稳定性与复杂度](static/routes/approximation.md) | 松弛、低秩、有限精度、效率改动的影响 | 误差传递、适用范围和完整成本 |

## 默认行为

- 用户要求理论初稿：交付填好的假设、命题和推导；关键步骤未完成时明确保留缺口。
- 用户要求证明：先检查命题是否成立。反例成立时给出反例、失效条件和可证明的修订命题。
- 用户要求 Lean：实际生成源码并尝试在可用环境检查，记录版本、命令和结果。没有运行环境时继续完成数学部分与源码，形式化状态如实保留为未运行。
- 用户要求润色：保留量词、常数、概率、条件和证明强度，直接返回修改后的命题与正文。

现成工程提供可复用的引理和完整示例，不代表任何新方法已被证明。只有应用条件得到证明且语义对应完成，才把库中引理的保证转移到论文算法。

## 参考与验证

来源分析按需读取：[阅读范围](references/source-index.md)、[三篇独作的理论分析](references/solo-paper-theory.md)、[其他样本](references/other-paper-theory.md)。通用规则与具体作者、模型和数值分开保存。

完整使用示例见 [从 Methods 到数学与 Lean](references/worked-example.md)。工程的实际检查状态见 [验证记录](references/validation.md)，工具依据见 [Lean 官方资料](references/lean-sources.md)。
