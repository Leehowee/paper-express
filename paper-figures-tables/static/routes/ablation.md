# 消融与设计选择

消融检验具体设计的作用。先列出完整方法、需要验证的因素和保持不变的条件，再制作表格或差值图。删去组件后的性能变化不自动等于组件的唯一因果效应。

## 套路 A：组件开关—任务结果—配对变化

用 T02 展示设置，用 F04 展示结果与“完整方法 − 变体”的配对差。每行明确改变的组件、阶段和计算预算。只需要精确数值时使用表；需要突出效应大小与离散程度时使用点区间图。

```text
主张：{{组件 A 通过机制 M 改善结果 Y}}
完整方法：{{A+B+共同训练}}
移除 A：{{替代操作；维度如何保持}}
替代 A：{{复杂度/参数量相当的竞争实现}}
共同条件：{{数据、seed、训练预算、选择协议}}
```

变体必须仍是有效方法。移除损失导致未约束变量、改变输入维度或停止某阶段时说明实际替代。配对差需要逐 seed 对齐，误差从差值计算；不存在配对关系时改成非配对展示并说明。

## 套路 B：目标 × 求解器的交叉对照

当目标函数和优化算法同时改变时，安排“旧目标/新目标 × 旧求解器/新求解器”的可行组合。不能通过只比较两个端点，把全部收益归于任一因素。某组合不适用时解释原因，不伪造四格齐全。

## 套路 C：训练模块 × 测试模块

训练期的鲁棒处理和测试期的修正分别分块；同时报告推理代价。参数变化行与组件移除行区分，避免把参数扫描都称为消融。

图注与正文：

> **Effects of {{COMPONENTS}} under matched {{CONTROLS}}.** The left panel shows {{METRIC}}; the right panel shows paired differences between the full model and each variant. Error bars indicate {{ERROR_OF_PAIRED_DIFFERENCES}}, computed over {{MATCHED_RUNS}}.
>
> Removing {{A}} changes {{METRIC}} by {{DELTA}} under {{CONDITION}}, supporting {{BOUNDED_CLAIM}}. However, {{EXCEPTION / ALTERNATIVE_CONTROL}} indicates that {{LIMIT}}.

保留无提升、反向提升和条件依赖。F04 的示例特意包含优于完整方法的变体，模板不会自动把本文方法排成最优。
