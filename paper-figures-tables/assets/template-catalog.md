# 图表模板目录

先按要回答的问题选模板，再换入数据或方法内容。编号是本库的稳定 ID，不是论文编号。统计图及表格均附合成数据；PPTX 中的数值与相应 CSV 同源，示意页含待填内容。所有示例必须替换后才能用于实证结论。

## 统计图：12 个可运行实例

每个配置调用同一个 [figurekit.py](../scripts/figurekit.py)，相应 CSV 位于 `examples/data/`。已生成 SVG/PDF/PNG；下表链接配置、矢量源和预览。SVG 可以改文字与图形，改数据优先重跑代码。

| ID 与用途 | 直接填充 | 矢量 / 预览 | 选用条件与关键字段 |
| --- | --- | --- | --- |
| F01 引言受控观察 | [配置](examples/configs/F01-motivation.json) | [SVG](gallery/F01-motivation.svg) · [PNG](gallery/F01-motivation.png) | 预算效应/退化；panel、series、真实 x、独立 run |
| F04 消融与配对差 | [配置](examples/configs/F04-ablation.json) | [SVG](gallery/F04-ablation.svg) · [PNG](gallery/F04-ablation.png) | reference、逐种子变体、差值单位；保留负差 |
| F05 分布与 ECDF | [配置](examples/configs/F05-distribution.json) | [SVG](gallery/F05-distribution.svg) · [PNG](gallery/F05-distribution.png) | 干净/噪声等分组；sample_id、score、共同 bins |
| F06 共同索引矩阵 | [配置](examples/configs/F06-alignment.json) | [SVG](gallery/F06-alignment.svg) · [PNG](gallery/F06-alignment.png) | 同样本顺序、同数量含义及色标，参考矩阵来源 |
| F07 一维参数 | [配置](examples/configs/F07-sensitivity-1d.json) | [SVG](gallery/F07-sensitivity-1d.svg) · [PNG](gallery/F07-sensitivity-1d.png) | 实际数值/对数刻度、默认值及选择协议 |
| F08 联合参数网格 | [配置](examples/configs/F08-sensitivity-2d.json) | [SVG](gallery/F08-sensitivity-2d.svg) · [PNG](gallery/F08-sensitivity-2d.png) | 每个已测组合及明确失败；离散网格不插值 |
| F09 条件稳健性 | [配置](examples/configs/F09-robustness.json) | [SVG](gallery/F09-robustness.svg) · [PNG](gallery/F09-robustness.png) | 缺失/噪声/规模；共同模式或预算、完整范围 |
| F10 优化与任务过程 | [配置](examples/configs/F10-convergence.json) | [SVG](gallery/F10-convergence.svg) · [PNG](gallery/F10-convergence.png) | 目标与效果分面，初始化、迭代、阶段位置 |
| F11 质量与成本 | [配置](examples/configs/F11-efficiency.json) | [SVG](gallery/F11-efficiency.svg) · [PNG](gallery/F11-efficiency.png) | score 越大越好，cost 越小越好；硬件与测量范围 |
| F12 内部权重 | [配置](examples/configs/F12-weights.json) | [SVG](gallery/F12-weights.svg) · [PNG](gallery/F12-weights.png) | component、weight、归一化；单向量无误差推造 |
| F13 表示投影 | [配置](examples/configs/F13-embedding.json) | [SVG](gallery/F13-embedding.svg) · [PNG](gallery/F13-embedding.png) | 同一 sample_id；已计算坐标、类别、投影协议 |
| F14 图像案例 | [配置](examples/configs/F14-cases.json) | [SVG](gallery/F14-cases.svg) · [PNG](gallery/F14-cases.png) | 原图路径、同 ROI、选择规则、成功与失败 |

F02/F03 未分配统计图编号；对应职责由 D01/D02 示意模板承担。F08 灰色单元的示例原始状态是 `error`；F06 的色标量是相似度。F13 没有运行 t-SNE/UMAP，附带坐标纯为教学。F14 的图像是程序生成的占位几何图，不是任何论文或实验样本。

## 表格：4 套同源多格式模板

