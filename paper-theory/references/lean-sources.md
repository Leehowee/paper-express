# Lean 与 Mathlib 的依据

核查日期：2026-11-18。使用官方文档与项目源文件核对工具行为；网页内容可能更新，实际复现以工程锁定版本和日志为准。

| 来源 | 本模块采用的内容 |
| --- | --- |
| [Lean：Validating Proofs](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) | 证明项检查、`#print axioms`、对信任基础和定理含义的分别审查 |
| [Lean：Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/) | 工程、构建与依赖管理 |
| [Lean v4.19.0 官方发布](https://github.com/leanprover/lean4/releases/tag/v4.19.0) | 本次便携式工具链的来源与固定版本 |
| [Mathlib v4.19.0 工具链声明](https://github.com/leanprover-community/mathlib4/blob/v4.19.0/lean-toolchain) | 与 Lean 版本匹配 |
| [Mathlib v4.19.0 工程声明](https://github.com/leanprover-community/mathlib4/blob/v4.19.0/lakefile.lean) | 依赖与缓存相关配置 |
| [Mathlib 的凸函数定义](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Function.html) | `ConvexOn` 的对象、类型和条件；实现时另外读取了固定版本的源码 |

## 本工程的固定环境

- Lean：`leanprover/lean4:v4.19.0`。
- Mathlib 标签：`v4.19.0`；实际提交：`c44e0c8ee63ca166450922a373c7409c5d26b00b`。
- 其他依赖：以 [lake-manifest.json](../assets/lean-project/lake-manifest.json) 的完整提交记录为准。
- 实际命令和结果：见 [验证记录](validation.md)。

此版本用于可复现示例，不作为最新版推荐。最新文档提到的其他检查工具或功能，不能据此假定已经在 v4.19.0 安装、可用或执行。本轮使用普通 Lean 构建、显式公理打印和源码审查，没有声称运行额外独立检查器。

复制工程后可在已有 Lean/Lake 环境构建。依赖缺失时先准备锁定依赖；升级版本是单独操作，升级后重新检查源码与日志。
