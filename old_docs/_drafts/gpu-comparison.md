
# GPU Comparisons

[GPU Specs Database](https://www.techpowerup.com/gpu-specs/)

| GPU | GPCs | TPCs | SMs | FP32/SM | Tensor/SM | Memory/Controller | Cache | PCIe  | Process | Die size |
|:----|:---- |:---- |:----|:----    |:----      | :----             |:----  |:----  |:----     |:----  |
|H100 | 8    | 72   | 144 | 128     | 4         | 6 HBM3/ 12 512-bit|60MB L2|PCIe 5 | TSMC 4nm | 814 mm2 |
|A100 | | | | | | | | | TSMC 7nm | |

Fermi -> Kepler  -> Maxwell-> Pascal -> Volta -> Turing -> Ampere -> Ada Lovelace -> Hopper

Tesla G80 2006 -> Tesla 2.0 GT200 2008

|Architecture|Tesla              |Fermi   |Maxwell   |Kepler   |Pascal       |Volta  |Turing   |Ampere   | Ada | Hopper |
|:--         |:--                |:--       |:--      |:--          |:--    |:--|:--|:--|:--|:--|
|When        |2006               |2009      |         |2016         |       |   |   |   |   |   |
|Product     |GeForce 8800       |          |         |Tesla P100   |       |   |   |   |   |   |
|Process     |TSMC 90 nm         |          |         |16 nm        |       |   |   |   |   |   |
|Transistor  |681 million        |          |         |15.3 billion |       |   |   |   |   |   |
|DIE size    |470 mm²            |          |         |610 mm²      |       |   |   |   |   |   |
|GPC         |NA                 |4         |         |             |       |   |   |   |   |   |
|TPC         |8                  |NA        |         |             |       |   |   |   |   |   |
|SM          |16                 |          |         |             |       |   |   |   |   |   |
|SP          |128                |          |         |             |       |   |   |   |   |   |
|CUDA Core   |NA                 |          |         |             |       |   |   |   |   |   |
|Core Clock  |1.35GHz             |          |         |             |       |   |   |   |   |   |
|INT32       |                   |          |         |             |       |   |   |   |   |   |
|FP32        |518Gflops(1.35GHz) |          |         |             |       |   |   |   |   |   |
|SFU         |32                 |          |         |             |       |   |   |   |   |   |
|Register    |8192 regs/SM       |          |         |256 KB       |       |   |   |   |   |   |
|L1 I-Cache  |                   |          |         |4 MB         |       |   |   |   |   |   |
|L1 D-Cache  |                   |          |         |4 MB         |       |   |   |   |   |   |
|L1 T-Cache  |16KB/TPC           |          |         |4 MB         |       |   |   |   |   |   |
|L2 Cache    |96KB               |          |         |4 MB         |       |   |   |   |   |   |
|DRAM        |GDDR3 768MB        |          |         |4 MB         |       |   |   |   |   |   |
|DRAM Clock  |1.08 GHz           |          |         |4 MB         |       |   |   |   |   |   |
|Interface   |384 bits           |          |         |4 MB         |       |   |   |   |   |   |
|Bandwidth   |104 GB/sec         |          |         |4 MB         |       |   |   |   |   |   |
|Texture     |64(37GT/S)         |          |         |10600 GFLOPS |       |   |   |   |   |   |
|ROP         |24(12pixel/cycle)  |          |         |10600 GFLOPS |       |   |   |   |   |   |
|FP32        |                   |          |          |64           |       |   |   |   |   |   |
|FP32        |                   |          |          |5304  GFLOPS |       |   |   |   |   |   |
|Power       |TDP:150W           |          |          |300W         |       |   |   |   |   |   |
