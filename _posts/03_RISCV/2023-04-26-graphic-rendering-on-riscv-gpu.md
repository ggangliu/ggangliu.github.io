---
layout: post
title: "Accelerating Graphic Rendering on Programmable RISC-V GPUs"
tags: riscv
---

## Motivation

- GPU acceleration for edge computing
GPU has many applications, such as, Graphics, ML, Crypto, etc
- Rearch in GPU Hardware Architecture
  - RISC-V ISA extension for graphics
  - Open-source Vulkan software stack

## GPU Framework Overview

![overview](/assets/snip-images/2023-04-26_114533.png)

## 3D Graphics Pipeline Stages

![Pipeline](/assets/snip-images/2023-04-26_114912.png)

## Graphics Hardware Microarchitecture

![microarchitecture](/assets/snip-images/2023-04-26_115258.png)

## Rasterizer Unit

![Rasterizer](/assets/snip-images/2023-04-26_115609.png)

## Render Output Unit

![ROP](/assets/snip-images/2023-04-26_115640.png)

## Reference

- [vortexgpgpu website](https://vortex.cc.gatech.edu/)
- [vortexgpgpu github](https://github.com/vortexgpgpu/vortex)
