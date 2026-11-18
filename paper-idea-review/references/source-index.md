# 来源、版本与阅读范围

编制与元数据核查日期：2026-11-17。本包分析的是用户放在工作区的六个 PDF；官方网页用于核实发表信息和奖项，不替换本地文本的页码。文件摘要与阅读记录见 [corpus-manifest.json](corpus-manifest.json)。

## 页码与证据规则

- `PDF p./pp.` 指相应本地文件从第一页开始的页序，不是网页页码或正式期刊页码。
- 案例中的“本技能重构的问题”、玩具例子和审查规则为本次分析；论文结果、作者解释、分析推断分别表述。
- “精读”指围绕问题提出、方法依据、关键检验和结论边界的有目的阅读，不代表已核查每个表格、全部参考文献、代码或外部附件。
- 本轮不是当前领域新颖性的系统检索。实际使用技能评价新 idea 时，仍需核查相应最新文献。

## 两篇 Nature 系列期刊论文

### GH-U：UltraBot

- **题名**：*Towards expert-level autonomous carotid ultrasonography with large-scale learning-based robotic system*。
- **作者标识**：Haojun Jiang、Andrew Zhao、Qian Yang 等，含 Gao Huang；完整作者以原文为准。
- **发表信息**：Nature Communications **16**, 7893 (2025)，DOI `10.1038/s41467-025-62865-w`。[出版页面](https://www.nature.com/articles/s41467-025-62865-w)；[出版方 PDF](https://www.nature.com/articles/s41467-025-62865-w.pdf)。
- **本地文件**：s41467-025-62865-w.pdf（来源文件：`GaoHuang/s41467-025-62865-w.pdf`；不随仓库或安装包分发），21 页。
- **阅读重点**：pp.1–8 的问题、系统、数据与评价；pp.9–10 的图注和相关结果；pp.12–13 的数据量分析与讨论；p.15 的方法及受试者信息。视觉核对 p.3、p.9。
- **边界**：未随本地 PDF 提供的独立补充材料、视频与原始数据未做完整审计。
- **分析文件**：[UltraBot 案例](cases/ultrabot.md)。

### GH-A：AdaptiveNN

- **题名**：*Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception*。
- **作者标识**：Yulin Wang、Yang Yue、Yang Yue 等，含 Gao Huang；两位 Yang Yue 是原文中不同作者，不自行去重。
- **发表信息**：Nature Machine Intelligence **7**, 1804–1822 (2025)，2025-11-06 发表，DOI `10.1038/s42256-025-01130-7`。[出版页面](https://www.nature.com/articles/s42256-025-01130-7)。
- **本地文件**：2509.15333v1.pdf（来源文件：`GaoHuang/2509.15333v1.pdf`；不随仓库或安装包分发），95 页；首页日期 2025-09-22。[arXiv 版本记录](https://arxiv.org/abs/2509.15333)。
- **版本区别**：分析页码、公式与措辞来自本地预印本，不宣称与正式发表版逐页相同。正式期刊信息只用于确认作品身份。
- **阅读重点**：pp.1–5 的问题与框架；pp.7–10 的建模与训练；pp.12–13、15、17、19–20 的主要结果；pp.21–23 的相关方法、讨论或证明片段；pp.26–27 的人类比较与阈值设置；p.32 的策略和停止控制。视觉核对 p.3、p.32，以及补充 pp.44–49。
- **边界**：pp.44–95 的补充内容为图像型页面，文本提取为空；本次实际视觉阅读其中 pp.44–49 的相关工作、比较控制及部分设置。其余补充表格未逐项阅读或核验。生成页面图片不等于已经阅读。
- **分析文件**：[AdaptiveNN 案例](cases/adaptivenn.md)。

## 获奖会议论文

### GH-R：RLVR

- **题名**：*Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?*
- **作者标识**：Yang Yue、Zhiqi Chen 等，含 Gao Huang；完整名单见原文。
- **发表信息**：NeurIPS 2025。[会议正式 PDF](https://papers.nips.cc/paper_files/paper/2025/file/537d5aa768c2d534016a4d06f87bc8fb-Paper-Conference.pdf)。
- **奖项**：NeurIPS 2025 **Best Paper Runner-Up**。官方公告将其列在 Runners Up 中，不记为 Best Paper Winner。[官方获奖公告](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)。
- **本地文件**：会议论文 PDF（来源文件：`GaoHuang/NeurIPS-2025-does-reinforcement-learning-really-incentivize-reasoning-capacity-in-llms-beyond-the-base-model-Paper-Conference.pdf`；不随仓库或安装包分发），36 页。
- **阅读重点**：pp.1–10 主文；pp.16–17 的指标与局限；p.19 的 CoT 检查；pp.21–23 的轨迹、覆盖、训练设置与熵相关分析。视觉核对 p.2、p.4。
- **边界**：未复现模型训练，未独立重评全部生成轨迹或全部后续个案。
- **分析文件**：[RLVR 案例](cases/rlvr.md)。

## 另外三篇对照论文

| 代号 | 作品与本地版本 | 重点阅读范围 | 分析 |
| --- | --- | --- | --- |
| GH-D | *Differential Transformer*；本地 PDF（来源文件：`GaoHuang/ICLR-2025-differential-transformer-Paper-Conference.pdf`；不随仓库或安装包分发），21 页，首页标注 ICLR 2025 | pp.1–3；p.4 的相关设置；pp.6–7、9–10 的诊断与消融；p.16 的匹配训练设置；视觉核对 p.1 | [机制设计案例](cases/differential-transformer.md) |
| GH-F | *Adaptive Focus for Efficient Video Recognition*；本地 PDF（来源文件：`GaoHuang/2105.03245v2.pdf`；不随仓库或安装包分发），12 页，arXiv:2105.03245v2 | pp.1–3、5、7–9、12；视觉核对 p.1 | [问题定位案例](cases/adafocus.md) |
| GH-J | *The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models*；文件名 JustGRPO.pdf（来源文件：`GaoHuang/JustGRPO.pdf`；不随仓库或安装包分发），19 页，首页日期 2026-06-09 | pp.1–11 的相关主文，pp.17–19 的随机顺序与限制分析；视觉核对 p.2 | [假说与简化案例](cases/justgrpo.md) |

后三篇按本地材料确认身份；本轮未另行认定 AdaFocus 的最终出版版本，也未认定 JustGRPO 的最终 venue 或奖项。不能从文件名推断题名或出版状态。

## 技能模板来源与可迁移性

来源为用户提供的 `nature-skills-main.zip` 快照，具体文件、继承原则和修改范围见 [nature-skills 改编说明](nature-skills-adaptation.md)。没有把参考包中的其他工作流全部执行或全部移植。

技能正文及参考案例可在不带原始 PDF、zip 和临时提取文件的情况下使用。此处指向工作区上级的链接仅供本次来源核查；移动技能目录后若该链接失效，可用题名、DOI、版本及文件摘要重新定位，不影响独立审查流程。
