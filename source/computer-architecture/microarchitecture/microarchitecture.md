---
layout: default
title: Mircoarchitecture
permalink: /microarchitecture/
nav_order: 2
has_children: true
has_toc: true
---

# Microarchitecture

## SP

## 模拟器中Latency的处理逻辑

1. 通过配置文件来配置每种指令的操作Latency,以INT为例

    ```config
    # Instruction latencies and initiation intervals
    # "ADD,MAX,MUL,MAD,DIV"
    # All Div operations are executed on SFU unit
    -ptx_opcode_latency_int 3,3,3,3,3,3
    -ptx_opcode_initiation_int 3,3,3,3,3,3
    ```

2. 在解析指令的时候，将配置文件中对应的Latency配置到每条指令中

   ```c++
   ptx_instruction::set_opcode_and_latency()
   ...
    case B32_TYPE:
    case U32_TYPE:
    case S32_TYPE:
    default:  // Use int settings for default
        latency = int_latency[1];
        initiation_interval = int_init[1];
        op = INTP_OP;
   ...
   ```
