---
layout: default
title: MVP uarch notes
permalink: /microarchitecture/uarch/
parent: Mircoarchitecture
nav_order: 1
---

# MVP uarch notes

SP作为MVP微架构中的最小单元，在模拟器中通过stream_processor::cycle()来串连流水线的各个阶段。

## Fetch

### FE阶段一次取多少条指令？

MVP fetchs 4 instructions from the instruction cache concurrently for the four horizontal launched threads provided that the threads is not stalled and no bank conflict, and do the same for next group of horizontal threads at next cycle.

If the PCs of the horizontal threads are the same, the fetch can be done using one access. Otherwise the fetch will use 2/3/4 times access with or without bank conflict.

scheduler_unit::cycle()

mvp_stream_processor::checkExecutionStatusAndUpdate()

### stream_processor::fetch()

### valid

```c++
warp(warp_id).set_next_pc(pc);
warp(warp_id).ibuffer_flush();
```

warp_inst_complete() 记录SP中完成的指令数量

 8： 5010
12： 5011
16:  5012
20:  5012

微架构的分析中发现如下个现象

1. 一个cycle可以完成4、8、12条指令
   - 4条指令意味着只有writeback或者execute阶段完成指令
   - 12条指令，发现分别是add/ld/jp
2. 有的cycle没有指令完成

-l2_ideal 1

memory partition latency config
-gpgpu_l2_rop_latency 160
-dram_latency 100

## Issue



## Register File



## Execution

EX阶段根据操作的Latency，建立自己的pipeline_depth及pipeline_reg。而在SP中也有m_pipeline_reg与EX阶段自身的重名。将会重命名EX的为m_ex_pipeline_reg以免混淆。在创建ALU的时候，会根据最大的Latency来创建EX阶段的流水级数m_ex_pipeline_depth。在EX执行的过程中，EX的cycle()会将m_ex_pipeline_reg[0]中指令放入m_result_port，m_result_port中的指令会在下一个cycle被传递给WB阶段。而在EX内部，流水是从最大往最小一次发送。在指令被放入EX内部流水之前，先经过initiation_interval个cycle的delay，之后放入EX流水线的（latency-initiation_interval）位置，然后再在每个cycle中依次往前传递，直到流水完成，进入WB阶段，EX完成使命。

SP中的定义如下：

```c++
 std::vector<register_set> m_pipeline_reg;
```

EX中的定义如下：

```c++
 warp_inst_t **m_ex_pipeline_reg;
```

### LDST Unit

在ldst的cycle中会完成下面的工作：

1. load指令的write_back
2. operand collector的step
3. subpipeline的执行
4. 处理cache的response_fifo，其中可能是某条load指令的响应
5. 执行各种cache的cycle
   1. L1D cache
6. 执行local memory的cycle
7. 如果stall，记录log
8. 如果未stall，则处理pending_write

## WriteBack

1. 根据warp_size和pipe_width[WB]计算max_committed_thread_instructions

2. 从m_pipeline_reg[EX_WB]得到要执行的指令 warp_inst_t **preg = m_pipeline_reg[EX_WB].get_ready()

3. 完成writeback操作 m_operand_collector.writeback(*pipe_reg);

4. 完成指令后的资源释放等工作

   ```c++
    unsigned warp_id = pipe_reg->warp_id();
    m_scoreboard->releaseRegisters(pipe_reg);
    m_warp[warp_id]->dec_inst_in_pipeline();
    warp_inst_complete(*pipe_reg);
    m_gpu->gpu_sim_insn_last_update_sid = m_sp_id;
    m_gpu->gpu_sim_insn_last_update = m_gpu->gpu_sim_cycle;
    m_last_inst_gpu_sim_cycle = m_gpu->gpu_sim_cycle;
    m_last_inst_gpu_tot_sim_cycle = m_gpu->gpu_tot_sim_cycle;
    pipe_reg->clear();
   ```
