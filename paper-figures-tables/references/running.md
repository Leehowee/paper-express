# 运行、换数据与编辑

命令从本 skill 目录运行。路径含空格时加引号。Python 示例已实际运行；这不表示所有机器都具备同一字体、包版本或 PowerPoint 渲染环境。

## Python：图与表

建议 Python 3.12 或以上，使用隔离环境（固定的 NumPy 版本要求至少 3.12）。依赖固定在 [requirements.txt](../requirements.txt)。

```sh
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/figurekit.py assets/examples/configs/F01-motivation.json --out output
python scripts/tablekit.py assets/examples/configs/T01-main.json --out output
python scripts/render_all.py
```

激活 `.venv` 后再运行 pip，或将命令中的 `python` 换成 `.venv` 内的 Python。`render_all.py` 读取包内全部示例并更新 `assets/gallery`；`make_examples.py` 会重新生成合成数据，真实项目不要把数据放在它管理的示例目录。

真实任务建议复制 JSON 到项目的 `figures/configs/`，放入真实 CSV/图像，设置 `data` 相对于 JSON 的路径，并使用独立 `--out`。填写 `provenance`、`synthetic: false`、实际 `independent_unit`、指标名称、单位和 caption；关闭合成标识只适用于已经换入真实且有来源的数据。`title` 可以删去，将完整标题留给论文图注。

代码输出 `.audit.json`，记录源数据/配置散列、生成代码散列、运行库版本、物理尺寸和统计摘要。渲染完成后其中 `visual_review` 仍为 `required`：程序不会自行声称有人看过图。

来源路径优先相对于审计文件保存；Windows 跨磁盘时保留绝对路径。移动工程后需要重新定位这些包外来源并核对散列，不把路径失效当成原数据不存在。

## 输入表结构

所有文件为带表头的 UTF-8 CSV。相同统计单元重复出现会被拒绝。数值必须有限；失败用明确状态，不能写 NaN/Inf 或填 0。

重复或空列名、行字段数不一致、缺失观测编号会被拒绝，避免静默覆盖数值。CSV 由标准解析器读取，支持正确引用的逗号、引号与换行。JSON 的 `synthetic`、分组 `rank` 使用真正的布尔值；图表 ID 只用于文件名，不含目录。配置中的面板、系列、比较组、方法与结果列保持唯一，复制模板后应同步修改这些标识。

| kind | 必需 CSV 字段 | 关键 JSON 字段 |
| --- | --- | --- |
| curves | panel,series,x,run,value,status | panels：id、series、xlabel、ylabel；可选 xscale、ylim、default、phase |
| ablation | series,run,value,status | series、reference、ylabel、delta_label |
| heatmap | panel,x,y,value,status | panels 的 x_values/y_values、轴名；vmin/vmax、colorbar、annotate |
| distribution | series,sample_id,value | series、range、bins、xlabel |
| embedding | panel,sample_id,class,x,y | panels、classes、xlim/ylim、projection_protocol |
| efficiency | series,run,cost,score,status | series、轴名、hardware_protocol |
| weights | series,component,value | series、components、normalized、ylabel、ymax |
| cases | case_id,method,path,outcome,roi_x,roi_y,roi_w,roi_h | methods、case_ids、selection_protocol |
| table | group,method,dataset,metric,run,value,status | groups、columns、uncertainty、caption、short_note |

通用 JSON 字段：`id`、`kind`、`data`、`synthetic`、`provenance`、`width_mm`、`height_mm`、`font_pt`、`dpi`、`formats`。格式支持 SVG/PDF/PNG。默认配色支持至多六个系列，更多系列先分面或明确扩展编码。

中文标签可通过 `font` 指定目标机器已安装的中文字体，随后重新渲染检查缺字和宽度；默认字体用于英文图表，不承诺在所有环境覆盖中文。

`uncertainty: sd` 计算独立运行的均值及样本 SD（分母 n−1），要求至少两次；`none` 不画误差。代码不从已发表的一个均值反推 SD，也不自动执行显著性、SE、bootstrap CI 或多重比较。需要这些分析时由适当统计流程提供原始结果与明确实现，再扩展图形。曲线中的 run 可以是独立种子或缺失模式，但不能把同一次运行的迭代点当成独立重复。

