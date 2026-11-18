# 来源索引与阅读范围

编制日期：2026-11-18。此次对 GaoHuang 的 6 篇、XiPeng 的 7 篇和 XinwangLiu/TPAMI 的 9 篇本地论文开展图表专题精读：查看选定页面的实际图形和表格，并结合图注、表注及相邻实验解释。共核对 73 个不同的 PDF 页面。并非逐字通读所有正文和附录，也未复现实验或逐格复算全部成绩。

页码是本地 PDF 从 1 开始的物理页序。图表编号沿用本地文件；工作目录中的作者分组不等同于每篇论文为该学者独作。文件散列、版本与页数见 [corpus-manifest.json](corpus-manifest.json)。临时提取和页面渲染不作为 skill 运行依赖。

## 本次定位

| ID | 论文 | 实际视觉核对页 | 图表与提炼重点 |
| --- | --- | --- | --- |
| GH01 | Adaptive Focus for Efficient Video Recognition（来源文件：`GaoHuang/2105.03245v2.pdf`；不随仓库或安装包分发） | 1, 2 | Fig.1：同视频的时间/空间选择；问题示意与路线比较。 |
| GH02 | Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception（来源文件：`GaoHuang/2509.15333v1.pdf`；不随仓库或安装包分发） | 3 | Fig.1：分辨率、规模、效率与自适应感知的概念组织；不是统一协议下的实验曲线。 |
| GH03 | Differential Transformer（来源文件：`GaoHuang/ICLR-2025-differential-transformer-Paper-Conference.pdf`；不随仓库或安装包分发） | 1 | Fig.1：注意力诊断与检索结果并置；相同上下文及归一化，诊断不等于因果证明。 |
| GH04 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models（来源文件：`GaoHuang/JustGRPO.pdf`；不随仓库或安装包分发） | 2 | Fig.1：Pass@k 预算曲线与跨基准结果；注明引用/复现来源，保留交叉。 |
| GH05 | Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?（来源文件：`GaoHuang/NeurIPS-2025-does-reinforcement-learning-really-incentivize-reasoning-capacity-in-llms-beyond-the-base-model-Paper-Conference.pdf`；不随仓库或安装包分发） | 2, 4 | Fig.1–2：搜索树示意、预算曲线及模型×任务分面；收益可能随预算反转。 |
| GH06 | Towards expert-level autonomous carotid ultrasonography with large-scale learning-based robotic system（来源文件：`GaoHuang/s41467-025-62865-w.pdf`；不随仓库或安装包分发） | 2, 3 | Fig.1–2：人工/远程/自主流程、系统闭环与能力矩阵；能力状态不等于性能分数。 |
| XP01 | Partially View-aligned Clustering（来源文件：`XiPeng/2020-NeurIPS-Partially-View-aligned-Clustering.pdf`；不随仓库或安装包分发） | 3, 4, 7, 8 | Fig.1–3，Table 1：部分对齐的问题、流程、参数/对齐比例/过程分析及信息条件分组。 |
| XP02 | Learning with Noisy Correspondence for Cross-modal Matching（来源文件：`XiPeng/2021-NeurIPS-Learning-with-Noisy-Correspondence-for-Cross-modal-Matching.pdf`；不随仓库或安装包分发） | 2, 4, 8, 10 | Fig.1–4，Tables 1–2、4：噪声类型、分治流程、检索表、损失分布、组件与案例。 |
| XP03 | Conditional Representation Learning for Customized Tasks（来源文件：`XiPeng/2025-NeurIPS-Conditional-Representation-Learning-for-Customized-Tasks.pdf`；不随仓库或安装包分发） | 2, 5, 7, 9, 10, 25 | Fig.1–2、5–6、8，Tables 1–2、4–5：任务条件、表征路线、shots、检索、参数与投影。 |
| XP04 | Test-Time Degradation Adaptation for Open-Set Image Restoration（来源文件：`XiPeng/gou24a.pdf`；不随仓库或安装包分发） | 1, 3, 4, 6, 8, 9 | Fig.1–3、5–7，Tables 1、4–6：任务路线、主图、恢复结果、策略与阶段边界、过程案例。 |
| XP05 | Multi-Granularity Correspondence Learning from Long-Term Noisy Videos（来源文件：`XiPeng/ICLR-2024-multi-granularity-correspondence-learning-from-long-term-noisy-videos-Paper-Conference.pdf`；不随仓库或安装包分发） | 2, 4, 7, 9, 20 | Fig.1–2及附录Fig.3，Tables 1–2、7：时间错配、OT流程、检索、编码消融及矩阵案例。 |
| XP06 | Learning with Dual-Level Noisy Correspondence for Multi-Modal Entity Alignment（来源文件：`XiPeng/ICLR-2026-learning-with-dual-level-noisy-correspondence-for-multi-modal-entity-alignment-Paper-Conference.pdf`；不随仓库或安装包分发） | 2, 4, 7, 9, 23, 31, 32 | Fig.1–2、4–5、7、11–15，Tables 1、3、7–8：双层噪声、分块结果、训练/推理消融与成败案例。 |
| XP07 | Uncover Underlying Correspondence for Robust Multi-View Clustering（来源文件：`XiPeng/ICLR-2026-uncover-underlying-correspondence-for-robust-multi-view-clustering-Paper-Conference.pdf`；不随仓库或安装包分发） | 2, 6, 8, 9, 17, 18, 20 | Fig.1–3、4–6、8，Tables 1、3–4：路线差异、生成流程、矩阵、噪声/参数、消融与自然噪声案例。 |
| XL01 | Efficient and Effective Regularized Incomplete Multi-View Clustering（来源文件：`XinwangLiu/TPAMI/1_4_XinwangLiu_TPAMI21.pdf`；不随仓库或安装包分发） | 10, 11 | Table 2–3，Fig.6–7：聚合主结果、不同先验变体、过程与正则参数。 |
| XL02 | Multiple Kernel k-Means with Incomplete Kernels（来源文件：`XinwangLiu/TPAMI/2_2_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发） | 11, 12 | Tables 5–6，Fig.6–8：补全质量与任务效果、缺失/噪声、权重及近似求解轨迹。 |
| XL03 | Absent Multiple Kernel Learning Algorithms（来源文件：`XinwangLiu/TPAMI/2_3_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发） | 8 | Table 1：均值/SD及成对检验；粗体的统计定义区别于数值最优。 |
| XL04 | Communication-Efficient Federated Multi-view Clustering（来源文件：`XinwangLiu/TPAMI/CeFMC_early_access.pdf`；不随仓库或安装包分发） | 10, 13, 14 | Tables III、VIII–IX，Fig.3–5：效果/通信、带符号Gap、目标与指标、联合参数。 |
| XL05 | Contrastive Multi-View Kernel Learning（来源文件：`XinwangLiu/TPAMI/Contrastive_Multi-view_Kernel_Learning.pdf`；不随仓库或安装包分发） | 8, 9, 12, 13 | Tables III、VII–VIII，Fig.5及邻近机制讨论：核配对比较、学习率/归一化与分阶段目标。 |
| XL06 | Hyperparameter-Free Localized Simple Multiple Kernel K-means With Global Optimum（来源文件：`XinwangLiu/TPAMI/Hyperparameter-Free_Localized_Simple_Multiple_Kernel_K-means_With_Global_Optimum.pdf`；不随仓库或安装包分发） | 5, 7, 8 | Fig.1–2、4–5：核/掩码权重、多初始化曲线与实际运行时间协议。 |
| XL07 | Generalized Probabilistic Graphical Modeling for Multi-View Bipartite Graph Clustering（来源文件：`XinwangLiu/TPAMI/Liang-Li-IEEE-TPAMI-2025.pdf`；不随仓库或安装包分发） | 8, 10, 11 | Table IV，Fig.2、4–7：统计排名、图清理、剪枝、相对对数耗时、策略及参数。 |
| XL08 | SimpleMKKM: Simple Multiple Kernel K-means（来源文件：`XinwangLiu/TPAMI/SimpleMKKM.pdf`；不随仓库或安装包分发） | 7, 8, 9 | Tables 2–3，Fig.1–3：主结果、目标×求解器交叉消融、优化与样本规模。 |
| XL09 | Incomplete Multiple Kernel Alignment Maximization for Clustering（来源文件：`XinwangLiu/TPAMI/TPAMI_IncomSimpleMKKM.pdf`；不随仓库或安装包分发） | 7, 9, 10, 11 | Fig.1、4–5，Table 2：缺失模式重复、任务曲线、核权重及统计加粗。 |

## 从来源到通用模板

- [Gao Huang 分析](gaohuang-analysis.md)：观察、概念和研究问题的关系。
- [Xi Peng 分析](xipeng-analysis.md)：路线、分层条件、机制与成败案例。
- [Xinwang Liu 分析](xinwangliu-analysis.md)：系统结果、交叉消融、参数、优化与统计语义。
- [模板目录](../assets/template-catalog.md)：每种套路对应可运行配置或可编辑模板。
- [上游改编](upstream-adaptation.md)：figures4papers 的实际继承、修正及许可。

本次不重新判定论文奖项或最终出版状态，不将个别文章的图形、最佳运行报告、坐标处理或标记规则视为通行规范。GH02 的分析依据本地预印本；XL08/XL09 的本地稿件信息不替代最终出版核验。所有新图表数据均为合成教学数据，未冒用来源论文结果。

复制安装本 skill 后，向上三级的原始 PDF 链接可能需要重新定位；核心流程、代码、示例和模板可在没有这些 PDF 的情况下独立使用。
