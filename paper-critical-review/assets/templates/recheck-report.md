# 复审报告模板

原版本：{{OLD_VERSION}}；新版本：{{NEW_VERSION}}。本次实际核验 {{MATERIALS_AND_SCOPE}}，未核验 {{UNREVIEWED_SCOPE}}。

所有关闭状态均限于 {{VERIFIED_SCOPE}}。原问题若超出该范围，明确局部已解决与整体尚待核验的区别，不把片段核验写成全文同步完成。

| 问题编号 | 原关闭标准 | 作者所述动作 | 实际改动与证据位置 | 核验结果 | 状态 | 剩余条件 |
| --- | --- | --- | --- | --- | --- | --- |
| {{I_ID}} | {{ORIGINAL_TEST}} | {{REPORTED_ACTION}} | {{VERIFIED_LOCATIONS}} | {{ACTUAL_CHECK}} | {{STATUS}} | {{REMAINDER_OR_NONE}} |

状态取 `open / partially_resolved / resolved / resolved_by_narrowing / withdrawn / not_assessable`。

**证据修复**：{{ISSUE_ID}} 已通过 {{NEW_EVIDENCE}} 解决；这支持 {{FINAL_BOUNDED_CLAIM}}。

**主张收缩**：{{ISSUE_ID}} 通过 {{REMOVAL_OR_NARROWING}} 解决，相关 {{SECTIONS}} 已同步。原来的 {{STRONG_CLAIM}} 仍未得到验证；剩余贡献应按 {{NEW_SCOPE}} 评价。

**尚未解决**：{{ISSUE_ID}} 的 {{REMAINING_LINK}} 仍缺少 {{EVIDENCE}}。建议下一步 {{MINIMAL_REMAINING_ACTION}}，无须重复 {{ALREADY_COMPLETED_WORK}}。

**撤回误判**：复核 {{ORIGINAL_MATERIAL}} 后发现原意见 {{ISSUE_ID}} 不成立，原因是 {{REASON}}。撤回该项，不将其计作作者新增修复。

**总体变化**：当前技术结论为 {{TECHNICAL_STATUS}}；贡献与目标适配判断为 {{CONTRIBUTION_AND_FIT}}。新发现 {{NEW_ISSUES_OR_NONE}} 由 {{NEW_EVIDENCE}} 触发。是否继续修改取决于 {{REMAINING_DECISIVE_ISSUES}}，而不是报告中的问题总数。
