---
layout: post
title: "NVIDIA H100 Tensor Core GPU Architecture"
tags: nvidia-arch nvidia-chips
---

H100 implemented using TSMC’s 4N process customized for NVIDIA with 80 billion transistors.
![SXM5-White](/assets/snip-images/SXM5-White-4-NEW-FINAL.jpg "NVIDIA H100 GPU on new SXM5 Module")

## NVIDIA H100 Tensor Core GPU Overview

H100 with InfiniBand interconnect delivers up to 30 times the performance of A100.

### NVIDIA H100 GPU Key Feature Summary

- New Streaming Multiprocessor
  - New fourth-generation Tensor Cores
  - New DPX Instructions accelerate Dynamic Programming algorithms by up to 7x over the A100 GPU
  - 3x faster IEEE FP64 and F32
  - New Thread Block Cluster feature
    - Threads, Thread Blocks, Thread Block Clusters, and Grids
  - New Asynchronous Execution features
    - Tensor Memory Accelerator (TMA) unit that can transfer large blocks of data very efficiently between global memory and shared memory
    - TMA also supports asynchronous copies between Thread Blocks in a Cluster
- New Transformer Engine
- HBM3 memory subsystem
  - provides nearly a 2x bandwidth increase over the previous generation
  - The H100 SXM5 GPU is the world’s first GPU with HBM3 memory deliveringa class-leading 3 TB/sec of memory bandwidth
- 50 MB L2 cache architecture
- Second-generation Multi-Instance GPU (MIG) technology
- New Confidential Computing support
- Fourth-generation NVIDIA NVLink
- Third-generation NVSwitch
- **PCIe Gen 5** provides 128 GB/sec total bandwidth (64 GB/sec in each direction)

## NVIDIA H100 GPU Architecture In-Depth

### H100 SM Architecture

### H100 GPU Hierarchy and Asynchrony Improvements

### H100 HBM and L2 Cache Memory Architectures
