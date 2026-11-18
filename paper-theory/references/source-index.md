# 来源与阅读范围

本模块对本地 Xinwang Liu 的九篇 TPAMI 论文进行理论专题阅读，以三篇首页仅署名 Xinwang Liu 的论文为重点。论文版本、作者角色和阅读深度分别记录；独作身份依据本地 PDF 首页，不由文件名推测。页码统一为 PDF 的一基页序。

## 本地语料

| 编号 | 论文与文件 | 本轮重点阅读 | 作者情况 |
| --- | --- | --- | --- |
| XL08 | SimpleMKKM: Simple Multiple Kernel K-means（来源文件：`XinwangLiu/TPAMI/SimpleMKKM.pdf`；不随仓库或安装包分发） | 第 2–5 页：目标、值函数、梯度、凸性及风险界 | 独作；本地为带 2022 投稿页眉的作者稿 |
| XL06 | Hyperparameter-Free Localized Simple Multiple Kernel K-means With Global Optimum（来源文件：`XinwangLiu/TPAMI/Hyperparameter-Free_Localized_Simple_Multiple_Kernel_K-means_With_Global_Optimum.pdf`；不随仓库或安装包分发） | 第 3–7 页：局部核、嵌套优化、唯一性、可微性及凸性论证 | 独作；本地为 2023 年卷 45 期 7 版本 |
| XL09 | Incomplete Multiple Kernel Alignment Maximization for Clustering（来源文件：`XinwangLiu/TPAMI/TPAMI_IncomSimpleMKKM.pdf`；不随仓库或安装包分发） | 第 3–5 页：半正定补全、重参数化、算法与风险界 | 独作；本地作者稿的占位页眉不作为正式出版年份 |
| XL01 | Efficient and Effective Regularized Incomplete Multi-view Clustering（来源文件：`XinwangLiu/TPAMI/1_4_XinwangLiu_TPAMI21.pdf`；不随仓库或安装包分发） | 第 4–6 页：块更新、权重解、收敛讨论及复杂度 | 合著 |
| XL02 | Multiple Kernel k-Means with Incomplete Kernels（来源文件：`XinwangLiu/TPAMI/2_2_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发） | 第 5–6 页：缺失核更新、半正定投影及泛化结论 | 合著 |
| XL03 | Absent Multiple Kernel Learning Algorithms（来源文件：`XinwangLiu/TPAMI/2_3_XinwangLiu_TPAMI20.pdf`；不随仓库或安装包分发） | 第 5–7 页：表示定理、代理目标与概率界 | 合著 |
| XL04 | Communication-Efficient Federated Multi-view Clustering（来源文件：`XinwangLiu/TPAMI/CeFMC_early_access.pdf`；不随仓库或安装包分发） | 第 8 页理论与通信分析；另做全文理论位置检索 | 合著；本地接受稿 |
| XL05 | Contrastive Multi-view Kernel Learning（来源文件：`XinwangLiu/TPAMI/Contrastive_Multi-view_Kernel_Learning.pdf`；不随仓库或安装包分发） | 第 3–4 页：特征映射、核归一化与优化链 | 合著 |
| XL07 | Generalized Probabilistic Graphical Modeling for Multi-View Bipartite Graph Clustering（来源文件：`XinwangLiu/TPAMI/Liang-Li-IEEE-TPAMI-2025.pdf`；不随仓库或安装包分发） | 第 3–4、6 页：概率模型、下界、实例化及算法分析 | 合著 |

另核对全部九篇首页作者栏，并检索定理、证明、假设和收敛相关位置。上表表示实际精读范围，不表示复核了每篇全部附录或实验。对关键公式进行了 PDF 页面图像核对：XL08 第 4 页，XL06 第 4、6 页，XL09 第 4 页。

## 补充材料

读取作者网站的 [SimpleMKKM 补充证明](https://xinwangliu.github.io/groupmember/Appendix_SimpleMKKM.pdf)，共 2 页，第二页进行了图像核对。该文件仍有未解析编号和引用占位，按公开作者补充稿处理，不推定为最终出版补充材料。记录中的文件散列用于区分后续版本。

XL09 的补充证明及其他论文中被指向的外部证明，未因正文声称“见补充材料”就当作已验证。本模块不补写原作者缺失的推导，也不声称复现论文实验。

## 从阅读到通用规则

- 来源观察：论文如何把研究问题连接到目标、命题、算法和风险解释。
- 数学审查：检查每一步实际需要的前提，区分成立的证明模式、待补条件和无效的一般推理。
- 设计扩展：将这些模式整理为通用路线、可填写的命题及正文模板，并自行构造 Lean 引理和示例。

Lean 工程是本模块编写的通用证明资产，**不是上述九篇论文的完整形式化复现**。具体分析见 [独作论文](solo-paper-theory.md)、[其他论文](other-paper-theory.md)；反例及其适用范围见 [反例说明](counterexamples.md)。语料散列与阅读记录见 [corpus-manifest.json](corpus-manifest.json)。
