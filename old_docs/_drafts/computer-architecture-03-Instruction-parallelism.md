---
layout: post
title: "Computer-Architecture Chapter 3: Instruction-Level Parallelism and Its Exploitation"
tags: other-arch
---

## 3.4 Overcoming Data Hazards With Dynamic Scheduling

一个简单的静态调度管线获取一条指令并发射它，除非该指令和已经在管线中的指令直接有数据依赖，并且刚获取的指令不能通过不能通过bypassing或forwarding来隐藏。如果存在不能被隐藏的数据依赖，那么冲突检测硬件就会从需要使用前一条指令结果的指令开始停滞流水线，就不会有新指令获取或者发送直到依赖清除。

在这一节，我们探索dynamic scheduling，一种硬件在维护数据流和异常行为的时候重排指令的执行顺序以减少停滞的技术。Dynamic scheduling有如下一些好处：

1. 允许基于某一个管线编译的代码能够高效的运行在另一个管线上
2. 能够处理一些在编译时不知道依赖的情况
3. 可能是最重要的，允许处理器容忍非预测延迟，比如cache misses，通过在等待miss被解决的时候执行其他代码

### Dynamic Scheduling: The Idea

简单流水线技术的主要限制是其使用顺序指令发射和执行：指令是按照program order发射的，并且如果一条指令在流水线中停滞了，后续的指令就不会被处理。

```csv
fdiv.d f0,f2,f4
fmul.d f6,f0,f8
fadd.d f0,f10,f14
```

register renaming

Imprecise exceptions的发生可能有以下两个可能性：

1. 流水线可能已经完成的指令在program order中是晚于产生异常的指令
2. 流水线可能还没有完成一些在program order中是早于产生异常的指令
