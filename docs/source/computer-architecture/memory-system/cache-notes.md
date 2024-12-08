---
layout: default
title: Cache notes
permalink: /memory-system/cache/
parent: Memory-system
nav_order: 2
---

# Cache Notes

|GPU                   |Cache Capacity          |
|:--                   |:--                     |
|Nvidia RTX 4090       |L2: 72 MB               |
|AMD Radeon RX 6900 XT |L2: 4 MB IC: 128 MB     |
|AMD Radeon RX 7900 XTX|L2: 6 MB IC: 96 MB      |

- Ada has enough L2 to handle every SM saving its register contents, with capacity to spare.[^1]

> 可认为线程栈是存在L2中

[^1]: <https://chipsandcheese.com/2023/05/16/shader-execution-reordering-nvidia-tackles-divergence/?utm_source=mailpoet&utm_medium=email&utm_campaign=new-post-from-chips-and-cheese>
