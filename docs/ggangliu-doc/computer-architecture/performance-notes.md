---
layout: default
title: 性能笔记
permalink: /performance/性能笔记/
parent: Performance
nav_order: 2
---

# 性能笔记

---

## ILP

在不支持ILP的情况下，SM需要更多的并发warp，至少在40个以上，现在目前的典型值是64个。 4 scheduler x 10 + cycles of latency
在支持ILP的情况下，由于Instruction级别并发的存在，在低纬度上增加了并发性，因此更少的warp能够满足要求。

**ILP有更好的硬件利用率，由于多发射，同时可以运行多条指令，因此硬件的执行单元可以被充分的使用，同时一定程度上能够降低resources的需求**

Resource
:    registers, shared memory, warp slots

## 好性能所需的线程数

- 跟core数量不是特别的相关
- 需要足够的线程（warps）来隐藏延迟

## Concurrent kernel

如果grid太小不足以完全利用GPU，那么多个kernel并发执行，将会有助于提高硬件利用率

## Memory

需记住两件事：

- 存储访问是以warp为单位的
- 内存是离散访问的
  - line/segments
  - 确保从DRAM到SM的bytes是有用的，对于这一点，我们需要理解存储系统是怎么工作的

所有的数据都在DRAM中，所有DRAM的访问都经过L2 Cache

- Global memory
- Local memory
- Texture
- Constants

为了填满memory bandwidth，SM必须发射足够多没有依赖的内存请求

调整线程块的维度，最大化占有

Nvidia的shared memory类似mvp中的local memory

100%的占用率不是达到最大性能所必须的。一旦达到需要的占用率，再进一步的增加不会提升性能

最大性能所需的占用率依赖于代码
:   - 每个线程有更多的非依赖指令，更少的占用率
    - 内存受限的代码往往需要更多的占用空间
![gpu utilization](/images/2023-07-03_205412.png)

线程块太大也有副作用，越多的线程需要更多的资源，也就意味着没有足够的资源给另一个更大的线程块。一个线程块的所有线程在拿到资源之前不会开始运行，也就意味着线程块运行的条件更苛刻。

## 总结

为了好的性能，你需要做些什么？

- 足够的并发性，让GPU保持忙碌
  - 通常的建议
    - 1000+ 线程块/GPU
    - 1000+ 并发线程/SM (32+ warps)
- 最大化内存带宽利用率
  - 注意warp地址模式
  - 是否有足够的独立内存访问来饱和总线
- 最小化warp分支
  - 指令是以warp为单位发射的

该参数起了什么作用
-gpgpu_num_sp_units 4 fp32

-gpgpu_dual_issue_diff_exec_units 0
