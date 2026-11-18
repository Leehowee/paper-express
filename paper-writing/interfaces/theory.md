# 理论模块接口

## 用途与调用条件

将论文中的数学主张转换为可检查的理论任务，再把结果放回同一条研究主线。Methods 是常见调用方；Abstract、Introduction、Experiments、Conclusion 和 Appendix 可以复用已有结果。用户也可以直接提供方法或命题，独立形成理论任务。

实际模块为 [paper-theory](../../paper-theory/SKILL.md)。调用时读取其 [统一请求与返回协议](../../paper-theory/interfaces/methods.md)，复用已有定义，只加载当前命题所需路线。可直接使用 [请求模板](../../paper-theory/assets/templates/request.yaml) 和 [返回模板](../../paper-theory/assets/templates/result.yaml)。本文件是写作侧适配说明，字段与状态以统一协议为准。

理论模块提供假设、命题、完整证明段落及 Lean 工程。具体论文需要完成实例化并实际检查，不能因模块或示例已验证就假定当前方法已获证明。没有可运行环境时，继续完成数学部分和其他写作，Lean 状态保持未运行。

需要请求的情形包括目标等价性、存在唯一性、可识别性、优化性质、误差界、复杂度或特殊情形关系。并非每篇论文都需要新增定理；已有结论可以准确引用，但需检查其条件与当前对象相符。

## 请求信息

只传递当前命题需要的信息，复用已有定义。下表中缺失的关键项应明确标记。

| 字段 | 内容 |
| --- | --- |
| `request_id` / `claim_ids` | 稳定编号与支撑的论文主张 |
| `research_question` / `purpose` | 研究问题，以及希望理论回答什么 |
| `objects_and_notation` | 定义、取值域、维度、概率空间与符号位置 |
| `algorithm_version` | 目标、实际算法、代码版本或材料位置 |
| `candidate_statement` | 带量词、前提和结论的候选命题 |
| `assumptions` | 已知条件、待验证条件及其实际合理性 |
| `existing_evidence` | 相关文献、推导、反例、实验；各自状态 |
| `implementation_gap` | 松弛、近似、随机性、有限迭代、数值精度等差异 |
| `requested_analysis` | 证明、反例、条件优化、复杂度或 Lean 形式化 |
| `placement` | 路线、正文/附录位置及篇幅需要 |

```yaml
request_id: T1
claim_ids: [C1]
purpose: "说明拟议更新在什么条件下改善指定目标"
candidate_statement: "待按实际定义填写，不能用全局收敛等模糊标签替代命题"
assumptions: []
algorithm_version: null
implementation_gap: []
requested_analysis: [assumption_audit, proof_or_counterexample, lean_formalization]
placement:
  route: trans
  statement: methods
  proof: main_text
```

上例是请求格式，不是已成立命题。实验模块的经验现象应先转化为可形式化的问题；若依赖具体数据表现，不能仅靠证明替代相应实证检验。

## 返回信息

| 字段 | 返回要求 |
| --- | --- |
| `statement` / `assumptions` | 最终命题、全部前提、与原请求的差异 |
| `original_statement` / `original_mathematical_status` | 修订时保留原命题及其状态，避免将原命题获否与新命题获证混在一起 |
| `mathematical_status` | 候选、证明草稿、已完成可检查证明、存在缺口或已有反例 |
| `proof_or_counterexample` | 推导、依据和反例；说明尚未解决的步骤 |
| `lean_status` | 未形式化、已形式化未运行、检查未通过、检查通过 |
| `lean_artifacts` | 真实源码、入口定理、Lean/依赖版本、命令、日志、退出状态 |
| `proof_integrity` | `sorry`/`admit`、新增公理、占位依赖和公理审计结果 |
| `semantic_mapping` | 论文定义、算法与 Lean 对象的逐项对应及未覆盖部分 |
| `application_obligations` | 把通用引理应用到当前方法时仍需证明的条件 |
| `supported_claims` | 支持哪些论文判断、不支持哪些外推 |
| `implementation_applicability` | 实际实现是否满足前提，需要怎样修改或降格表述 |
| `manuscript_text` | 可用于正文的命题、解释、证明摘要及完整证明位置 |

`mathematical_status` 与 `lean_status` 分别记录，机器可读返回使用统一协议中的固定英文状态值。数学证明完成但未运行 Lean，不能写“已形式化验证”；Lean 检查通过但语义映射或应用条件未确认，也不能写“本文算法已得到完整保证”。

每个状态绑定具体命题和产物。辅助引理、原命题与修订命题分别对应，写作方只采用最终成立且覆盖当前算法的结论。

## 写作方接收规则

1. 检查命题是否确实回答原来的问题，是否通过增加不现实假设改变了研究对象。
2. 对齐原始目标、松弛目标、子问题、完整算法和离散输出；逐一说明保证覆盖哪一层。
3. 区分目标值收敛、变量收敛、驻点、局部最优和全局最优。理论复杂度说明哪些量固定，不能隐藏内循环或预处理。
4. 核对泛化结论所用样本、分布、独立性和函数类，避免把形式界直接表述为更高测试精度。
5. 检查实际运行记录及占位证明。存在 `sorry`、`admit` 或把待证结论作为新增公理时，记录未完成；合法基础公理与额外假设明确披露。
6. 将新条件、反例或范围限制同步写回所有相关章节，不只修改定理所在段。

发现理论缺口时，可以保留不依赖该结论的算法说明和经验结果，将理论降为待证命题或删去保证；不能为了完成稿件自动生成证明通过状态。

## 位置与独立调用

Trans 默认正文给出必要证明，会议正文保留前提、命题及关键思路，并按规则引用长证明。完整 Lean 工程属于可复查产物，论文正文需解释其科学含义，不必在每节展示工程细节。

独立调用使用同一请求和返回格式，`placement` 可以为空。缺少论文全文不阻止研究一个明确命题；缺少对象定义或关键假设时，先补全这些内容再开展依赖它们的证明。
