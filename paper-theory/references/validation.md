# 实际验证记录

检查日期：2026-11-18（Asia/Shanghai）。Lean 工程及 11 个审查入口已通过。这里记录实际执行结果；不把通用工程的通过状态转移给尚未实例化的新方法。

## 环境与执行对象

- Lean `4.19.0`，提交 `6caaee842e94`，Windows x86_64 官方便携式发行版。
- Lake `5.0.0-6caaee8`。
- Mathlib `v4.19.0`，锁定提交 `c44e0c8ee63ca166450922a373c7409c5d26b00b`，其他依赖保存在 [锁文件](../assets/lean-project/lake-manifest.json)。
- 在工作区 `tmp/paper-theory-check` 中准备依赖并验证，避免将下载缓存放入 skill。交付目录为 [assets/lean-project](../assets/lean-project/lakefile.toml)；它的 8 个源码及配置文件与验证副本的散列一致。

实际收集了下列命令，退出码均为 0：

```text
lake --version
lake env lean --version
lake build
lake env lean Audit.lean
```

完整可执行文件位置、工作目录、源码散列和状态保存在 [verification.json](validation/verification.json)。日志包括 [Lean 版本](validation/lean-version.log)、[Lake 版本](validation/lake-version.log)、[构建](validation/build.log) 和 [公理依赖](validation/axioms.log)。构建日志为最终增量构建记录；核心和示例模块已在此前同一副本中编译，最终检查导入了全部交付模块。

## 已检查的数学范围

| 入口，省略 `PaperTheory.` 前缀 | 实际保证 | 应用仍需承担的条件 |
| --- | --- | --- |
| `minimizer_transfer` | 参数最优点经映射成为原域最优点 | 可行性、覆盖及参数问题最优性 |
| `two_block_descent` | 两次精确块更新使同一目标不增 | 乘积域、旧解可行、两次子问题最优性 |
| `run_feasible` | 递归轨迹保持可行 | 初值可行与真实更新保持可行 |
| `run_descent` | 轨迹每步目标不增 | 真实更新的一步下降与可行性 |
| `approximate_optimum_transfer` | 目标误差最多增加 `η+2ε` | 一致近似界及代理目标比较关系 |
| `convex_attained_envelope` | 有达到值选择器的凸上包络凸 | 切片凸、选择器可行、达到值及上界 |
| `quadratic_step_descent` | 已定义二次目标及更新的一步不增 | 实数运算，`0≤η≤2` |
| `quadratic_run_descent` | 同一实例的递归轨迹每步不增 | 同上；不证明变量收敛 |
| `constant_has_two_minimizers` | 常目标有两个不同最优点 | 具体实数反例 |
| `twoWell_not_convex` | 两个二次式下包络非凸 | 具体函数反例 |
| `squared_one_sided_max_bound_fails` | 一个错误平方步骤不成立 | 具体数值反例 |

源码审查核对了定义、量词和上述说明。完整标量实例的逐项映射见 [使用示例](worked-example.md)。概率泛化界、矩阵谱导数、全部优化收敛层级和来源论文的完整方法没有包含在当前已验证入口中；其研究路线与模板不等同于已完成形式化证明。

## 依赖与占位检查

本工程未发现 `sorry`、`admit`、新增 `axiom`、`unsafe`、`native_decide` 或跳过内核检查的源标记。入口的实际公理依赖为：`run_feasible` 无公理依赖；其他十项依赖标准的 `propext`、`Classical.choice`、`Quot.sound`。没有发现 `sorryAx` 或额外自定义公理。

该检查包含构建与显式入口的传递公理输出，不等于对任意元程序的安全审计。脚本也不会自动判断形式对象是否忠实于真实论文；因此 JSON 中保留 `semantic_mapping: not_reviewed_by_script`，语义说明单独给出。

## 验证脚本的实际行为检查

在隔离的临时 Lean 工程中检查了四种输入，结果见 [verifier-checks.json](validation/verifier-checks.json)：

1. 完整证明，注释含占位关键词：返回 `checked`，没有误报注释。
2. 证明含 `sorry`：Lean 构建本身成功，但脚本检测到 `sorryAx` 和源标记，返回 `not_cleared`。
3. 结论依赖新增公理：构建成功，但脚本识别额外公理，返回 `not_cleared`。
4. 没有显式公理审查入口：返回 `not_cleared`，不把空审查登记为通过。

这是对本脚本主要失效路径的检查，不宣称覆盖所有 Lean 语法或元编程情形。

## Skill 与资料一致性

新理论模块和更新后的写作模块均通过 skill-creator 的 `quick_validate.py`。另检查 YAML/JSON 解析、manifest 文件存在性、Markdown 本地链接、Methods 接口、交付工程散列以及九篇本地 PDF 散列；详细结果保存在 [package-checks.json](validation/package-checks.json)。以上为第三部分开发时的检查记录；五部分现已完成，最终修订与新增状态检查见 [整体验证记录](../../references/final-validation.md)。
