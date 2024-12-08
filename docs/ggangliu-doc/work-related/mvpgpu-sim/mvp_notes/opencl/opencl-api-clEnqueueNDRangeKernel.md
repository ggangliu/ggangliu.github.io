
# clEnqueueNDRangeKernel

## 函数定义

cl_int clEnqueueNDRangeKernel (
    cl_command_queue command_queue,
    cl_kernel kernel,
    **表示有几维数据**
    cl_uint work_dim, 
    const size_t *global_work_offset,
    **describe the number of global work-items in work_dim dimensions that will execute the kernel function**
    const size_t*global_work_size,
    **describe the number of work-items that make up a work-group**
    const size_t *local_work_size,
    cl_uint num_events_in_wait_list,
    const cl_event*event_wait_list,
    cl_event *event
)

根据MVPGPU-SIM中的代码实现，要求其参数中的 global_work_size % local_work_size == 0

在支持图形处理的时候，顶点和像素的个数是不可控的，因此需要能够支持任意数量线程的运行，也可以实际按照cta size运行线程，只不过线程id大于count的线程会进入else分支

_cl_V0Zo2b.s:67
```
PC=0x008 (./tempfiles/_cl_01_opencl_arithmetic.s:15) st.w$ra, 52($sp) opcode: add operand name: $sp operand name: $sp operand value: -56 
PC=0x010 (./tempfiles/_cl_01_opencl_arithmetic.s:16) st.w$6, 32($sp) opcode: st operand name: $ra operand value: 52 operand name: $sp 
PC=0x018 (./tempfiles/_cl_01_opencl_arithmetic.s:17) st.w$5, 36($sp) opcode: st operand name: $6 operand value: 32 operand name: $sp 
PC=0x020 (./tempfiles/_cl_01_opencl_arithmetic.s:18) st.w$4, 40($sp) opcode: st operand name: $5 operand value: 36 operand name: $sp 
PC=0x028 (./tempfiles/_cl_01_opencl_arithmetic.s:19) add.si$4, $zero, 0 opcode: st operand name: $4 operand value: 40 operand name: $sp 
PC=0x030 (./tempfiles/_cl_01_opencl_arithmetic.s:20) jplnk_Z13get_global_idj opcode: add operand name: $4 operand name: $zero operand value: 0 
PC=0x038 (./tempfiles/_cl_01_opencl_arithmetic.s:21) ld.w$3, 32($sp) opcode: jplink operand name: _Z13get_global_idj 
PC=0x040 (./tempfiles/_cl_01_opencl_arithmetic.s:22) setlt.u$3, $2, $3 opcode: ld operand name: $3 operand value: 32 operand name: $sp 
PC=0x048 (./tempfiles/_cl_01_opencl_arithmetic.s:23) beq$3, $zero, .LBB0_2 opcode: setlt operand name: $3 operand name: $2 operand name: $3 
PC=0x050 (./tempfiles/_cl_01_opencl_arithmetic.s:24) jp.LBB0_1 opcode: beq operand name: $3 operand name: $zero operand name: .LBB0_2 
PC=0x058 (./tempfiles/_cl_01_opencl_arithmetic.s:25) .LBB0_1:                                # %if.then opcode: jp operand name: .LBB0_1 
PC=0x060 (./tempfiles/_cl_01_opencl_arithmetic.s:27) ld.w$3, 40($sp) opcode: sfll operand name: $2 operand name: $2 operand value: 2 
PC=0x068 (./tempfiles/_cl_01_opencl_arithmetic.s:28) add$3, $3, $2 opcode: ld operand name: $3 operand value: 40 operand name: $sp 
PC=0x070 (./tempfiles/_cl_01_opencl_arithmetic.s:29) ld.w$3, 0($3) opcode: add operand name: $3 operand name: $3 operand name: $2 
PC=0x078 (./tempfiles/_cl_01_opencl_arithmetic.s:30) fmul$4, $3, $3 opcode: ld operand name: $3 operand value: 0 operand name: $3 
PC=0x080 (./tempfiles/_cl_01_opencl_arithmetic.s:31) fadd$3, $3, $3 opcode: fmul operand name: $4 operand name: $3 operand name: $3 
PC=0x088 (./tempfiles/_cl_01_opencl_arithmetic.s:32) fsub$3, $3, $4 opcode: fadd operand name: $3 operand name: $3 operand name: $3 
PC=0x090 (./tempfiles/_cl_01_opencl_arithmetic.s:33) fcvt$3, $3 opcode: fsub operand name: $3 operand name: $3 operand name: $4 
PC=0x098 (./tempfiles/_cl_01_opencl_arithmetic.s:34) fcvt$4, $4 opcode: fcvt operand name: $3 operand name: $3 
PC=0x0a0 (./tempfiles/_cl_01_opencl_arithmetic.s:35) sub$5, $4, $3 opcode: fcvt operand name: $4 operand name: $4 
PC=0x0a8 (./tempfiles/_cl_01_opencl_arithmetic.s:36) add$3, $3, $4 opcode: sub operand name: $5 operand name: $4 operand name: $3 
PC=0x0b0 (./tempfiles/_cl_01_opencl_arithmetic.s:37) mul.s$3, $3, $5 opcode: add operand name: $3 operand name: $3 operand name: $4 
PC=0x0b8 (./tempfiles/_cl_01_opencl_arithmetic.s:38) ld.w$4, 36($sp) opcode: mul operand name: $3 operand name: $3 operand name: $5 
PC=0x0c0 (./tempfiles/_cl_01_opencl_arithmetic.s:39) add$2, $4, $2 opcode: ld operand name: $4 operand value: 36 operand name: $sp 
PC=0x0c8 (./tempfiles/_cl_01_opencl_arithmetic.s:40) st.w$3, 0($2) opcode: add operand name: $2 operand name: $4 operand name: $2 
PC=0x0d0 (./tempfiles/_cl_01_opencl_arithmetic.s:41) .LBB0_2:                                # %if.end opcode: st operand name: $3 operand value: 0 operand name: $2 
PC=0x0d8 (./tempfiles/_cl_01_opencl_arithmetic.s:43) add.si$sp, $sp, 56 opcode: ld operand name: $ra operand value: 52 operand name: $sp 
PC=0x0e0 (./tempfiles/_cl_01_opencl_arithmetic.s:44) jr$ra opcode: add operand name: $sp operand name: $sp operand value: 56 
PC=0x0e8 (./tempfiles/_cl_01_opencl_arithmetic.s:45) .setmacro opcode: jr operand name: $ra 
```