调用 [tablekit.py](../scripts/tablekit.py)。输出原始统计结果的 CSV、Markdown、booktabs LaTeX、SVG/PDF/PNG 和供 PPTX 使用的表格 JSON。PPTX 为原生表格，不是表格截图。

| ID | 配置 | 可直接插入的表格 | 预览 | PPTX 页 |
| --- | --- | --- | --- | --- |
| T01 主实验，协议分组/并列/失败 | [JSON](examples/configs/T01-main.json) | [LaTeX](gallery/T01-main.tex) · [CSV](gallery/T01-main.csv) · [Markdown](gallery/T01-main.md) | [PNG](gallery/T01-main.png) | 6 |
| T02 组件与替代策略 | [JSON](examples/configs/T02-ablation.json) | [LaTeX](gallery/T02-ablation.tex) · [CSV](gallery/T02-ablation.csv) · [Markdown](gallery/T02-ablation.md) | [PNG](gallery/T02-ablation.png) | 7 |
| T03 参数与选择依据 | [JSON](examples/configs/T03-parameter.json) | [LaTeX](gallery/T03-parameter.tex) · [CSV](gallery/T03-parameter.csv) · [Markdown](gallery/T03-parameter.md) | [PNG](gallery/T03-parameter.png) | 8 |
| T04 效果与资源开销 | [JSON](examples/configs/T04-efficiency.json) | [LaTeX](gallery/T04-efficiency.tex) · [CSV](gallery/T04-efficiency.csv) · [Markdown](gallery/T04-efficiency.md) | [PNG](gallery/T04-efficiency.png) | 9 |

T01 可扩展成“噪声条件→数据集→指标”或“数据集→检索方向→R@k”。T02 可扩展目标×求解器交叉消融。列组过多时分表；不要用任意缩小字体代替组织。

## 示意图：6 套 SVG 与 11 页原生 PPTX

完整源文件：[paper-figure-table-templates.pptx](native/paper-figure-table-templates.pptx)。页码清单：[slides.json](native/slides.json)。D01–D04、D06 使用 [diagram-scenes.json](diagram-scenes.json) 定义节点与连接；D05 的共享行列定义在 [构建脚本](../scripts/build_native_templates.mjs) 中。

| ID | 模板用途 | SVG | PPTX / 预览 |
| --- | --- | --- | --- |
| D01 | 同输入、同输出的前人/本文路线比较 | [SVG](native/D01-comparison.svg) | 1 · [预览](native/01-D01-comparison.png) |
| D02 | 总体方法及核心模块展开 | [SVG](native/D02-method.svg) | 2 · [预览](native/02-D02-method.png) |
| D03 | 帧、文本、时间与对应问题 | [SVG](native/D03-temporal.svg) | 3 · [预览](native/03-D03-temporal.png) |
| D04 | 检索/排序成功与失败案例 | [SVG](native/D04-retrieval-cases.svg) | 4 · [预览](native/04-D04-retrieval-cases.png) |
| D05 | 有来源的假设与能力矩阵 | [SVG](native/D05-capability.svg) | 5 · [预览](native/05-D05-capability.png) |
| F12 原生图表 | 可修改数值的柱图及嵌入工作簿 | [同数据统计 SVG](gallery/F12-weights.svg) | 10 · [预览](native/10-F12-native-chart.png) |
| D06 | 观察—诊断—干预—边界的组合图布局 | [SVG](native/D06-compound.svg) | 11 · [预览](native/11-D06-compound.png) |

这些页是结构模板，允许删减、重排和扩展。图中模型、损失、矩阵和箭头必须映射到真实方法。修改 JSON 后同时生成 SVG/PPTX；在 PPTX 中手工修改不会自动回写 JSON，正式版本应记录选用的源文件。

## 从模板到论文

1. 填写 [任务说明](templates/figure-brief.yaml)，确定一个需要回答的问题。
2. 选择上表资产，按 [运行说明](../references/running.md) 换入真实 CSV、图像或方法节点。
3. 生成与核对成品，按 [图注模板](templates/captions.md) 填写条件、统计和边界。
4. 用 [返回格式](templates/figure-return.yaml) 向写作模块交付。对概念图不要求伪造实验数据，对未完成实验不画虚构结果。
