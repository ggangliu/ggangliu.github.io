# Project Plan

处理器性能的提升越来越依赖于处理器微体系结构的优化改良,而处理器微体系结构的优化改良离不开体系结构模拟器的辅助,因此体系结构模拟器在现代和未来的高性能处理器设计中的作用越来越重要.

## Project Requirement

- MVP v3.0 Peak Performance FP32 10 TFLOPS
- Evaluation v3.0 architecture design and confirm feature parameter
- Verify v3.0 performance compare to v2.0 by application, for example, pytorch
- Modularization design
  - Some submodules should be implemented as dynamic library

- Architecture
  - Pipeline
      SMT/SIMT/SIMD
    - Fetch
    - MSHR
    - Issue
      - Scheduler
      - Dual-issue
    - Register File
    - Execution
    - Write Back
  - OCC/ICC/DCC
  - ISA
  - Tensor core
  - Memory sub-system
    - Register File -> Compiler 32 Reg/Thread
    - Local Memory -> Compiler使用更多的寄存器，节省多少stack space
    - L1 I/D Cache
    - L2 Cache
    - DRAM
- Graphics
  - Graphics Pipeline (configurable)
  - PA/Raster/Texture/ROP module (configurable)
  - Datapath, for example, with cache, ddr
  - Interact with shader
  - Interconnect
  - Ray tracing
- Performance
  - Visualization performance tool
    - 提供流水线各单元及memory的Peak占有率数据和随cycle变化的占用率
    - Source Code View可以解析mvp asm文件
  - Performance overview of the whole GPU pipeline
  - API Statistics
  - Shader performance
  - Power evaluation
  - Area evaluation
  - Simulation speed
- API
  - Interface lib for reusing OpenCL/OpenGL software stack
  - Async copy
  - Async barrier
  - MVP libs
    - GEMM
  - Refer to BudaM from tenstorrent
    - Keller分享了两个可能预示Tenstorrent生存的理念：一是编程的“开源”，另一个是让那些需要的人可以得到使用AI/CPU IP的授权
      - 开源API: 计划为Tenstorrent的AI硬件引入一个开源的硬件堆栈。BudaM是基于纯C++并带有API的Tenstorrent内核，它允许直接写入硬件，与CUDA相比，BudaM的优势在于，程序员可以完全控制每一个RISC-V内核，包括RISC-V处理器，NoC，矩阵和向量引擎以及SRAM。Keller说他了解到客户真正想要的是“一种在硬件上编程的方法”。Keller的重点是去满足那些从Nvidia那里无法得到真正所需的客户
  - 思考
    - 咱们是否短期内无法解决算力问题，是否可以先解决其他客户的问题，比如对算力要求不高，但能运行一些常见的模型

## External Dependencies

- CI: Gerrit/Jenkins

## Requirement Analysis

## Solution

## Breaking Down Task

|序号|任务  |责任人|完成时间|输入|输出|预期成果|关键节点|
|:-- |:--  |:--|:--|:--|:--|:--|:--|
|    |     |   |   |   |   |   |   |

## Task Plan

``` mermaid
gantt
dateFormat YYYY-MM-DD
%%axisFormat WK%W
inclusiveEndDates
todayMarker stroke-width:3px,stroke:#0f0,opacity:0.5
title MVPGPU-Sim项目计划

section 第一阶段
  需求分析和任务分解                              :done, t1,  2023-08-13, 8w
  评审Product backlog和 Sprint Plan              :done, milestone, crit, m0, after t1, 1d
  可编程部分性能建模                              :done, t2,  after t1,   24w
  Memory子系统性能建模                            :done, t3,  after t1,   12w
  可视化性能分析工具MVP-Perfvision                :active, t4,  after t1,   24w
  MVP v3.0性能建模                                :active, t5,  after t1,   16w
  MVP v3.0性能建模分析报告 release v1.0            :milestone, crit, m1, after t5, 1d
section 第二阶段
  图形固定管线的性能建模                           :t7,  after 2023-11-01,   20w
  SMD复用现有软件栈                               :active, t8,  after t1,   24w
  SMD复用软件栈 release v2.0                      :milestone, crit, m2, after t8, 1d
  Pytorch性能分析                                 :t9,  after t8,   12w
  Pytorch分析报告 release v3.0                    :milestone, crit, m3, after t9, 1d
  Tensor Core建模                                 :t10, after m1,   16w
  Ray Tracing建模                                 :t11, after t7,   16w
  Interconnection建模                             :t13, after m1,   20w
  功耗建模                                        :t14, after m1,   20w
  面积建模                                        :t15, after t14,   20w
  功耗及面积分析报告 release v4.0                  :milestone, crit, m5, after t15, 1d
  MVPGPU-Sim的性能优化和重构                      :t16, after m1,   20w
  输出发明专利                                    :t17, after t7,   16w 
  MVP v4.0性能建模                                :t6,  after m5,   20w
  MVP v4.0性能建模分析报告 release v5.0            :milestone, crit, m6, after t6, 1d
```

## Reference

- [Jim Keller规划AI策略，旨在绕过Nvidi](https://mp.weixin.qq.com/s/pkoBr8FQSv_i_SaBOkHVUA)
- <https://zhuanlan.zhihu.com/p/346141573?utm_id=0>

- [ispass.org∕ispass2007∕keynote2.pdf](https://ispass.org/ispass2007/keynote2.pdf)
- [cse.iitk.ac.in∕users∕biswap∕CASS18∕performance-AMD.pdf](https://www.cse.iitk.ac.in/users/biswap/CASS18/performance-AMD.pdf)

AMD使用

- 功能模拟器SimNow
- 性能模拟器AMD-Core
- 多核互联系统模拟器AMD-NB

性能模拟器一般要求时钟精准，其运行速度一般要比RTL仿真速度快1000倍以上才有实际使用价值
性能模拟器还要支持多种调试手段，比如GDB，快速前进，检查点等。
为了加快模拟器的速度，善于使用类似于SimPoint的取样方法
对于多核互联模拟器考虑到仿真速度, 可以使用时钟近似模式和抽象的处理器核, 但要可以精确反映性能变化趋势

模拟器开发投入很大, 要持续与 RTL 进行校准[２３] ．模拟器的开发首先是一项软件工程, 因此好的软件架构模拟器成功的首要条件, 相比而言计算机体系结构的知识也非常重要但是次要的[１６] ．AMD模拟器的微结构代码约有１０ 万行, 其他结构包含共享库约有４０ 万行代码[１６] , 因此模块化的设计、 良好的代码接口、 使用源代码管理工具等必不可少． 在资源不足的情况下, 基于开源模拟器开发模拟器也是不错的选择