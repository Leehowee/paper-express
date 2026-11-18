# 案例、检索与失败展示

案例解释方法如何工作、怎样失败和适用到哪里。记录选择方式，避免让精挑的案例承担总体性能结论。

## 套路 A：输入—基线—本文—参考，匹配区域

使用 F14。行是样本，列是相同任务下的方法，统一尺寸、裁剪和显示变换。ROI 使用相同像素坐标；需要放大时对所有方法采用相同放大倍数。参考图不存在时删除该列，不能把某个模型输出称为 ground truth。

## 套路 B：查询—条件—候选—排名变化

使用 D04 / PPTX 第 4 页。给出查询及检索标准，候选按实际排名排列，保留候选 ID、相关性标注与前后排名。成功、失败、歧义和属性缺失分别展示。模型生成的理由与核实后的解释采用不同标签。

## 套路 C：时间—片段—文本—对应矩阵

用 D03 加 F06。共用帧序号和真实时间轴，将问题位置与矩阵位置对应。排序和重新对齐不能改变实际时序。对没有合法对应的样本保留空匹配或拒绝位置，不能强制画成一一对应。

## 套路 D：中间状态—最终输出—机制边界

展示固定时间点或预先定义阶段，说明每张中间图由哪个操作产生。各案例使用相同取点规则，避免只挑某次最好轨迹。中间结果更清晰不必然意味着量化效果更好。

图注：

> Qualitative examples selected by {{SELECTION_RULE}} from {{SPLIT}}. Rows correspond to {{CASE_IDS_AND_TYPES}} and columns to {{METHODS / STAGES}}. All methods use the same {{INPUT / ROI / DISPLAY_TRANSFORM}}. {{LABELS}} indicate verified annotations, whereas {{MODEL_EXPLANATION}} is model-generated. The failure case illustrates {{SPECIFIC_LIMIT}}, without estimating its prevalence.

正文从案例回到条件：哪里改善、哪里仍错、什么缺失信息可能造成失败、需要怎样的后续验证。不能把看起来合理的生成解释写成已知因果机制。
