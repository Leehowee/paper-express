---
name: paper-express
description: Paper-Express routes research-paper work through five reusable modules for idea and problem review, Transactions and CCF-A writing, mathematical theory and Lean, scientific figures and tables, and critical manuscript review. Use for 科研论文技能、论文全流程、idea 到成稿、多模块协同 or when the user needs help selecting a Paper-Express module. Load only the module needed for the current task.
---

# Paper-Express

围绕研究问题、核心主张、方法、证据和适用边界，选择当前需要的模块。五部分可分别使用，不要求按顺序执行，也不把一次局部任务扩展为完整论文流程。

## 选择入口

| 当前任务 | 模块 | 实际交付 |
| --- | --- | --- |
| 检查 idea、问题、假说与可行性 | [Idea 与问题审查](paper-idea-review/SKILL.md) | 多条研究路径、创新与重要性判断、验证思路 |
| 起草、重组、润色或压缩正文 | [论文写作](paper-writing/SKILL.md) | Trans 与 CCF-A 各章节的实际稿件和成段模板 |
| 建立数学结论、证明、反例或形式化 | [数学理论与 Lean](paper-theory/SKILL.md) | 假设、命题、证明及真实验证状态 |
| 制作科研图表、图注及可编辑文件 | [科研图表](paper-figures-tables/SKILL.md) | 绘图与制表代码、PPTX、SVG 及数据对应 |
| 审查成稿、定位问题或核验修改 | [成型论文批判审查](paper-critical-review/SKILL.md) | 有证据的审稿报告、修改方案与复核结果 |

读取目标模块的 `SKILL.md` 后，按其 manifest 或内部入口加载相关材料，不一次性读取所有模板。用户明确指定部分时直接进入；已知上下文复用，不重复索要。

## 跨模块工作

保留研究问题、claim_id、稿件版本、证据位置、成立条件和待定状态。复杂任务按 [共用上下文与状态](shared/research-context.md) 串联，可使用 [交接模板](assets/templates/research-context.yaml)；小任务直接传递必要信息。

- 写作遇到需要建立的理论或待制作的图表，使用写作模块的相应接口。
- 用户要求审查成稿时，审查方检查实际稿件和证据；需要修改时将 issue_id 与关闭标准返回对应模块。
- 需要新研究数据或实验时，明确执行任务与当前证据缺口，不让写作、证明或绘图模板虚构结果。
- 其他模块返回“完成”时，仍核对实际产物及其覆盖范围。未运行 Lean、未复现实验、未核实文献的状态必须保留。

输出默认是用户所需的成品：优化后的问题、正文、理论、图表或审稿报告。来源、设计范围与模块关系见 [architecture.md](architecture.md)，最终修订的实际检查见 [整体验证记录](references/final-validation.md)。本目录提供本地技能源文件，是否已被宿主安装或自动发现应以实际环境为准。

面向不同 agent 的发布包、安装方式与模块调用例子见 [INSTALL.md](INSTALL.md)。维护目录保留各模块入口；安装时使用 `dist/` 中生成的标准技能 ZIP。
