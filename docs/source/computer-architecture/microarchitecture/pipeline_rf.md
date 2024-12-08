# Pipeline RF

## Register File

首先在配置文件中定义了寄存器文件的port数量，即reg_file_port_throughput。

1. 通过dipatch_ready_cu()把ready的CU中的指令传递给RF_EX流水线寄存器，并重置CU及源操作数
2. allocate_reads()处理没有冲突的读请求
   1. m_arbiter->allocate_reads()根据m_queue来确定bank和oc之间的关系_request[bank_id][oc_id]
   2. 如果对应的bank分配为write，则获得优先权，通过_inmatch[bank_id]=0来标记
   3. 除了is_write的bank，其他跟request匹配的bank对应的操作数从m_queue队列中取出并放入result中
   4. m_arbiter.allocate_for_read()为分read请求分配bank
3. allocate_cu()
   1. cu->allocate()
   2. m_arbiter.add_read_requests(cu)将read请求放入m_queue中