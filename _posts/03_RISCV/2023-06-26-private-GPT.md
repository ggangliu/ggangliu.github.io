---
layout: post
title: "如何部署一个私有的，不需要联网的ChatGPT"
tags: software
---

想打造一个自己私有的、不联网的ChatGPT吗？本文将介绍并记录如何利用开源项目privateGPT来打造一个私有的ChatGPT

---

通常我们可能有一些私有的数据为自己所用，不希望其他人拿到这些数据，但数据量也比较大，每次查找起来不是很快速，那么搭建一个自己私有的ChatGPT就能够向这些文档提问，用起来也是很方便且酷酷的。

## privateGPT

利用大语言模型的能力，向你的文档提问。100%的私有，在任何时候都不会有数据离开你的运行环境，因为不联网也可以用。

## 环境安装

1. 为了让你的环境能够运行代码，首先安装所有需要的依赖。

    ```bat
    pip3 install -r requirements.txt
    ```

2. 下载LLM模型并且放在自己选择的目录下
    默认是[ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin)
3. 复制example.env模板为.env

    ``` bat
    cp example.env .env
    ```

    并且编辑.env文件中相关的变量

    ```bat
    MODEL_TYPE: supports LlamaCpp or GPT4All
    PERSIST_DIRECTORY: is the folder you want your vectorstore in
    MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
    MODEL_N_CTX: Maximum token limit for the LLM model
    MODEL_N_BATCH: Number of tokens in the prompt that are fed into the model at a time. Optimal value differs a lot depending on the model (8 works well for GPT4All, and 1024 is better for LlamaCpp)
    EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
    TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
    ```

**注意**：由于langchain加载SentenceTransformers，所以第一次运行脚本的时候将要求联网去下载这个embeddeding模型自己。

## 测试数据集

这个库有一个[state of the union transcript](https://github.com/imartinez/privateGPT/blob/main/source_documents/state_of_the_union.txt)作为例子

## 导入自己的数据集

测试没问题的话，就可以导入我们自己的数据集了。需要将所有你的文件放入source_documents目录中

支持的文件扩展名如下：

``` bat
.csv: CSV,
.docx: Word Document,
.doc: Word Document,
.enex: EverNote,
.eml: Email,
.epub: EPub,
.html: HTML File,
.md: Markdown,
.msg: Outlook Message,
.odt: Open Document Text,
.pdf: Portable Document Format (PDF),
.pptx : PowerPoint Document,
.ppt : PowerPoint Document,
.txt: Text file (UTF-8),
```

运行下面的命令导入所有的数据

```bat
python ingest.py
```

输出应该如下所示：

```ini
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.73s/it]
Loaded 1 new documents from source_documents
Split into 90 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Using embedded DuckDB with persistence: data will be stored in: db
Ingestion complete! You can now run privateGPT.py to query your documents
```

这个过程中将创建一个db目录存放本地的数据。每个文档大概需要20-30秒，具体时间跟文档大小相关。你可以导入尽可能多你想要的文档，并且将被累积在本地的数据库中。如果你想从一个空的数据开始，删除db目录即可。

**注意**：在你导入的过程中，没有数据会离开你的本地环境。你可以在没联网的情况下导入，除了第一次运行ingest脚本的时候，因为第一次需要下载一个内置模型。

## 在本地向你的文档提问

为了提问，运行如下命令：

```bat
python privateGPT.py
```

并等待脚本让你输入问题

```bat
> Enter a query:
```

输入完问题，按下回车键后，你可能需要等待20-30秒（跟电脑的性能也相关），LLM模型需要消耗时间解析你的问题并且准备答案。一旦完成，它将输出答案及作为文档上下文使用的4个来源。你能够持续提问，不需要重新运行脚本，仅仅是再一次等待。

**注意**：即使你关闭网络，脚本的推理任然可以工作，没有数据能够离开你的电脑。

输入exit退出脚本。

## 它是怎么工作的呢？

选择正确的本地模型和LangChain能力，你能在本地运行整个管线，且没有任何数据泄露的风险，并且有着比较合理的性能。

- ingest.py uses LangChain tools to parse the document and create embeddings locally using HuggingFaceEmbeddings (SentenceTransformers). It then stores the result in a local vector database using Chroma vector store.
- privateGPT.py uses a local LLM based on GPT4All-J or LlamaCpp to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- GPT4All-J wrapper was introduced in LangChain 0.0.162.

## 写在最后

该项目的官方源码地址<https://github.com/imartinez/privateGPT>，有能力的可以自行研究。
