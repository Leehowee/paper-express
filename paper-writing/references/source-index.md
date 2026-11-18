# 来源、版本与阅读范围

编制日期：2026-11-17。写作语料来自用户工作目录：XinwangLiu/TPAMI 的 9 篇论文、XiPeng 的 7 篇论文，以及 `nature-skills-main.zip`。未以在线版本替换本地文件。

本轮为**写作结构专题精读**：逐篇分析摘要、问题定位、方法与理论的衔接、实验解释和结论，并在提供的会议附录中选读证明、实现与补充分析。全 PDF 文本提取用于定位，不等同于逐字阅读每页；没有逐项复算所有实验、独立验证论文定理或复现代码。下表如实记录主要阅读范围，未读的参考文献和扩展页不作为归纳依据。

页码均为 PDF 页序，从 1 开始。文件标识、SHA256、总页数和阅读备注见 [机器可读清单](corpus-manifest.json)。本地提取与渲染中间文件保存在工作区 `tmp/pdfs/paper-writing/`，运行本 skill 不依赖它们。

## 期刊语料

| ID | 论文及本地版本 | 主要阅读范围与关注点 |
| --- | --- | --- |
| XL01 | Efficient and Effective Regularized Incomplete Multi-View Clustering（来源文件：`XinwangLiu/TPAMI/1_4_XinwangLiu_TPAMI21.pdf`；不随仓库或安装包分发），TPAMI 43(8), 2021，13 页 | p1–2；p4–6；p7 协议及理论衔接选段；p12 分析与结论。问题分解、期刊扩展、正则动机、求解与泛化 |
| XL02 | Multiple Kernel k-Means with Incomplete Kernels（来源文件：`XinwangLiu/TPAMI/2_2_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发），TPAMI 42(5), 2020，14 页 | p1–3、5；p6 理论与设置选段；p11 §5.8 起、p12 至参考文献前。联合目标、约束、近似算法与保证边界 |
| XL03 | Absent Multiple Kernel Learning Algorithms（来源文件：`XinwangLiu/TPAMI/2_3_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发），TPAMI 42(6), 2020，14 页 | p1–3、6–7；p12 结论。问题与最近工作、多个求解方案、理论条件与预测过程 |
| XL04 | Communication-Efficient Federated Multi-view Clustering（来源文件：`XinwangLiu/TPAMI/CeFMC_early_access.pdf`；不随仓库或安装包分发），2025 accepted author version，16 页 | p1–2；p3–8 方法相关段落；p9 设置与基线选段；p13 分析；p14 参数与结论选段。通用框架/实例、通信与计算成本。视觉核对 p2 |
| XL05 | Contrastive Multi-View Kernel Learning（来源文件：`XinwangLiu/TPAMI/Contrastive_Multi-view_Kernel_Learning.pdf`；不随仓库或安装包分发），TPAMI 45(8), 2023，15 页 | p1–5；p7 协议与结果选段；p9、12–13。核生成与下游实例、结果例外、机制分析、关系讨论 |
| XL06 | Hyperparameter-Free Localized Simple Multiple Kernel K-means With Global Optimum（来源文件：`XinwangLiu/TPAMI/Hyperparameter-Free_Localized_Simple_Multiple_Kernel_K-means_With_Global_Optimum.pdf`；不随仓库或安装包分发），TPAMI 45(7), 2023，11 页 | p1–2、4、6、8、10。由参数选择进入新目标、求解和理论；协议与权重、参数、运行分析 |
| XL07 | Generalized Probabilistic Graphical Modeling for Multi-View Bipartite Graph Clustering（来源文件：`XinwangLiu/TPAMI/Liang-Li-IEEE-TPAMI-2025.pdf`；不随仓库或安装包分发），TPAMI 47(12), 2025，14 页 | p1–4 核心论述；p6、8、11。生成关系、分布实例、约束、统计比较与消融。视觉核对 p8 |
| XL08 | SimpleMKKM: Simple Multiple Kernel K-means（来源文件：`XinwangLiu/TPAMI/SimpleMKKM.pdf`；不随仓库或安装包分发），本地稿件抬头为 submitted 2022，13 页 | p1–8、12。目标与求解器共同变化、性质论证、交叉消融、成本与结论；不将抬头当作最终出版信息 |
| XL09 | Incomplete Multiple Kernel Alignment Maximization for Clustering（来源文件：`XinwangLiu/TPAMI/TPAMI_IncomSimpleMKKM.pdf`；不随仓库或安装包分发），本地稿件抬头为 June 2021，13 页 | p1–5；p6 协议选段；p12、p13 结论。完整/缺失设置关系、参数化、理论与经验的区分；最终出版元数据未另行核实 |

