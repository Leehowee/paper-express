# nature-skills 组织与写法的改编说明

## 来源与许可

来源为用户提供的 nature-skills-main.zip（来源文件：`nature-skills-main.zip`；不随仓库或安装包分发），编制日期 2026-11-17。本 skill 是按当前需求重新组织和改写的版本，未修改原始压缩包，也不要求安装上游 nature-writing。

上游根目录 LICENSE 为 Apache License 2.0，原样保留为 [LICENSE.nature-skills](../LICENSE.nature-skills)。压缩包未发现独立 NOTICE 文件。这里的归属与许可说明针对所参考、改编的技能内容，不将论文 PDF 或图表纳入该许可。

## 读取并采用的文件

以下路径以压缩包中的 `nature-skills-main/skills/` 为起点：

- `nature-writing/SKILL.md`、`nature-writing/manifest.yaml`。
- `nature-writing/static/core/stance.md`、`workflow.md`、`output-format.md`。
- `nature-writing/static/fragments/section/abstract.md`、`intro.md`、`related-work.md`、`method.md`、`experiments.md`、`conclusion.md`。
- `nature-writing/static/fragments/paper_type/algorithmic.md`、`methods.md`。
- `nature-writing/static/fragments/language/en.md`、`zh-to-en.md`。
- `nature-writing/references/experiments.md`。
- `nature-shared/core/main-text-discipline.md`。

第一部分开发已读取的 `nature-shared/core/nature-introduction.md` 也为问题与引言关系提供背景，本轮不依赖其独立执行。压缩包和本轮主要参考文件的散列值保存在 [语料清单](corpus-manifest.json)。

## 采用的组织方式

短入口负责识别任务和选择文件，manifest 显式列出路线与章节，核心文件保留共用原则，章节分片提供具体写法。来源论文分析单独放在 references，按需加载，不让每次写作先阅读整套案例。

本 skill 的路径轴改为 `route × section × task`：先区分 Trans 与 CCF-A，再选择章节和写作动作。`static/routes/` 提供目的、输入、论证顺序、证据要求与完成判据；`assets/templates/` 提供可直接填充的连续段落及润色前后示例。实际写作按当前任务读取对应章节的两层材料。

## 采用并调整的写法

| 上游经验 | 本地实现与调整 |
| --- | --- |
| 科学问题、主张与证据优先 | 共用原则与流程；不补造结果、文献或理论 |
| 一段一个任务，校准语言强度 | language.md；中文指导配英文关系骨架 |
| 章节按任务渐进加载 | manifest.yaml；局部修改不启动整篇流程 |
| 以核心证据决定正文内容 | venue-and-allocation.md；结合两种路线处理 |
| 方法、实验与贡献相互对应 | 两套 Methods/Experiments；增加目标、求解、实例与对照的区分 |
| 正文、图注和补充材料各有职责 | 会议正文/附录配对；期刊保留默认正文完整的用户偏好 |
| 先给正文，再简要报告重要改动 | output.md；不强制每次返回庞大检查表 |

上游主文精简原则主要强调完整证据可分布在 SI 等载体中；本地 Trans 路线依用户要求，默认将必要推导与分析放在正文，不自动沿用 SI 分配。上游具体字数、章节比例或表格视觉偏好没有被转写为所有刊会的强制政策。

## 本轮新增内容

新增两条路线各七个章节模板、可选论证路径、投稿约束记录、正文与附录分配规则、理论与图表请求/返回接口。理论接口特别区分数学证明、Lean 运行状态与编码对实际方法的覆盖；图表接口区分设计方案、生成产物、数据核查和视觉核查。

Xinwang Liu 与 Xi Peng 语料用于补充方法论文的具体组织经验。通用模板正文不保留作者、模型名称、特定任务、实验数值或论文页码；这些内容只在来源分析中出现。

## 成段模板的补充

为直接起草和润色新增 14 个章节资产文件，按两条路线覆盖七类章节。引言与摘要提供多种主线，方法提供定义、目标、求解或组件的连续段落，实验提供主结果、消融、成本和边界等可组合段落。每节均含实际改写模式；共用执行规则要求先返回正文。

这些句型和完整填充示例是本地新写的通用表达，不是来源论文原句或作者授权范文，也不增加新的论文阅读范围。`{{FIELD}}` 必须绑定输入材料；模板中的保证、效果和因果语言仍受证据约束。润色示例中的补充事实需要真实提供，不能由句型反向生成。
