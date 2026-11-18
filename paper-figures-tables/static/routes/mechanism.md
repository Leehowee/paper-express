# 机制分析

把机制主张拆成可观测对象、预期变化和任务后果。内部图像变得更清楚只是观察；机制结论需要能够区分竞争解释的干预或对照。

## 套路 A：分布分离—阈值含义—错误区域

使用 F05 的共同分箱密度与 ECDF。输入每个样本的评分及来源分组，注明 clean/noisy 标签如何得到。共享范围和分箱，密度面积归一；组大小不同不能直接比较计数柱高度。需要分布模型时区分拟合曲线和真实标签，记录拟合方法与样本。

## 套路 B：中间结构—参考结构—任务结果

使用 F06 的固定顺序矩阵。横纵轴分别对应同一组样本，比较初始、更新后和参考关系；若参考来自类别标签则明示。相同量使用同一色标；概率、相似度和注意力不可只因都在 [0,1] 就混为同一量。

结合消融说明改变某模块后，结构指标和任务指标如何变化；有更好的内部重建却没有更好的下游性能时保留该分歧。

## 套路 C：权重分配—受控扰动—下游效果

使用 F12，说明权重的约束和归一化。加入已知噪声组件后，查看权重与任务变化。权重非零、分布平滑或稀疏都不是普遍意义上的“好”；判断依赖主张和对照。

## 套路 D：表示投影—共同样本—定量补充

使用 F13，输入真实降维坐标及样本 ID。记录投影方法、种子、参数和是否联合拟合。独立拟合的投影不能按坐标距离跨图比较。固定样本与类别编码，补充原空间指标或任务测试。示例中的坐标是合成演示，不声称运行过 t-SNE。

通用图注：

> **{{DIAGNOSTIC}} associated with {{MECHANISM}}.** We visualize {{OBJECT}} from {{SAMPLES / LAYER / TIME}} using {{NORMALIZATION / ORDERING}}. {{PANELS}} share {{SCALE / IDS}}. {{INTERVENTION}} changes {{OBSERVATION}}; its relation to task performance is evaluated in {{CONTROL_OR_TABLE}}. The visualization alone does not establish {{UNTESTED_CAUSAL_CLAIM}}.
