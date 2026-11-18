# 从材料到正文：完整填充示例

本例是为演示模板使用而构造的简单数学设定，不是用户研究、论文贡献或已完成实验。它只展示如何把给定定义写成 Methods，以及如何润色同一内容。没有性能数据、创新性证据或形式化验证记录，因此不生成这些结论。

## 输入材料

- 训练数据为 $D=\{(x_i,y_i)\}_{i=1}^n$，其中 $n\geq 1$。
- 每个样本有一个外部提供的固定可靠性分数 $r_i\in[0,1]$；不在本方法中估计或更新。
- 模型为 $f_\theta$，逐样本损失为 $\ell(f_\theta(x_i),y_i)$。
- 当 $S=\sum_i r_i>0$ 时，权重 $w_i=r_i/S$；当 $S=0$ 时，$w_i=1/n$。
- 训练目标 $L(\theta)=\sum_i w_i\ell(f_\theta(x_i),y_i)$，采用随机梯度下降更新 $\theta$。具体批采样方式、学习率及停止条件尚未提供。
- 推理仅使用 $f_\theta(x)$，不需要可靠性分数。
- 未提供实验结果、可靠性估计的正确性假设、相关工作或收敛证明。

## 任务 A：直接写 Trans Methods 初稿

采用 [期刊 Methods](../assets/templates/trans/methods.md) 的问题定义—目标—求解套路，保留足够说明。

### Reliability-weighted training

Let $D=\{(x_i,y_i)\}_{i=1}^n$ be a training set with $n\geq 1$, and let $r_i\in[0,1]$ denote a fixed, externally supplied reliability score for sample $i$. We use these scores to determine the relative contributions of the training samples to the objective. The scores are treated as inputs and are not updated during optimization.

Define $S=\sum_{j=1}^n r_j$. The weight assigned to each sample is

\[
w_i=\begin{cases}
r_i/S, & S>0,\\
1/n, & S=0.
\end{cases}
\]

For a positive total score, normalization assigns a larger weight to a sample with a larger supplied score. When all scores are zero, the uniform fallback keeps the objective defined. In both cases, the weights are nonnegative and sum to one.

We train $f_\theta$ by minimizing

\[
L(\theta)=\sum_{i=1}^n w_i\ell(f_\theta(x_i),y_i).
\]

The parameters $\theta$ are updated using stochastic gradient descent, while the weights remain fixed. [待补：与加权目标一致的批采样方式、损失缩放、学习率和停止条件。] At inference, predictions are computed as $f_\theta(x)$ without reliability scores.

这里的非负性、归一化及退化情形可以由给定定义直接检查；没有由此推断预测更准、可靠性分数正确或算法收敛。

## 任务 B：写成会议正文的紧凑版本

采用 [会议 Methods](../assets/templates/ccf-a/methods.md) 的核心定义—操作—训练与推理套路。正文保留权重来源及全零情形，不引用尚不存在的附录。

### Reliability-weighted objective

Given $D=\{(x_i,y_i)\}_{i=1}^n$ and fixed external scores $r_i\in[0,1]$, we train $f_\theta$ with $L(\theta)=\sum_i w_i\ell(f_\theta(x_i),y_i)$. We set $w_i=r_i/\sum_j r_j$ when the total score is positive and use $w_i=1/n$ otherwise. This assigns relative training weights according to the supplied scores, with a uniform fallback when all scores are zero. We optimize $\theta$ using stochastic gradient descent and hold $w_i$ fixed. [待补：批采样与损失缩放、学习率和停止条件。] Inference uses only $f_\theta(x)$.

## 任务 C：润色已有段落

原稿：

> Our method uses reliability. We give reliable samples more weight. The weights are normalized. If all scores are zero, all samples have the same weight. Then we train the network using SGD. Testing does not need scores.

已知补充材料仅为上述输入，不增加实验、方法新颖性或理论保证。

润色稿：

> We weight each training sample using its fixed, externally supplied reliability score. For a positive total score, the weights are normalized to sum to one; when all scores are zero, each sample receives weight $1/n$. We then optimize the weighted loss using stochastic gradient descent, keeping the weights fixed. At inference, the model makes predictions without access to reliability scores.

主要修改是明确分数来源、权重更新状态和训练与推理的区别。“分数较高”不等于样本的真实可靠性已得到验证，因此没有写成“该设计确保高质量样本主导训练”。

## 缺少实验时如何处理摘要中的结果句

请求若进一步要求摘要，可以先写问题、定义和操作，再保留 `[待补：在何种数据和比较协议下，哪些结果支持该设计]`。不得补出“优于现有方法”“显著提升鲁棒性”或任意数值，也不需要把已经明确的 Methods 全部改成未来时态。
