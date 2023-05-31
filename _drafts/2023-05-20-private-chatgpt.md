---
layout: post
title: "Offline Private ChatGPT"
tags: software
---

本项目旨在利用**开源模型**进行**离线私有部署**

## 想要解决的问题

- 畜牧行业的知识问答
  - 问题解答
  - 能否支持图像识别，比如拍一张牛的照片
- 投资人信息管理
- 细分行业的信息检索和管理

<https://github.com/ggangliu/langchain-ChatGLM.git>
<https://github.com/imClumsyPanda/langchain-ChatGLM.git>

## 项目基本原理

加载文件 -> 读取文本 -> 文本分割 -> 文本向量化 -> 问句向量化 -> 在文本向量中匹配出与问句向量最相似的top k个 -> 匹配出的文本作为上下文和问题一起添加到prompt中 -> 提交给LLM生成回答
![基本原理](/assets/snip-images/langchain+chatglm.png)
从文本处理的角度来看，流程如下：
![文本流程](/assets/snip-images/langchain+chatglm2.png)

## 硬件要求

- ChatGLM-6B模型硬件需求
  模型文件下载至本地需要 15 GB 存储空间
  |量化等级	|最低 GPU 显存（推理）|最低 GPU 显存（高效参数微调）|
  |:--|:--|:--|
  |FP16（无量化）|13 GB|14 GB|
  |INT8         |8  GB|9  GB|
  |INT4         |6  GB|7  GB|
- MOSS 模型硬件需求
  模型文件下载至本地需要 70 GB 存储空间
  |量化等级	|最低 GPU 显存（推理）|最低 GPU 显存（高效参数微调）|
  |:--|:--|:--|
  |FP16（无量化）|	68 GB|	- |
  |INT8	         | 20 GB|   - |
- Embedding模型硬件需求
  本项目中默认选用的 Embedding 模型 [GanymedeNil/text2vec-large-chinese](https://huggingface.co/GanymedeNil/text2vec-large-chinese/tree/main) 约占用显存 3GB，也可修改为在 CPU 中运行

### My GPU

[GeForce MX150](https://www.nvidia.com/en-us/geforce/gaming-laptops/geforce-mx150/specifications/)
![](/assets/snip-images/2023-05-20_235413.png)

## 部署

### 开发部署

Python 3.8 - 3.10，CUDA 11.7 

## 训练

## 推理

 
## 相关概念

[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)
:  An Open Bilingual Dialogue Language Model | 开源双语对话语言模型

    ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型，基于 General Language Model (GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。 ChatGLM-6B 使用了和 ChatGPT 相似的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答


## Reference

1. [基于本地知识的 ChatGLM 应用实现](https://www.heywhale.com/mw/project/643977aa446c45f4592a1e59)
