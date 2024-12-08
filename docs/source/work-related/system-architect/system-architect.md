---
layout: default
title: System Architect
permalink: /system-architect/
nav_order: 4
has_children: false
has_toc: true
---

数据库设计：

1. 需求分析
2. 概念结构设计
   1. E-R图合并，E-R图即实体-联系图
3. 逻辑结构设计
4. 物理设计
5. 数据库实施阶段
6. 数据库运行和维护阶段

函数依赖：

1. 部分函数依赖
2. 传递函数依赖

外键：其他表的主键
主属性：候选键内的属性为主属性，其他为非主属性

范式：

1. 第一范式1NF:关系中的每一个分量必须是一个不可分的数据项
2. 第二范式2NF:消除部分函数依赖（如果候选键是单属性则不存在部分函数依赖）
3. 第三范式3NF:消除传递依赖
