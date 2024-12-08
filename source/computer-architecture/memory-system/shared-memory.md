
# Shared Memory

根据此图，可以理解shared memory的设计会影响性能。如果每个线程都能有一个唯一对应的bank来存储其所需数据，性能将会大大提升。

![shared memory bank conflicts](../../_images/2023-08-29_103612.png)
