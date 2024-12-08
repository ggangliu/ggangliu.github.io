# Register Renaming

## Physical Register

处理器中实际存在的寄存器个数要多于指令集中定义的通用寄存器的个数,这些在处理器内部实际存在的寄存器称为物理寄存器(Physical Register)

## Logical Register / Architecture Register

指令集中定义的寄存器称为逻辑寄存器(Logical Register,或Architecture Register)

往往在设计中，物理寄存器的数量要多于逻辑寄存器的数量，这样rename才能真正发挥其作用

## 物理寄存器如何映射到逻辑寄存器

处理器在进行寄存器重命名的时候，会动态的将逻辑寄存器映射到物理寄存器，这样可以解决WAW和WAR的相关性