31 jr $ra

224 PC=0x0e0 (./tempfiles/_cl_01_opencl_arithmetic.s:44) jr$ra opcode: add operand name: $sp operand name: $sp operand value: 56

## CTA ID

一个SP上运行一个cta
每个cta有64个线程

CTA: “cooperative thread array” is a PTX point of view of a “CUDA block”.

- kernel
- grid
  - cta/blocks
    - warps
      - threads

每个cta有16个warp
每个warp有4个线程

warp_per_cta    16
thread_per_warp 4

### ptx_sim_init_thread的流程

```c++

dim3 GridDim; (1, 1, 1)
GridDim.x = global_work_size[0]/_local_size[0] < 1 ? 1 : global_work_size[0]/_local_size[0];
GridDim.y = (work_dim < 2)?1:(global_work_size[1]/_local_size[1]);
GridDim.z = (work_dim < 3)?1:(global_work_size[2]/_local_size[2]);
dim3 BlockDim;(64, 1, 1)
BlockDim.x = _local_size[0];
BlockDim.y = (work_dim < 2)?1:_local_size[1];
BlockDim.z = (work_dim < 3)?1:_local_size[2];


issue_block2core(kernel)
{

  kernel.inc_running(); 
  int cta_size = kernel.threads_per_cta();

  init_warps(free_cta_hw_id, start_thread, end_thread, ctaid, cta_size, kernel);
}

ptx_sim_init_thread()
{
  while (m_next_tid.z < m_block_dim.z && m_next_tid.y < m_block_dim.y && m_next_tid.x < m_block_dim.x) //block_dim
  {
    ctaid3d = m_next_cta;
    new_tid = m_next_tid.x + m_block_dim.x * m_next_tid.y + m_block_dim.x * _block_dim.y * m_next_tid.z;
    tid3d = m_next_tid;
    //m_next_tid从x开始加1，如果大于block_dim的话，y开始+1，以此类推
    increment_x_then_y_then_z(m_next_tid, m_block_dim);
    new_tid += tid;
    //新建thread
    ptx_thread_info *thd = new ptx_thread_info(kernel);
    //新建warp
    ptx_warp_lookup[hw_warp_id] = warp_info;
    thd->m_warp_info = warp_info;

    thd->set_info(kernel.entry());
    thd->set_nctaid(kernel.get_grid_dim()); //设置gridDim (1,1,1)
    thd->set_ntid(kernel.get_cta_dim());    //设置blockDim (64,1,1)
    thd->set_ctaid(ctaid3d); //m_next_cta
    thd->set_tid(tid3d); //m_next_tid

    ctaid = m_next_cta.x + m_grid_dim.x * m_next_cta.y +
            m_grid_dim.x * m_grid_dim.y * m_next_cta.z;
    thd_id = ctaid * kernel.threads_per_cta() + new_tid;
    thd->set_tid_to_reg(thd_id);        

    thd->m_cta_info = cta_info;
    cta_info->add_thread(thd);
  }

  increment_x_then_y_then_z(m_next_cta, m_grid_dim);
  m_next_tid.x = 0;
  m_next_tid.y = 0;
  m_next_tid.z = 0;

}


```

