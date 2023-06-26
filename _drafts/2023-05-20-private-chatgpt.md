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

## 可以参考的项目

- <https://github.com/ggangliu/langchain-ChatGLM.git>
- <https://github.com/ggangliu/privateGPT>

### langchain-ChatGLM 项目基本原理

加载文件 -> 读取文本 -> 文本分割 -> 文本向量化 -> 问句向量化 -> 在文本向量中匹配出与问句向量最相似的top k个 -> 匹配出的文本作为上下文和问题一起添加到prompt中 -> 提交给LLM生成回答
![基本原理](/assets/snip-images/langchain+chatglm.png)
从文本处理的角度来看，流程如下：
![文本流程](/assets/snip-images/langchain+chatglm2.png)

### privateGPT 项目基本原理

该项目允许你在问你自己文档问题的时候不需要联网。100%的私有，在任何一点上都没有数据泄露你的运行环境。你能够摄取文档并问问题。

#### Requirements

```bat
pip3 install -r requirements.txt
```

```bat
apt install python3.10
apt install python3-pip
```

#### 安装

```bat
cp example.env .env
python ingest.py
python privateGPT.py
```

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
![mx150](/assets/snip-images/2023-05-20_235413.png)

## Reference

1. [基于本地知识的 ChatGLM 应用实现](https://www.heywhale.com/mw/project/643977aa446c45f4592a1e59)
2. Error of privateGPT installing
  
    ``` bat
    RROR: torchvision 0.13.1 has requirement torch==1.12.1, but you'll have torch 1.11.0 which is incompatible.
    ERROR: pandas 2.0.2 has requirement numpy>=1.20.3; python_version < "3.10", but you'll have numpy 1.17.4 which is incompatible.
    ERROR: pandas 2.0.2 has requirement python-dateutil>=2.8.2, but you'll have python-dateutil 2.7.3 which is incompatible.
    ERROR: pandas 2.0.2 has requirement pytz>=2020.1, but you'll have pytz 2019.3 which is incompatible.
    ERROR: huggingface-hub 0.15.1 has requirement packaging>=20.9, but you'll have packaging 20.3 which is incompatible.
    ERROR: scipy 1.10.1 has requirement numpy<1.27.0,>=1.19.5, but you'll have numpy 1.17.4 which is incompatible.
    ERROR: chromadb 0.3.23 has requirement numpy>=1.21.6, but you'll have numpy 1.17.4 which is incompatible.
    ERROR: chromadb 0.3.23 has requirement requests>=2.28, but you'll have requests 2.22.0 which is incompatible.
    ERROR: typer 0.9.0 has requirement click<9.0.0,>=7.1.1, but you'll have click 7.0 which is incompatible.
    ERROR: argilla 1.11.0 has requirement pandas<2.0.0,>=1.0.0, but you'll have pandas 2.0.2 which is incompatible.
    ```
