# Methods 与独立调用协议

本模块是 `paper-theory` 的实际入口。Methods 常通过 [写作侧接口](../../paper-writing/interfaces/theory.md) 调用；独立任务直接使用同一格式，论文位置可以为空。接口描述上下文传递，不假装存在自动 RPC 或工具插件。

## 最小输入与扩展输入

最小输入是对象定义、当前操作或候选命题，以及希望得到的结论。已有正文、代码与证明直接复用；只补当前问题所需信息。

| 字段 | 含义 |
| --- | --- |
| `request_id` / `claim_ids` | 稳定任务和论文主张编号 |
| `research_question` / `purpose` | 为什么需要此理论，它应支持哪一关系 |
| `objects_and_notation` | 定义、维度、量词、概率空间及原位置 |
| `algorithm_version` | 目标、更新、代码版本、停止条件 |
| `candidate_statement` | 候选命题，或需要从操作中建立的性质 |
| `assumptions` | 已证明、拟采用、待核查条件及来源 |
| `existing_evidence` | 证明、反例、文献、数据的真实状态 |
| `implementation_gap` | 近似、浮点、随机、取整及有限迭代差异 |
| `requested_analysis` | 条件审查、证明、反例、形式化或正文写作 |
| `placement` | 路线、正文或附录位置；独立调用可为空 |

可复制格式见 [request.yaml](../assets/templates/request.yaml)。

## 返回格式

| 字段 | 必须表达的内容 |
| --- | --- |
| `statement` / `assumptions` | 最终命题、条件，以及相对请求的变化 |
| `original_statement` / `original_mathematical_status` | 命题经过修订时，保留原命题及其状态；未修订可为空 |
| `mathematical_status` | candidate / proof_draft / proved / gap / refuted |
| `proof_or_counterexample` | 完整推导、来源依赖、反例或具体缺口 |
| `lean_status` | not_formalized / source_unrun / check_failed / checked |
| `lean_artifacts` | 源码、入口、版本、锁定依赖、命令和日志 |
| `proof_integrity` | 占位、公理、额外条件和信任扩展的检查 |
| `semantic_mapping` | 定义、算法、量词和结论的对应及未覆盖部分 |
| `application_obligations` | 库引理用于当前方法时仍需证明的条件 |
| `supported_claims` | 已支持主张及禁止外推的范围 |
| `implementation_applicability` | 实现是否满足条件，误差如何处理 |
| `manuscript_text` | 命题、证明、含义和位置的实际文字 |

可复制格式见 [result.yaml](../assets/templates/result.yaml)。状态用固定英文值便于追踪，面向用户的解释可用中文。

`mathematical_status` 只描述同一条返回记录中的 `statement`。原命题有反例而修订命题已证明时，分别记录 `original_mathematical_status: refuted` 与 `mathematical_status: proved`，不要用一个状态同时描述两者。多条命题分别返回记录并保留各自编号。

`lean_status` 描述当前命题的对应形式化产物；只有不相关的条件引理源码时，当前算法命题仍可为 `not_formalized`，该引理另记在 `lean_artifacts.auxiliary_artifacts` 中，并标记其自己的 `source_unrun` 等状态。不能把辅助片段状态移给完整算法。

跨模块任务可按 [共用上下文](../../shared/research-context.md) 保留版本与主张编号；本模块独立使用时无需该文件。

## 写作方如何接收

1. 检查结论是否仍回答原问题，新增假设是否改变研究对象。
2. 对齐原始问题、松弛、子问题、算法和最终输出；确认每次保证传递都有依据。
3. 将完整数学证明、Lean 检查和语义覆盖分别判断。仅通用引理通过时，不把当前方法写成已验证。
4. 检查未完成的应用条件，特别是内层精确性、可行性、最优解覆盖和样本外定义。
5. 根据实际状态使用“证明”“在假设下成立”“经验观察”或“待证”。
6. 新条件或反例影响主张时，同步更新摘要、引言、方法、实验解释和结论。

理论暂未完成不阻止不依赖它的算法描述和经验结果继续写作。没有形式化环境时，明确保留未运行状态；不能因模块已存在就声称 Lean 已执行。
