# 效率与性能代价

先确定成本边界，再比较收益。训练、推理、预处理、通信、额外推理模型和参数搜索可以分别报告，但总成本主张应覆盖相应环节。

## 套路 A：性能—成本散点与经验前沿

使用 F11。同一横轴成本越低越好，纵轴效果越高越好；若指标方向不同先明确转换。点代表真实配置，不用曲线连接没有对应配置的系统。经验 Pareto 前沿仅对当前比较集合和统计量成立；均值前沿不证明统计显著占优。

## 套路 B：效果—延迟—内存/通信并列表

使用 T04，记录硬件、软件、批大小、输入尺度、数值精度、warmup、同步、重复次数和计时范围。GPU 计时需要正确同步；吞吐与单样本延迟分开报告。多客户端通信量注明是每轮、累计还是最大单端。

默认保留原始单位。跨数量级时使用明确对数轴；不要用“对数时间之比”代替时间加速比。归一化需给出基准及公式，并提供原始值。

图注：

> Accuracy–cost trade-off under {{MATCHED_PROTOCOL}}. Cost includes {{SCOPE}} and is measured on {{HARDWARE_AND_SOFTWARE}} with {{BATCH/PRECISION/INPUT}}. Points show {{STATISTIC}} from {{RUNS}}. The dashed line links non-dominated tested configurations based on their means, without asserting significance.

若某方法更准但更慢，直接描述权衡。不能只报去掉新增测试模块后的速度来支持完整方法的效率。
