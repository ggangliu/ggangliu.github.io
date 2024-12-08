# SMD Development Plan Overview

``` mermaid
gantt
dateFormat YYYY-MM-DD
inclusiveEndDates
todayMarker stroke-width:3px,stroke:#0f0,opacity:0.5
title SMD Development Plan

section 第一阶段
    %% This is comments
    libdrm.so接口文档v1.0                 :crit, des1, 2023-07-11, 5d
    确定最小和最典型CL/GL测试用例           :des2, after des1, 3d
    创建libdrm.so编译构建工程及配套的头文件 :done, des3, 2023-07-11, 5d
    环境变量配置脚本                       :des4, after des3, 2d
    实现“任务1”中V1.0提供的所有接口定义     :des5, after des1, 5d
    调试                                  :des6, after des5, 5d
    Release libdrm.so v1.0                :milestone, crit, des7, after des6, 0d

section 第二阶段
    %% This is comments
    libdrm.so接口文档v2.0                 :crit, des8, after des1, 10d
    实现“任务1”中V2.0提供的所有接口定义     :des9, after des8, 3d
    跑通一个最小最简单OpenCL用例            :des10, after des9, 6d
    调试                                  :des11, after des10, 6d
    Release libdrm.so v2.0                :milestone, crit, des12, after des11, 0d   

section 第三阶段
    %% This is comments
    libdrm.so接口文档v3.0                 :crit, des13, after des8, 15d
    实现“任务1”中V3.0提供的所有接口定义     :des14, after des13, 20d
    跑通一个最典型的OpenCL/GL用例          :des15, after des14, 5d
    跑通所有已支持的OpenCL/GL用例          :des16, after des15, 10d
    调试                                  :des17, after des16, 5d
    Release libdrm.so v3.0                :milestone, crit, after des17, 0d
```
