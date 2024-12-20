# GPC debugging

ldst_unit::init
mem_fetch::mem_fetch
shader_core_mem_fetch_allocator

## deadlock after added GPC

## scoreboard

reserveRegister
: 在issue阶段的issue_warp中执行指令后进行reserve

releaseRegister
: ldst_unit::cycle()中指令完成后和stream_processor::writeback()中

如下为正常场景，每个cycle处理一个warp指令

``` log
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 3 - scheduler_unit::cycle()
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 3 - Testing (warp_id 3, dynamic_warp_id 3)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 3 - Warp (warp_id 3, dynamic_warp_id 3) has valid instruction ( PC=0x000 (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:13) sub$zero, $zero, $zero opcode: sub operand name: $zero operand name: $zero operand name: $zero 
)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 3 - Warp (warp_id 3, dynamic_warp_id 3) passes scoreboard
MVPGPU-Sim Cycle 5002: SCOREBOARD - Core 0 - Reserved Register - warp:3, reg: 1
MVPGPU-Sim Cycle 5002: SCOREBOARD - Core 0 - Reserved register - warp:3, reg: 1
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 3 - Warp (warp_id 3, dynamic_warp_id 3) issued 1 instructions
```

如下为异常场景，每个cycle处理了多个warp，可能由于ibffer_empty

``` log
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - scheduler_unit::cycle()
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Testing (warp_id 0, dynamic_warp_id 0)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Warp (warp_id 0, dynamic_warp_id 0) fails as ibuffer_empty
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Testing (warp_id 4, dynamic_warp_id 4)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Warp (warp_id 4, dynamic_warp_id 4) fails as ibuffer_empty
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Testing (warp_id 8, dynamic_warp_id 8)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Warp (warp_id 8, dynamic_warp_id 8) fails as ibuffer_empty
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Testing (warp_id 12, dynamic_warp_id 12)
MVPGPU-Sim Cycle 5002: WARP_SCHEDULER - Core 0 - Scheduler 0 - Warp (warp_id 12, dynamic_warp_id 12) fails as ibuffer_empty
```

## [现象]

jr指令只执行了256条，意味着还有3/4的线程没有执行结束

- SP中的变量m_not_completed
cycle()中用m_not_completed判断是否还有未完成的线程，没创建一个warp就加4，因为每个warp有4个线程
而m_not_completed减一的条件是m_warp[warp_id]->hardware_done()

- warp的变量n_completed
warp中记录完成线程数量：n_completed++，条件是m_thread[hw_thread_id]->is_done()

- warp初始化时的m_warp_id初始化，warp_id是否唯一 

### 执行到第18条指令后，从第19条指令开始只有256个线程继续执行第19条指令，其他线程都没有继续运行