F04 的配对差只接受完全相同的 run ID，不自动取交集。差值方向是 reference−variant，是否有利取决于指标方向；`delta_label` 必须注明真实单位。F11 固定为成本越小、效果越大，经验前沿仅对已测均值成立，不是显著优势声明。

热力图必须显式提供每个声明格点；失败状态可为 `NR/OOM/timeout/error/NA`，value 留空，显示为灰色 NA，具体原因保存在审计文件并写入图注。单元格是离散已测组合，不对参数空间插值。案例路径相对于 JSON，同行要求同尺寸与同 ROI；这只检查显示匹配，不验证医学、物理或语义上的配准。

## 表格配置与多格式同步

`groups` 定义可比块，每块有 `id/label/methods`。每个方法可以附组件或阶段字段，由 `descriptor_columns` 定义显示顺序。`columns` 定义 dataset、metric、label、direction（up/down/none）和 decimals。需要参照但不可排名的块设置 `rank: false`。

默认加粗按每个可比块内显示精度后的均值决定，保留并列；不会跨协议排名。缺失单元必须有状态行，同一单元混有成功和失败会拒绝自动聚合，要求先单独报告完成率及成功条件的统计。表注由配置提供并补充实际加粗规则。

LaTeX 使用 `booktabs` 与 `table*`；单栏可改为 `table`。模板导出不等于已在用户的期刊类文件中编译，插入稿件后仍需核对宽度、字体和跨页行为。CSV/JSON 为数值来源，不能在 LaTeX、PPTX、SVG 三处分别改成绩。

## 原生 PPTX 与 D 类 SVG

现成的 [PPTX](../assets/native/paper-figure-table-templates.pptx) 可以直接打开修改文字、节点、连接线、原生表格和原生图表。代码重建采用 Node.js 与 `@oai/artifact-tool`；它是本次环境提供的运行库，不是 Python 依赖，也未在本包中分发。

```sh
node scripts/build_native_templates.mjs --out output/native --build output/build --editability-check
```

可用环境变量：

- `ARTIFACT_NODE_MODULES`：包含 `@oai/artifact-tool` 的 node_modules 绝对路径；普通项目可以直接安装在正常 Node 解析路径下。
- `PRESENTATION_SKILL_DIR`、`RUNTIME_PYTHON`、`RUNTIME_NODE_MODULES`：可选的 Codex 演示文稿验证环境。配置后执行结构、版面、字体声明、图表工作簿及重新导入检查；未配置时脚本明确报告仅导出，不宣称完成这些检查。

先运行 Python 表格生成，构建器从 `.table.json` 读取表格；F12 原生图表从对应 CSV 读取数值。该原生图表示例仅接受不带引号/逗号标签的简单三列 CSV，复杂标签需更换完整 CSV 解析器。其他统计图仍由 Python 生成，不能声称 PPTX 中包含每张统计图的原生数据图表。

构建器默认重建本模板库，因此保留示例标题、SYNTHETIC 标识与说明。改编为真实论文时，同时依据真实材料更新页内说明、图注与数据来源，不能只更改数字。

脚本默认拒绝覆盖已存在的 PPTX，确定要更新该输出时用 `--replace`。`--init-scenes` 会将 D01–D04/D06 的 JSON 恢复为默认模板，仅在主动重置示例时使用。D05 的行列在构建脚本中统一定义，同时生成 SVG 与原生表格。

`--editability-check` 在临时副本中改标签、移动节点、改填色、表格单元和图表数值，保存后重新导入并检查；原件不变。实际验证范围见 [validation.md](validation.md)。不同 Office 版本中的字体与连线表现还需要在目标应用检查。

## 重新检查模板包

```sh
python scripts/validate_package.py
```

本地原始语料仍在上级目录时可加 `--check-sources`；需要校验本机原生构建收据时加 `--native-receipts {{BUILD_DIRECTORY}}`。脚本检查包内链接、文件格式、源数据散列、表格重算、方向/并列、输入拒绝规则、原生表格/图表及工作簿数值。默认跳过包外来源链接；`--check-sources` 还检查原始论文与上游归档。视觉检查和目标 PowerPoint 应用检查仍需分别完成。

## 参考 API

本次查阅官方 [Matplotlib errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)、[savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) 和 [fill_between 示例](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)。本包采用明确误差条，未将填充带误称为置信区间。具体版本与验证结果随记录保存。
