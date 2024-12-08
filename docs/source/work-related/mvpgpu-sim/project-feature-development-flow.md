---
layout: default
title: Project or Feature Development Flow
permalink: /Home/Project or Feature Development Flow/
parent: Home
nav_order: 4
---

# Project/Feature Development Flow

## 1. Project Development Flow

## 2. Feature Development Flow

特性需求分析，并给出实现Feature的具体方法(Approach)，进行必要评审后，开始Coding完成Feature，Coding完成后及时进行Code review，避免代码测试稳定后再Review，引入新的修改而反复测试。如发现前期Approach有缺陷，可及时进行必要重构，避免技术欠债。

### 2.1 Feature Requirement Clarification Meeting

系统或者需求导入者，需要召开特性需求澄清会议，进行特性需求澄清

>注意：针对复杂Feature，Feature Owner可召开特性需求反串讲会议，将对特性需求的理解进行反向串讲给系统工程师或者需求到入者，以达到充分正确理解特性需求的目的

### 2.2 Approach Review Meeting

1. 评审特性开发方案，针对评审过程中的意见进行答复、修改或进一步讨论
2. 关键评审人达成一致后，开始Coding

>注意: 如有必要，也可在特性的分析评审过程中编写必要的demo代码辅助理解特性或阐述方案

### 2.3 Code Review

- Offline meeting
代码改动较大，或认为有必要的，采用线下召开code review meeting的形式进行完成code review

- Online gerrit review
代码改动较小的可采用线上code review
