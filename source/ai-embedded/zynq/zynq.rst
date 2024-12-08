=======
ZYNQ
=======

基于ZYNQ做端侧的AI加速。

How to do
===========

1. 通过寄存器传递指令
#. 通过PS和PL之间的AXI接口传递数据
#. FPGA实现对应的AI加速单元

.. list-table:: 
    :widths: 15 15
    :header-rows: 1

    * - Pros
      - Cons

    * - 灵活可变，可以根据需求改变加速单元
      - PS端需要实现相应的软件栈支持使用FPGA加速

Software Stack
===============

Adding Pytorch support and define a custom backend.


.. toctree:: 
    :maxdepth: 1

    zynq_7010