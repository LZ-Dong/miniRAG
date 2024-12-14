# miniRAG
> LLM会产生误导性的 “幻觉”，依赖的信息可能过时，处理特定知识时效率不高，缺乏专业领域的深度洞察，同时在推理能力上也有所欠缺。
>
> 正是在这样的背景下，检索增强生成技术（Retrieval-Augmented Generation，RAG）应时而生，成为 AI 时代的一大趋势。
>
> RAG 通过在语言模型生成答案之前，先从广泛的文档数据库中检索相关信息，然后利用这些信息来引导生成过程，极大地提升了内容的准确性和相关性。RAG 有效地缓解了幻觉问题，提高了知识更新的速度，并增强了内容生成的可追溯性，使得大型语言模型在实际应用中变得更加实用和可信。
>
> 此仓库用于学习大模型RAG的相关内容，目前为手搓实现，主要是llama-index和langchain不太好魔改。此仓库可以方便看论文的时候，实现一些小的实验。以下为本仓库的RAG整体框架图。
>
> 以下为笔者所构思的RAG实现过程，这里面主要包括包括三个基本步骤：
>
> 1. 索引 — 将文档库分割成较短的 Chunk，并通过编码器构建向量索引。
> 2. 检索 — 根据问题和 chunks 的相似度检索相关文档片段。
> 3. 生成 — 以检索到的上下文为条件，生成问题的回答。
>

## 项目流程图

# ![RAG](.\images\figure1.png)

## 举例说明

**Query**

如何打开后背箱？

**Matching docs （Top-3）**

1. '自定义后备箱打开角度\n方法\n在中控屏进入设置＞车辆控制，点击后备箱高度记忆，可自行设置后备箱打开角度。\n',

2. '在中控屏进入设置＞车辆控制，点击开关，可打开、暂停或关闭后备箱。\n',

3. '中控屏打开或关闭后备箱\n您可以通过以下方式打开或关闭后备箱：\n从中控屏顶部下滑出控制中心，点击"后备箱"开关，可打开、暂停或关闭后备箱。\n'

**Response**

![Response](.\images\figure2.png)

# 项目结构

```
miniRAG
├─ component
│  ├─ data_chunker.py
│  ├─ databases.py
│  ├─ embedding.py
│  └─ llms.py
├─ data
├─ database
│  ├─ doecment.json
│  └─ vectors.json
├─ miniRAG.md
├─ README.md
└─ requirements.txt
```
# QuickStrat

安装依赖，需要 Python 3.10 以上版本。

```bash
pip install -r requirements.txt
```