```c++
dim3 **m_grid_dim**; 初始化为gridDim (1,1,1)
dim3 m_block_dim;    初始化为blockDim (64,1,1)
dim3 **m_next_cta**; 初始化为0
dim3 m_next_tid;     初始化为0

//每个线程有一个状态
m_threadState[i].m_active = true;

//获取下一个cta id
dim3 ctaid3d = kernel.get_next_cta_id();  
//获取下一个线程id  m_next_tid * m_block_dim
unsigned new_tid = kernel.get_next_thread_id();
//获取下一个线程id的3d形式 m_next_tid
dim3 tid3d = kernel.get_next_thread_id_3d();
//m_next_tid从x开始加1，如果大于block_dim的话，y开始+1，以此类推
kernel.increment_thread_id();

new_tid += tid; //以传入的tid为基准
ptx_thread_info *thd = new ptx_thread_info(kernel);

thd->set_nctaid(kernel.get_grid_dim());
thd->set_ntid(kernel.get_cta_dim());
thd->set_ctaid(ctaid3d);
thd->set_tid(tid3d);

unsigned ctaid = kernel.get_next_cta_id_single();
unsigned int thd_id = ctaid * kernel.threads_per_cta() + new_tid;
thd->set_tid_to_reg(thd_id);

unsigned get_next_thread_id() const {
return m_next_tid.x + m_block_dim.x * m_next_tid.y +
        m_block_dim.x * m_block_dim.y * m_next_tid.z;
}

dim3 get_next_thread_id_3d() const { return m_next_tid; }

dim3 get_next_cta_id() const { return m_next_cta; }

void increment_thread_id() {
    increment_x_then_y_then_z(m_next_tid, m_block_dim);
}

bool **more_threads_in_cta()** const {
  return m_next_tid.z < m_block_dim.z && m_next_tid.y < m_block_dim.y &&
          m_next_tid.x < m_block_dim.x;
}

void increment_x_then_y_then_z(dim3 &i, const dim3 &bound) {
  i.x++;
  if (i.x >= bound.x) {
    i.x = 0;
    i.y++;
    if (i.y >= bound.y) {
      i.y = 0;
      if (i.z < bound.z) i.z++;
    }
  }
}
```
