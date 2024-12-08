# MVP v3.0 Performance Evaluation Plan

``` mermaid
gantt
dateFormat YYYY-MM-DD
axisFormat WK%W
inclusiveEndDates
todayMarker stroke-width:3px,stroke:#0f0,opacity:0.5
title MVP v3.0 Performance Evaluation Plan

section 第一阶段
    %% 着力在整体框架及完整性，细节不追求完全一致
    GPC support             :t1, 2023-07-13, 2w
    L1I Cache               :t2, after t1, 3w
    L1D Cache               :t3, after t2, 3w
    Local Memory            :t4, after t3, 2w
    L2 Cahce                :t5, after t4, 3w
    DRAM Analysis           :t6, after t5, 3w
    Register File           :t7, after t6, 2w
    Refine MVP v3.0 perf report   :t8, after t7, 1w
    Release analysis report for MVP v3.0 :milestone, crit, t9, after t8, 0d
```

GPC support
: Criteria: 根据配置文件创建多个GPC，每个GPC包含多个TPC

L1I Cache
: Criteria: 分析评估L1指令缓存的大小，给出具体建议值

L1D Cache
: Criteria: 分析评估L1数据缓存的大小，给出具体建议值