``` log
execute thread: 5288 [thd=1][i=18] : ctaid=(0,0,0) tid=(0,0,0) icount=16 [pc=120] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:29 - ld.w$3, 0($3))  [0x41066e17]
execute thread: 5289 [thd=2][i=18] : ctaid=(0,0,0) tid=(1,0,0) icount=16 [pc=120] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:29 - ld.w$3, 0($3))  [0x407c67b3]
execute thread: 5290 [thd=3][i=18] : ctaid=(0,0,0) tid=(2,0,0) icount=16 [pc=120] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:29 - ld.w$3, 0($3))  [0x40fa977d]
execute thread: 5291 [thd=4][i=18] : ctaid=(0,0,0) tid=(3,0,0) icount=16 [pc=120] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:29 - ld.w$3, 0($3))  [0x40ff8035]

execute thread: 16384 [thd=1][i=19] : ctaid=(0,0,0) tid=(0,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x428d2edf]
execute thread: 16385 [thd=2][i=19] : ctaid=(0,0,0) tid=(1,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4178dc52]
execute thread: 16386 [thd=3][i=19] : ctaid=(0,0,0) tid=(2,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42754c3a]
execute thread: 16387 [thd=4][i=19] : ctaid=(0,0,0) tid=(3,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x427f00aa]

execute thread: 16388 [thd=65][i=19] : ctaid=(1,0,0) tid=(0,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40e38dd2]
execute thread: 16389 [thd=66][i=19] : ctaid=(1,0,0) tid=(1,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41e912af]
execute thread: 16390 [thd=67][i=19] : ctaid=(1,0,0) tid=(2,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41613f99]
execute thread: 16391 [thd=68][i=19] : ctaid=(1,0,0) tid=(3,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x426730f5]

execute thread: 16396 [thd=5][i=19] : ctaid=(0,0,0) tid=(4,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42a6385f]
execute thread: 16397 [thd=6][i=19] : ctaid=(0,0,0) tid=(5,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4079c517]
execute thread: 16398 [thd=7][i=19] : ctaid=(0,0,0) tid=(6,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4133cc82]
execute thread: 16399 [thd=8][i=19] : ctaid=(0,0,0) tid=(7,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x426c1218]

execute thread: 16400 [thd=513][i=19] : ctaid=(8,0,0) tid=(0,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41f3457c]
execute thread: 16401 [thd=514][i=19] : ctaid=(8,0,0) tid=(1,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42ae412c]
execute thread: 16402 [thd=515][i=19] : ctaid=(8,0,0) tid=(2,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41c38cf0]
execute thread: 16403 [thd=516][i=19] : ctaid=(8,0,0) tid=(3,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41f443f8]

execute thread: 16408 [thd=69][i=19] : ctaid=(1,0,0) tid=(4,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41d2276d]
execute thread: 16409 [thd=70][i=19] : ctaid=(1,0,0) tid=(5,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4232578e]
execute thread: 16410 [thd=71][i=19] : ctaid=(1,0,0) tid=(6,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41e21596]
execute thread: 16411 [thd=72][i=19] : ctaid=(1,0,0) tid=(7,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x3e1dff63]

execute thread: 16412 [thd=577][i=19] : ctaid=(9,0,0) tid=(0,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x421ee1f2]
execute thread: 16413 [thd=578][i=19] : ctaid=(9,0,0) tid=(1,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42aa933b]
execute thread: 16414 [thd=579][i=19] : ctaid=(9,0,0) tid=(2,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4259d240]
execute thread: 16415 [thd=580][i=19] : ctaid=(9,0,0) tid=(3,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41ab62c1]

execute thread: 16424 [thd=9][i=19] : ctaid=(0,0,0) tid=(8,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40f6e87c]
execute thread: 16425 [thd=10][i=19] : ctaid=(0,0,0) tid=(9,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41f58194]
execute thread: 16426 [thd=11][i=19] : ctaid=(0,0,0) tid=(10,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41b6538d]
execute thread: 16427 [thd=12][i=19] : ctaid=(0,0,0) tid=(11,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x421e3103]

execute thread: 16428 [thd=517][i=19] : ctaid=(8,0,0) tid=(4,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b06489]
execute thread: 16429 [thd=518][i=19] : ctaid=(8,0,0) tid=(5,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x427fc5f7]
execute thread: 16430 [thd=519][i=19] : ctaid=(8,0,0) tid=(6,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4284907a]
execute thread: 16431 [thd=520][i=19] : ctaid=(8,0,0) tid=(7,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x420d5eec]

execute thread: 16440 [thd=73][i=19] : ctaid=(1,0,0) tid=(8,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x419938aa]
execute thread: 16441 [thd=74][i=19] : ctaid=(1,0,0) tid=(9,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42ada9d0]
execute thread: 16442 [thd=75][i=19] : ctaid=(1,0,0) tid=(10,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42ad4808]
execute thread: 16443 [thd=76][i=19] : ctaid=(1,0,0) tid=(11,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x424fe8ae]

execute thread: 16444 [thd=581][i=19] : ctaid=(9,0,0) tid=(4,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4199de82]
execute thread: 16445 [thd=582][i=19] : ctaid=(9,0,0) tid=(5,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4290b311]
execute thread: 16446 [thd=583][i=19] : ctaid=(9,0,0) tid=(6,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b58359]
execute thread: 16447 [thd=584][i=19] : ctaid=(9,0,0) tid=(7,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b4161b]

execute thread: 16456 [thd=13][i=19] : ctaid=(0,0,0) tid=(12,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4154e889]
execute thread: 16457 [thd=14][i=19] : ctaid=(0,0,0) tid=(13,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41d2dd4a]
execute thread: 16458 [thd=15][i=19] : ctaid=(0,0,0) tid=(14,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b55929]
execute thread: 16459 [thd=16][i=19] : ctaid=(0,0,0) tid=(15,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42a7e1f8]

execute thread: 16460 [thd=521][i=19] : ctaid=(8,0,0) tid=(8,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x422cc3e5]
execute thread: 16461 [thd=522][i=19] : ctaid=(8,0,0) tid=(9,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42c61fd8]
execute thread: 16462 [thd=523][i=19] : ctaid=(8,0,0) tid=(10,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42af29e9]
execute thread: 16463 [thd=524][i=19] : ctaid=(8,0,0) tid=(11,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x412885ff]

execute thread: 16472 [thd=77][i=19] : ctaid=(1,0,0) tid=(12,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x410150ff]
execute thread: 16473 [thd=78][i=19] : ctaid=(1,0,0) tid=(13,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x425a2c57]
execute thread: 16474 [thd=79][i=19] : ctaid=(1,0,0) tid=(14,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4223d444]
execute thread: 16475 [thd=80][i=19] : ctaid=(1,0,0) tid=(15,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41488f8d]

execute thread: 16476 [thd=585][i=19] : ctaid=(9,0,0) tid=(8,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42a1abd1]
execute thread: 16477 [thd=586][i=19] : ctaid=(9,0,0) tid=(9,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x426b52f0]
execute thread: 16478 [thd=587][i=19] : ctaid=(9,0,0) tid=(10,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4132078d]
execute thread: 16479 [thd=588][i=19] : ctaid=(9,0,0) tid=(11,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41e67958]

execute thread: 16492 [thd=525][i=19] : ctaid=(8,0,0) tid=(12,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4298e224]
execute thread: 16493 [thd=526][i=19] : ctaid=(8,0,0) tid=(13,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x420ad79d]
execute thread: 16494 [thd=527][i=19] : ctaid=(8,0,0) tid=(14,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4222b362]
execute thread: 16495 [thd=528][i=19] : ctaid=(8,0,0) tid=(15,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4266a102]

execute thread: 16508 [thd=589][i=19] : ctaid=(9,0,0) tid=(12,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4099aa7b]
execute thread: 16509 [thd=590][i=19] : ctaid=(9,0,0) tid=(13,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41b671b3]
execute thread: 16510 [thd=591][i=19] : ctaid=(9,0,0) tid=(14,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b46e86]
execute thread: 16511 [thd=592][i=19] : ctaid=(9,0,0) tid=(15,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41add9bc]

execute thread: 16520 [thd=17][i=19] : ctaid=(0,0,0) tid=(16,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4221a6d9]
execute thread: 16521 [thd=18][i=19] : ctaid=(0,0,0) tid=(17,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x424dce55]
execute thread: 16522 [thd=19][i=19] : ctaid=(0,0,0) tid=(18,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40005407]
execute thread: 16523 [thd=20][i=19] : ctaid=(0,0,0) tid=(19,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42135d4f]

execute thread: 16536 [thd=81][i=19] : ctaid=(1,0,0) tid=(16,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x423d42e6]
execute thread: 16537 [thd=82][i=19] : ctaid=(1,0,0) tid=(17,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40304db3]
execute thread: 16538 [thd=83][i=19] : ctaid=(1,0,0) tid=(18,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x419af41f]
execute thread: 16539 [thd=84][i=19] : ctaid=(1,0,0) tid=(19,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x429ae810]

execute thread: 16556 [thd=529][i=19] : ctaid=(8,0,0) tid=(16,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x427082e8]
execute thread: 16557 [thd=530][i=19] : ctaid=(8,0,0) tid=(17,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x427cc0bb]
execute thread: 16558 [thd=531][i=19] : ctaid=(8,0,0) tid=(18,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40dcfa75]
execute thread: 16559 [thd=532][i=19] : ctaid=(8,0,0) tid=(19,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42121c06]

execute thread: 16572 [thd=593][i=19] : ctaid=(9,0,0) tid=(16,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x429c6751]
execute thread: 16573 [thd=594][i=19] : ctaid=(9,0,0) tid=(17,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42bb1ffc]
execute thread: 16574 [thd=595][i=19] : ctaid=(9,0,0) tid=(18,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40582049]
execute thread: 16575 [thd=596][i=19] : ctaid=(9,0,0) tid=(19,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41a7d6fc]

execute thread: 17024 [thd=21][i=19] : ctaid=(0,0,0) tid=(20,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x3cd9ab25]
execute thread: 17025 [thd=22][i=19] : ctaid=(0,0,0) tid=(21,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40bcc7de]
execute thread: 17026 [thd=23][i=19] : ctaid=(0,0,0) tid=(22,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x3ff10e5b]
execute thread: 17027 [thd=24][i=19] : ctaid=(0,0,0) tid=(23,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4281570d]

execute thread: 17040 [thd=85][i=19] : ctaid=(1,0,0) tid=(20,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x428983d1]
execute thread: 17041 [thd=86][i=19] : ctaid=(1,0,0) tid=(21,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x412e98a1]
execute thread: 17042 [thd=87][i=19] : ctaid=(1,0,0) tid=(22,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40a7c3b9]
execute thread: 17043 [thd=88][i=19] : ctaid=(1,0,0) tid=(23,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x429f9f74]

execute thread: 17056 [thd=25][i=19] : ctaid=(0,0,0) tid=(24,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x401d1bff]
execute thread: 17057 [thd=26][i=19] : ctaid=(0,0,0) tid=(25,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41809ae9]
execute thread: 17058 [thd=27][i=19] : ctaid=(0,0,0) tid=(26,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x3fd79f86]
execute thread: 17059 [thd=28][i=19] : ctaid=(0,0,0) tid=(27,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x3f978b33]

execute thread: 17060 [thd=533][i=19] : ctaid=(8,0,0) tid=(20,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41b12501]
execute thread: 17061 [thd=534][i=19] : ctaid=(8,0,0) tid=(21,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40326481]
execute thread: 17062 [thd=535][i=19] : ctaid=(8,0,0) tid=(22,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x427d1f39]
execute thread: 17063 [thd=536][i=19] : ctaid=(8,0,0) tid=(23,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4295acb2]

execute thread: 17072 [thd=89][i=19] : ctaid=(1,0,0) tid=(24,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41446753]
execute thread: 17073 [thd=90][i=19] : ctaid=(1,0,0) tid=(25,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x423c9b30]
execute thread: 17074 [thd=91][i=19] : ctaid=(1,0,0) tid=(26,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b6f75e]
execute thread: 17075 [thd=92][i=19] : ctaid=(1,0,0) tid=(27,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x420a9951]

execute thread: 17076 [thd=597][i=19] : ctaid=(9,0,0) tid=(20,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42737ff0]
execute thread: 17077 [thd=598][i=19] : ctaid=(9,0,0) tid=(21,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x426afa0d]
execute thread: 17078 [thd=599][i=19] : ctaid=(9,0,0) tid=(22,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42a3b9d6]
execute thread: 17079 [thd=600][i=19] : ctaid=(9,0,0) tid=(23,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40d4521c]

execute thread: 17088 [thd=29][i=19] : ctaid=(0,0,0) tid=(28,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42c791ec]
execute thread: 17089 [thd=30][i=19] : ctaid=(0,0,0) tid=(29,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40986f79]
execute thread: 17090 [thd=31][i=19] : ctaid=(0,0,0) tid=(30,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41d27acf]
execute thread: 17091 [thd=32][i=19] : ctaid=(0,0,0) tid=(31,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x428cd265]

execute thread: 17092 [thd=537][i=19] : ctaid=(8,0,0) tid=(24,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42986ee9]
execute thread: 17093 [thd=538][i=19] : ctaid=(8,0,0) tid=(25,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4230941f]
execute thread: 17094 [thd=539][i=19] : ctaid=(8,0,0) tid=(26,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41881d0f]
execute thread: 17095 [thd=540][i=19] : ctaid=(8,0,0) tid=(27,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4215cee4]

execute thread: 17104 [thd=93][i=19] : ctaid=(1,0,0) tid=(28,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x422cd1c7]
execute thread: 17105 [thd=94][i=19] : ctaid=(1,0,0) tid=(29,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4293770b]
execute thread: 17106 [thd=95][i=19] : ctaid=(1,0,0) tid=(30,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x419a9200]
execute thread: 17107 [thd=96][i=19] : ctaid=(1,0,0) tid=(31,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42aabe7a]

execute thread: 17108 [thd=601][i=19] : ctaid=(9,0,0) tid=(24,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4268057a]
execute thread: 17109 [thd=602][i=19] : ctaid=(9,0,0) tid=(25,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42b9ab13]
execute thread: 17110 [thd=603][i=19] : ctaid=(9,0,0) tid=(26,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x413031d1]
execute thread: 17111 [thd=604][i=19] : ctaid=(9,0,0) tid=(27,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x418186e5]

execute thread: 17124 [thd=541][i=19] : ctaid=(8,0,0) tid=(28,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x420e83f0]
execute thread: 17125 [thd=542][i=19] : ctaid=(8,0,0) tid=(29,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4226b874]
execute thread: 17126 [thd=543][i=19] : ctaid=(8,0,0) tid=(30,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41e808d5]
execute thread: 17127 [thd=544][i=19] : ctaid=(8,0,0) tid=(31,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x400cd589]

execute thread: 17140 [thd=605][i=19] : ctaid=(9,0,0) tid=(28,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41fb955c]
execute thread: 17141 [thd=606][i=19] : ctaid=(9,0,0) tid=(29,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x41f5ee23]
execute thread: 17142 [thd=607][i=19] : ctaid=(9,0,0) tid=(30,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x421ad627]
execute thread: 17143 [thd=608][i=19] : ctaid=(9,0,0) tid=(31,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x40698bc9]

execute thread: 18176 [thd=97][i=19] : ctaid=(1,0,0) tid=(32,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x417e00ba]
execute thread: 18177 [thd=98][i=19] : ctaid=(1,0,0) tid=(33,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x4284c4de]
execute thread: 18178 [thd=99][i=19] : ctaid=(1,0,0) tid=(34,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x423b4311]
execute thread: 18179 [thd=100][i=19] : ctaid=(1,0,0) tid=(35,0,0) icount=17 [pc=128] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:30 - fmul$4, $3, $3)  [0x42a5f958]

```


execute thread: 18132 [thd=85][i=33] : ctaid=(1,0,0) tid=(20,0,0) icount=30 [pc=232] (/home/user/liuyonggang/repo/mvpgpu-sim/tempfiles/_cl_01_opencl_arithmetic.s:44 - jr$ra)  [0x0]
