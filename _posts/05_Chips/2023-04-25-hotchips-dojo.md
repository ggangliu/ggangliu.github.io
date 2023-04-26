---
layout: post
title: Hotchip Dojo System
tags: other-arch
comments: false
---

Dojo Super-Compute System Scaling for ML Training

## Flexible Building Block

![Scale with multiple Tiles](/assets/snip-images/2023-04-26_092301.png)

## V1 Dojo Interface Processor

![DIP](/assets/snip-images/2023-04-26_093656.png)

- 32GB High-Bandwidth Memory
  800 GB/s Total Memory Bandwidth
- 900 GB/s TTP Interface
  Provideds full DRAM bandwidth to Training Tile
- 32 GB/s Gen4 PCIe Interface
- 160GB total DRAM per Tile edge
  Shared memory for training tiles
- 5 DIP Cards provide Max Bandwidth
  4.5 TB/s aggregate bandwidth to DRAM over TTP
- 80 Lanes PCIe Gen4 Interface
  Provide standard connectivity to hosts

![DIP](/assets/snip-images/2023-04-26_093640.png)

## Remote DMA Topology

![RDT](/assets/snip-images/2023-04-26_094059.png)

## V1 Dojo Training Matrix

![DTM](/assets/snip-images/2023-04-26_094634.png)

## Dissaggregated Scalable System

![DSS](/assets/snip-images/2023-04-26_094911.png)

## Dojo Supercomputer for ML Training

![ML](/assets/snip-images/2023-04-26_101611.png)