XL04 的页眉保留 submitted 字样，但页脚明确写明已接受及 DOI，因此按已接受作者版本记录。若正式引用 XL08、XL09，应另行核实最终出版信息，不从文件名或稿件抬头猜测卷期。

## 会议语料

| ID | 论文及本地版本 | 主要阅读范围与关注点 |
| --- | --- | --- |
| XP01 | Partially View-aligned Clustering（来源文件：`XiPeng/2020-NeurIPS-Partially-View-aligned-Clustering.pdf`；不随仓库或安装包分发），NeurIPS 2020，11 页 | p1–9 主论述。信息假设、相邻问题、对齐模块、信息条件不同的比较与局限；文中外部补充材料未提供 |
| XP02 | Learning with Noisy Correspondence for Cross-modal Matching（来源文件：`XiPeng/2021-NeurIPS-Learning-with-Noisy-Correspondence-for-Cross-modal-Matching.pdf`；不随仓库或安装包分发），NeurIPS 2021，14 页 | p1–6；p7 协议与设置；p9–10 分析和结论。未对 p8 主结果表作逐项核算；文中外部补充材料未提供 |
| XP03 | Conditional Representation Learning for Customized Tasks（来源文件：`XiPeng/2025-NeurIPS-Conditional-Representation-Learning-for-Customized-Tasks.pdf`；不随仓库或安装包分发），NeurIPS 2025；本地 arXiv v2 标记 2025-12-13，32 页 | p1–10 主论述；核对 p11–22 参考文献/checklist 与 p23 附录起点；选读 p24 的提示词/设置及 p31–32 消融。其他附录表与响应列表未逐项审查 |
| XP04 | Test-Time Degradation Adaptation for Open-Set Image Restoration（来源文件：`XiPeng/gou24a.pdf`；不随仓库或安装包分发），ICML 2024 / PMLR 235，11 页 | p1–9 主论述；p10–11 为参考文献。本地文件无附录。视觉核对 p1 问题对比图 |
| XP05 | Multi-Granularity Correspondence Learning from Long-Term Noisy Videos（来源文件：`XiPeng/ICLR-2024-multi-granularity-correspondence-learning-from-long-term-noisy-videos-Paper-Conference.pdf`；不随仓库或安装包分发），ICLR 2024，20 页 | p1–9；附录 p16 求解推导、p17 效率与噪声验证、p18 应用范围选段。p15、19–20 未逐项深读。视觉核对 p4 方法图 |
| XP06 | Learning with Dual-Level Noisy Correspondence for Multi-Modal Entity Alignment（来源文件：`XiPeng/ICLR-2026-learning-with-dual-level-noisy-correspondence-for-multi-modal-entity-alignment-Paper-Conference.pdf`；不随仓库或安装包分发），ICLR 2026，32 页 | p1–10 主论述；p13 附录目录；p18 证明及实现开头。其余附录按目录定位，未逐项复核噪声统计、扩展实验和案例。视觉核对 p13 |
| XP07 | Uncover Underlying Correspondence for Robust Multi-View Clustering（来源文件：`XiPeng/ICLR-2026-uncover-underlying-correspondence-for-robust-multi-view-clustering-Paper-Conference.pdf`；不随仓库或安装包分发），ICLR 2026，20 页 | p1–9，p10 结论续段；p14–15 证明与实现；p16–19 协议、扩展问题及理论/经验分析选段。p10 的 Table 2 未逐项核算，p20 未深读。视觉核对 p6 |

## 图表核对与阅读限制

对 XL04 p2、XL07 p8、XP04 p1、XP05 p4、XP06 p13、XP07 p6 进行了页面渲染与视觉核对，确认方法图、结果表、正文结构和附录导航的实际位置。渲染输出中的部分字体警告不作为理论符号核验依据。

部分旧 PDF 的公式提取存在字符编码问题。本轮用文字、章节、算法和代表页分析论证结构，未依据乱码重建定理。来源论文中对“最优”“保证”“首次”等判断只作为原文主张，不自动成为模板的科学事实。

## 组织模板来源

主要参考 `nature-skills-main.zip` 中的 `skills/nature-writing/SKILL.md`、`manifest.yaml`、核心文件、章节分片、算法/方法类分片、语言分片，以及 `nature-shared/core/main-text-discipline.md`。具体文件与改编范围见 [改编说明](nature-adaptation.md)。

本部分保留本地来源索引用于追溯；复制安装 skill 后，模板本身仍可使用，指向原始论文和压缩包的链接则需要保留同样的语料目录或重新定位。
