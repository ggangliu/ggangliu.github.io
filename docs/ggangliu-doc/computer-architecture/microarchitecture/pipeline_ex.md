# Pipeline EX

## Execution

## 当前EX的操作大致如下

1. 遍历所有的ALU单元，执行每个单元的cycle()
   1. 除了ldst，其所有alu的cycle()中，都是主要将前一阶段流水线寄存器中的指令传递给下一阶段
   2. ldst
   3. scheduler
2. 从前一阶段RF的流水线寄存器中取出指令
3. 判断当前取出的指令能否发送给下一阶段EX

## 重构点

1. 调度器可能的挪到IS阶段
   1. 同一个warp只发送一条指令
2. 每个阶段自己完成流水线寄存器从前一阶段到下一阶段的搬移
3. EX阶段进行指令的执行 func_exec_inst(warp_inst_t &inst)
4. 非store和FE阶段指令均在WB阶段完成寄存器回写

### 非store和FE阶段指令均在WB阶段完成寄存器回写

1. ldst_unit::writeback()
2. ldst_unit::L1_latency_queue_cycle()
3. ldst_unit::cycle()
4. ldst_unit::cycle()

LD/ST unit  0 = bubble
LD/ST next wb = bubble
Last LD/ST writeback @ 0 + 0 (gpu_sim_cycle+gpu_tot_sim_cycle)
Pending register writes:
Cache L1C_000:
MSHR contents

L1T_000 (texture cache) state:
fragment fifo entries  = 0 / 512
reorder buffer entries = 0 / 128
request fifo entries   = 0 / 8
Cache L1D_000:
MSHR contents

LD/ST response FIFO (occupancy = 0):

### Store指令的后处理

1. 该warp进入pending状态，在FE阶段不被调度，直到变为非pending状态
   1. 在L1D拿到该warp指令要取的数据后，该warp的pending状态置为false
2. 该warp的next_pc设置为当前pc

### Load指令

1. 如果处于Pending状态，则查询是否所有warp都处于Pending状态，
   1. 如果否，则将该指令换出
   2. 如果是，则stall，等待该指令需要的数据返回
2. FE阶段判断当前warp是否Pending状态
   1. 如果否，则该warp中取指
   2. 如果是，则跳过该warp
3. IS阶段判断将要发射的warp是否处于Pending状态，
   1. 如果否，继续发射
   2. 如果是，则从流水线清除，且不发射

如果pending状态的load指令的数据已返回，那么该如何处理？

1. 立即调度已返回的指令
2. 不处理，等待FE正常调度

### LDST单元

1. writeback()有需要进入WB阶段的指令在这里处理
2. EX阶段的sub_pipeline
3. 从response_fifo取出mem_fetch,然后m_L1D->fill(mem_fetch)
4. m_L1D->cycle() 处理m_miss_queue
5. L1_latency_queue_cycle()处理l1_latency_queue队列，当前所有load指令都配置了1个Cycle，也就是所有load指令都会先进入l1_latency_queue队列。该Cycle用来处理其中的mem_fetch请求，如果在m_L1D中命中，load指令继续执行
6. memory_cycle() 处理mem_fetch请求，会将请求放入l1_latency_queue
   1. process_memory_access_queue_l1cache（）

在cache命中的情况下m_pending_writes减一