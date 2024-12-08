---
layout: post
title: "NVIDIA Fermi Architecture"
tags: nvidia-arch nvidia-chips
---

## A Brief History of GPU Computing A Brief History of GPU Computing

The graphics processing unit (GPU), first invented by NVIDIA in 1999.
Efforts to exploit the GPU for non-graphical applications have been underway since 2003. To address these problems, NVIDIA introduced two key technologies—the G80 unified graphics and compute architecture, first introduced in GeForce 8800.

### The G80 Architecture

NVIDIA's G80 GPU uses the Tesla architecture and is made using a 90 nm production process at TSMC. With a die size of 484 mm² and a transistor count of 681 million it is a very big chip. G80 supports DirectX 11.1 (Feature Level 10_0). For GPU compute applications, OpenCL version 1.1 (1.0) and CUDA 1.0 can be used. It features 128 shading units, 32 texture mapping units and 24 ROPs. Nov 8th, 2006 released.

NVIDIA’s GeForce 8800 was the product that gave birth to the new GPU Computing model. Introduced in November 2006, the G80 based GeForce 8800 brought several key innovations to GPU Computing:

- G80 was the first GPU to support C
- G80 was the first GPU to replace the separate vertex and pixel pipelines with a single, unified processor that executed vertex, geometry, pixel, and computing programs
- G80 was the first GPU to utilize a scalar thread processor, eliminating the need for porgrammers to manually manage vector registers
- G80 introduced the single-instruction multiple-thread(SIMT) execution model where multiple independent threads execute concurrently using a single instruction
- G80 introduced shared memory and barrier synchronization for inter-thread communication

In june 2008, NVIDIA introduced a major revision to the G80 architecture. The second generation unified architecture-GT200(firsted introduced in the GeForce GTX 280), increased the number of streaming processor cores from 128 to 240. Each register file was doubled in size, allowing a greater number of threads to execute on-chip at any given time. Hardware memory access coalescing was added to improve access efficiency. Double precision floating point support was also added  to address the needs of **scientific** and **high-perfomance computing(HPC)** application.
> 从2008就开始认准了科学计算和HPC的方向，到今天为止一直在坚持这个方向，并且也做到世界第一。所以还是得有自己对某个事物的判断，并坚持做到最好

**When designing each new generation GPU, it has always been the philosophy ata NVIDIA to improve both existing application performance and GPU programmability.**

### The GT200 vs G80

![vs](/assets/snip-images/2023-05-30_105441.png)

## An Overview of the Fermi Architecture

### Third Generation Streaming Multiprocessor

### Second Generation Parallel Thread Execution ISA

### Memory Subsystem Innovations

### GigaThreadTM Thread Scheduler

## Conclusion
