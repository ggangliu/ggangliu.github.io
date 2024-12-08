# Instruction Flow

## 指令的执行流程

1. gpu_micro_architecture::cycle()
2. graphics_process_cluster::core_cycle()
3. texture_process_cluster::core_cycle()
4. stream_multiprocessor::sp_cycle()
5. stream_processor::cycle()
6. scheduler_unit::cycle()
7. stream_processor::issue_warp(register_set &pipe_reg_set,
                                  const warp_inst_t *next_inst,
                                  const active_mask_t &active_mask,
                                  unsigned warp_id, unsigned sch_id)
8. mvp_stream_processor::func_exec_inst(warp_inst_t &inst)
9. core_t::execute_warp_inst_t(warp_inst_t &inst, unsigned warpId)
10. ptx_thread_info::ptx_exec_inst(warp_inst_t &inst, unsigned lane_id)
11. mvp_jr_impl(const ptx_instruction *pI, ptx_thread_info *thread)

## 指令的完成判断流程

目前看指令完成有两条主要路径，分别如下

### WB

1. gpu_micro_architecture::cycle()

2. graphics_process_cluster::core_cycle()

3. texture_process_cluster::core_cycle()

4. stream_multiprocessor::sp_cycle()

5. stream_processor::cycle()

6. stream_processor::writeback()
   1. max_committed_thread_instructions = m_sp_config->warp_size *  m_sp_config->pipe_widths[EX_WB];

   1. stream_processor::warp_inst_complete(const warp_inst_t &inst)

      1. warp_inst_t::completed(unsigned long long cycle)

### EX

1. gpu_micro_architecture::cycle()

2. graphics_process_cluster::core_cycle()

3. texture_process_cluster::core_cycle()

4. stream_multiprocessor::sp_cycle()

5. stream_processor::cycle()

6. stream_processor::execute()

   1. ldst_unit::writeback()
   2. ldst_unit::L1_latency_queue_cycle()
   3. ldst_unit::cycle()
   4. ldst_unit::cycle()

7. stream_processor::warp_inst_complete(const warp_inst_t &inst)

8. warp_inst_t::completed(unsigned long long cycle)

### 该函数用于打印代码对应指令的latency

gpu_ctx->stats->ptx_file_line_stats_write_file();

pInsn->get_source() 用于拿到汇编指令字符串
