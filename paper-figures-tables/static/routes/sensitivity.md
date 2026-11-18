# 参数敏感性

敏感性分析描述方法依赖哪些选择、可用区间有多宽，以及极端设置为何失效。图中的默认值应来自既定选择协议，不能查看测试集后再标为事先确定。

## 套路 A：单参数—真实尺度—默认值

用 F07。固定其余参数，横轴使用实际数值或明确的 log 尺度，显示整个相关范围和重复变异，竖线标默认值。不同数据集可叠加或分面；绝对水平差异掩盖趋势时采用分面，不擅自归一化。

含零值时，零通常代表组件关闭，可单列消融；不能把零伪装成极小正数放入对数轴。无序策略使用点或条形，不连接成连续参数曲线。

## 套路 B：双参数—离散网格—稳定区域

用 F08，或 T03 精确列数值。网格色标固定，失败格显示 NA/错误状态；解释网格等距表示的是已测试组合。仅有限网格时不画暗示连续光滑性质的插值曲面。三维表面在遮挡无法消除时改成热图和剖面线。

区分单因素扫描与联合搜索，不把两个分别改变的参数表拼成同一横轴。默认值、稳定区间和边界例外是不同结论。

图注：

> Sensitivity to {{PARAMETER}} on {{SPLIT}}. All other settings are fixed at {{FIXED_VALUES}}. Markers/cells denote tested settings; {{ERROR}} is computed from {{RUNS}}. The default {{VALUE}} was selected using {{SELECTION_PROTOCOL}}. Missing/failed configurations are shown as {{CODE}}.

正文套路：

> Performance varies within {{RANGE}} over {{INTERVAL}}, whereas {{EXTREME}} produces {{FAILURE}}. We therefore use {{DEFAULT}} according to {{PREDEFINED_RULE}}, with {{LIMITATION}}.
