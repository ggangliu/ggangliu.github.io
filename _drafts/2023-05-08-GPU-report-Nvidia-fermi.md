---
layout: post
title: "理解GPU的核心"
tags: nvidia-arch
---

理解GPU的核心：性能+生态

## 1. GPU：计算机图形处理以及并行计算的核心

GPU全称是Graphic Processing Unit，即图形处理单元，是计算机显卡的核心

- 它的主要功能可以分为：1）图形图像渲染计算 GPU；2）作为运算协作处理器 GPGPU
- GPU的功能主要集中于执行高度线程化、相对简单的并行任务处理

GPU vs GPGPU

- GPGPU全称通用GPU，运用CUDA及对应开放标准的OpenCL实现通用计算功能运算，能够辅助CPU进行非图形相关程序执行
- 由GPU性能拓展至计算密集领域，将GPU强大的并行运算能力运用于通用计算领域。多侧重科学计算、AI领域、大数据处理、通用计算、
物理计算、加密货币生成等领域

### 1.1 GPU性能影响因素：微架构、制程、核心频率

评估GPU物理性能的参数主要包括：微架构、制程、图形处理器数量、流处理器数量、显存容量/位宽/带宽/频率、核心频率
![Image](/assets/snip-images/2023-05-08_191932.png)

微架构
: 又称为微处理器体系结构，是硬件电路结构，用以实现指令执行

制程
: 指GPU集成电路的密集度。在晶体管硬件数量一定的情况下，更精细的制程能够减少功耗和发热。现阶段GPU主流最先进工艺制程为5nm

核心频率
: 代表GPU显示核心处理图像频率大小/工作频率

## 2. 性能：决定GPU是否“高效”，其中微架构是GPU性能领先的关键

显存容量：显存作为GPU核心部件，用以临时存储未处理数据
显存位宽：是GPU在单位时钟周期内传送数据的最大位数，位数越大GPU的吞吐量越大
显存频率：显存数据传输的速度即显存工作频率，通常以MHz为显存频率计数单位
显存带宽：显存带宽=显存频率X显存位宽/8，为显存与显卡芯片间数据传输量

### Fermi架构

![Fermi](/assets/snip-images/2023-05-10_200703.png "Fermi")

512 High Performance CUDA cores
:  Each SM features 32 CUDA processors—a fourfold increase over prior SM designs. Each CUDA processor has a fully pipelined integer arithmetic logic unit (ALU) and floating point unit (FPU).
: The Fermi architecture implements the new IEEE 754-2008 floating-point standard, providing he fused multiply-add (FMA) instruction for both single and double precision arithmetic.

16 Load/Store Units
: Each SM has 16 load/store units, allowing source and destination addresses to be calculated for sixteen threads per clock. Supporting units load and store the data at each address to cache or DRAM

4 Special Function Units
: Special Function Units (SFUs) execute transcendental instructions such as sin, cosine, reciprocal, and square root. Each SFU executes one instruction per thread, per clock; a warp executes over eight clocks. The SFU pipeline is decoupled from the dispatch unit, allowing the dispatch unit to issue to other execution units while the SFU is occupied

Dual Warp Scheduler
: The SM schedules threads in groups of 32 parallel threads called warps. Each SM features two warp schedulers and two instruction dispatch units, allowing two warps to be issued and executed concurrently. Fermi’s dual warp scheduler selects two warps, and issues one instruction from each warp to a group of sixteen cores, sixteen load/store units, or four SFUs.
![warp scheduler](/assets/snip-images/2023-05-10_203750.png)

64 KB Configurable Shared Memory and L1 Cache
: One of the key architectural innovations that greatly improved both the programmability and performance of GPU applications is on-chip shared memory. Shared memory enables threads within the same thread block to cooperate, facilitates extensive reuse of on-chip data, and greatly reduces off-chip traffic.

PTX
: PTX is a low level virtual machine and ISA designed to support the operations of a parallel thread processor. At program install time, PTX instructions are translated to machine instructions by the GPU driver

Memory Subsystem Innovations
: NVIDIA Parallel DataCacheTM with Configurable L1 and Unified L2 Cache
![Memory](/assets/snip-images/2023-05-10_205409.png)

GigaThreadTM Thread Scheduler
: One of the most important technologies of the Fermi architecture is its two-level, distributed thread scheduler. At the chip level, a global work distribution engine schedules thread blocks to various SMs, while at the SM level, each warp scheduler distributes warps of 32 threads to its execution units.

Concurrent Kernel Execution
: Fermi supports concurrent kernel execution, where different kernels of the same application context can execute on the GPU at the same time.
![concurrent kernel](/assets/snip-images/2023-05-10_205752.png)

![summary](/assets/snip-images/2023-05-10_204728.png)

### Hopper架构

![Full-H100-GPU](/assets/snip-images/Full-H100-GPU-with-144-SMs-1024x457.png)[^0]
![H100 SM](/assets/snip-images/H100-Streaming-Multiprocessor-SM.png)


## 3. 生态：构筑通用计算壁垒

>[!VIDEO](https://video.tv.adobe.com/v/29770/?quality=12)
![daf](https://www.youtube.com/watch?v=Ptk_1Dc2iPY)


[^0]: <https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth>
