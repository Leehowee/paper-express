# 主结果与通用表格

表格让读者准确比较数值与条件。先确定比较单位，再决定行列。方法多时方法放行；数据集多而方法少时可转置；设置多时先按协议分块。表注应能独立解释数字和标记。

## 套路 A：方法 × 数据集—指标

使用 T01。列按“数据集 → 指标”分层，行按“相同资源/监督的比较组 → 方法”排列。本文方法放在可比组内，额外监督参考另成组。最佳值由方向和分组计算，不手工加粗。

```text
比较组：{{相同划分、监督、输入和资源}}
方法          {{Dataset A: Metric 1↑ / Metric 2↓}}  {{Dataset B: ...}}
{{Baseline}}  {{mean ± uncertainty}}                {{value / missing status}}
{{Proposed}}  {{mean ± uncertainty}}                {{value}}
参考组：{{额外信息或不同协议，单独说明}}
```

## 套路 B：条件分块—同组方法—共同指标

适合噪声率、缺失率、检索方向、任务标准或 shots。复制 T01 的 `groups`，以每个独立条件为块；必要时将检索方向写入 `dataset` 的分层标签。不能跨条件排名后声称某方法处处最佳。显示确有价值的均值；平均所用集合和权重必须定义。

## 套路 C：组件表、参数表、资源表

- T02：组件开关或策略、训练/推理阶段与结果并排；用文字定义 on/off。
- T03：参数值、固定条件和默认值选择依据同列展示；运行失败保留状态。
- T04：效果与成本放在同一行，分别标明方向和单位；备注硬件及测量范围。
- D05 / PPTX 第 5 页：假设与能力对照。采用 Yes / Partial / No / Unknown / Not applicable 的有定义状态，附支持来源；这不是效果排行榜。

## 生成与润色

将原始重复结果填入 CSV，修改 JSON 的行组、方法、指标、方向、精度和图注，运行 `tablekit.py`。生成 LaTeX、CSV、Markdown、SVG/PDF/PNG 及原生 PPTX 的数据矩阵。PPTX 的数字修改后应回写源数据再生成，防止多个版本漂移。

润色时优先删除重复表头、拆分过宽指标、合并有定义的分组与统一小数位。重要的列不能靠缩小字号塞入页面。没有统计检验时不使用显著性星号；“统计不显著”也不等于“结果等效”。

表注套路：

> Results on {{DATASETS}} under {{PROTOCOL}}. Values are {{STATISTIC}} over {{N AND UNIT}}; {{UNCERTAINTY}} denotes {{DEFINITION}}. Higher/lower values are better as indicated. Bold marks {{RANKING_RULE}} within {{COMPARISON_SCOPE}}. {{MISSING_CODES}} denote {{REASONS}}. {{EXTRA_INFORMATION / REPRODUCED_OR_QUOTED_NOTE}}.
