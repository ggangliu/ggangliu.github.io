---
layout: post
title: "Chapter-3 Instruction-Level Parallelism and Its Exploitation"
tags: compiler
---

## 3.1 Basic Compiler Techniques for Exposing ILP

## 3.2 Basic Compiler Techniques for Exposing ILP

这一节介绍一些简单的编译器技术来增强处理器的能力

### Basic Pipeline Scheduling and Loop Unrolling

- To keep a pipeline full
  指令间的并行性必须通过找出不相关且可以在流水线中overlap执行指令序列
- To avoid a pipeline stall
  依赖指令的执行必须跟源指令保持一定时钟周期的距离，这个距离等于源指令的流水线延迟

### Summary of the Loop Unrolling and Scheduling

- Use different registers to avoid unnecessary constraints(e.g., name dependences)
- Eliminate the extra test and branch instructions and adjust the loop termination
- Schedule the code

有三个不同的幅面效果限制loop的unrolling

1. 每次展开所平摊的开销的减少(不太理解)
2. 代码size限制，对于大的loop，代码size的增长基本是确定的，会导致instruction cache miss rate
3. 编译器限制，过于激进的展开和调度会导致*register pressure*，也就是面临寄存器不够分配的问题

loop展开是一个简单且有用的方法，通过增加代码段的size能够被有效的调度

## 3.3 Reducing Branch Costs With Advanced Branch Prediction

Loop unrolling是一种减少分支冒险数量的方法，我们也能通过预测来减少分支导致的性能损失。在这一节，我们研究提升动态预测精度的技术。

### Correlating Branch Predictiors

分支预测器通过使用其他分支的行为去做预测称为correlating predictors或者two-level predictors
(1, 2) 预测器用最后分支的行为去预测
(m, n) 使用最后m个分支从2m个分支预测器中选择