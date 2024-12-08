# first ISA

## Instruction format

- R-type

|0-5   |6-8    |9-13 |14-18 |19-23  |
|:---  |:---   |:--- |:---  |:---   |
|Opcode|d_type |ra   |rb    |rd     |

- I-type

|0-5   |6-8    |9-13 |14-18 |19-31  |
|:---  |:---   |:--- |:---  |:---   |
|Opcode|d_type |ra   |rd    |imm    |

-B-type

|0-5   |6-8    |9-13 |14-18 |19-31  |
|:---  |:---   |:--- |:---  |:---   |
|Opcode|d_type |ra   |rd    |imm    |

## Data type supported

d_type: i8, i16, i32, f8, f16, f32

## Instruction list

|Type  |Assembly |Binary |Comments |
|:---  |:---     |:---   |:---     |
|R-type|add.i32 ra, rb, rd   | | |
|I-type|addi.i32 ra, imm, rd | |解决数据初始化 |
|R-type|madd.i32 ra, rb, rd  | |乘加运算 |
|I-type|ld.i32 ra, imm, rd   | |加载数据到寄存器，用imm可以解决数组偏移 |
|I-type|st.i32 ra, imm, rd   | |存储数据到memory，用imm可以解决数组偏移 |
|R-type|beq ra, rb, rd | | |
|I-type|jr imm, rd     | | |
