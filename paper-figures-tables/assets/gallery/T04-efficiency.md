| Method / variant | Inference / ACC (%) ↑ | Inference / Latency (ms) ↓ | Inference / Memory (GB) ↓ |
| --- | --- | --- | --- |
| Same device / batch / precision / input / timing scope |  |  |  |
| Small | 70.0 ± 0.3 | **12.0 ± 0.3** | **2.0 ± 0.3** |
| Large | **82.0 ± 0.3** | 45.0 ± 0.3 | 6.0 ± 0.3 |
| Adaptive | 80.0 ± 0.3 | 24.0 ± 0.3 | 3.0 ± 0.3 |

SYNTHETIC EXAMPLE. Synthetic means and SD over three independent runs. Latency includes preprocessing, model and postprocessing; memory denotes peak allocation. No real hardware was measured. Bold: best displayed mean within each comparison block; ties at displayed precision are retained. This marking is not a significance test.
