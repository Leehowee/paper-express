# Lean 工程与实例化模板

直接复制 `assets/lean-project/` 作为任务起点，再根据实际方法修改定义、证明与审查入口。详细检查状态见 [验证记录](../../references/validation.md)。工程中的通用引理及示例是实际源码，未解决的科研命题应另列义务，不能直接替换成公理。

## 文件职责

| 文件 | 职责 |
| --- | --- |
| [Core.lean](../lean-project/PaperTheory/Core.lean) | 最优性转移、两块下降、可行轨迹、一致近似与凸包络 |
| [Example.lean](../lean-project/PaperTheory/Example.lean) | 明确目标和更新的完整二次函数实例 |
| [Counterexamples.lean](../lean-project/PaperTheory/Counterexamples.lean) | 多个最优点、非凸下包络、错误平方步骤的反例 |
| [PaperTheory.lean](../lean-project/PaperTheory.lean) | 构建入口，导入交付模块 |
| [Audit.lean](../lean-project/Audit.lean) | 对交付入口打印公理依赖 |
| [lean-toolchain](../lean-project/lean-toolchain) | 固定 Lean 版本 |
| [lakefile.toml](../lean-project/lakefile.toml) 与 [lake-manifest.json](../lean-project/lake-manifest.json) | 依赖声明与实际锁定版本 |

## 实例化计划

```text
论文命题：{{PRECISE_STATEMENT}}
形式对象：{{DEFINITIONS_AND_TYPES}}
复用引理：{{ACTUAL_LIBRARY_THEOREM}}
应用义务：{{OBLIGATIONS_NOT_ALREADY_PROVED}}
入口定理：{{FULLY_QUALIFIED_NAME}}
尚未覆盖：{{FLOATING_POINT_OR_STATISTICS_OR_OTHER_GAP}}
```

例如使用 `run_descent` 时，需要真实更新 `step`、初始可行性、可行性保持和一步下降的证明。只提供这些条件作为参数的通用引理，并未验证具体方法。使用 `convex_attained_envelope` 时，还需要构造或证明存在所需最优解选择，以及它的可行性、达到值和上界关系。

## 以声明类型固定研究主张

以下是需要按实际内容改写的结构说明，不是可编译文件：

```text
definition: 论文中的真实对象、目标和更新
lemma A: 定义有效与可行性
lemma B: 当前方法的一步性质或核心界
theorem T: 使用 A、B 和已核实库定理得到论文命题
audit: 对 T 打印传递公理并核对论文语义
```

已编译工程使用完整的真实证明；不要把本结构说明转换成 `sorry` 填充的文件再报告通过。

## 执行

在复制后的工程目录准备固定依赖，并运行：

```text
lake build
lake env lean Audit.lean
```

也可以从任意目录调用：

```text
python scripts/verify_lean.py PATH_TO_PROJECT --output PATH_TO_LOGS
```

这里的脚本路径相对于 skill 根目录；`--lake` 可以指定已有 Lake 可执行文件。脚本不安装依赖、不升级锁文件、不更改全局配置。首次缺少依赖时单独准备，之后保留锁文件。

## 证明完成记录

```text
源码散列：{{SOURCE_HASHES}}
工具链和依赖：{{EXACT_VERSIONS}}
构建结果：{{EXIT_CODE_AND_LOG}}
审查入口：{{ENTRY_NAMES}}
传递公理：{{ACTUAL_AXIOMS}}
研究假设：{{EXPLICIT_ASSUMPTIONS}}
论文对应：{{MAPPING_REVIEW}}
实现覆盖：{{IMPLEMENTATION_SCOPE}}
```

只记录实际观察到的状态。编译器退出码、占位检查、公理清单和语义审查分别给出。
