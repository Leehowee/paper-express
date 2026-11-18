# 收敛与训练过程

把优化行为和任务效果分开表示，再分析它们的联系。目标下降不保证泛化提升；有限次数的曲线稳定不证明所有初始化都达到全局最优。

## 套路：共同时间轴—目标/残差—任务指标

使用 F10 的并排面板或上下对齐面板。左侧目标值、残差或约束违反；右侧训练/验证/测试指标。轴标题说明最大化还是最小化、归一化还是原始值。不同量级不强制共享纵轴，不用双轴人为制造趋势吻合。

Warmup、目标切换、冻结和优化阶段用垂线与名称标明；跨阶段目标定义改变时不把两段数值当作同一个函数。只用于诊断、未参与优化的损失也要注明。

多初始化可画细轨迹、分位带及最终值分布；统计带需要实际轨迹。不同长度运行不补成虚构终点；迭代成本不同的算法额外给时间轴比较。

图注：

> Optimization trajectories over {{INDEPENDENT_INITIALIZATIONS}}. (a) {{OBJECTIVE / RESIDUAL}}; (b) {{TASK_METRIC}} evaluated on {{SPLIT}} at the same checkpoints. The vertical line marks {{PHASE_CHANGE}}. {{UNCERTAINTY}} reflects {{UNIT}}. These curves characterize empirical behavior; the theoretical guarantee and its conditions are stated in {{THEOREM}}.

当 Methods 需要收敛证明时，通过理论模块检查命题、假设和实际算法的一致性。图表只报告真实过程，不能补写未经验证的全局保证。
