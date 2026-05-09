## Models

在Langchian中，对于“模型”的分类有三种:

- LLMs
- Chat Models
- Text Embedding Models

### LLMs

LLMs(Large Language Models)

LLM是最早期的大语言模型抽象，本质上是一种文本续写器: Prompts -> Completion
并不理解"角色"，"对话历史"等结构。

Input:string
Output:string

### Chat Models

Chat Models(聊天模型)

一组消息(messages) -> AI回复

Input:Message
Output:AIMessage

注：Message在Langchain中被实现类，用来表示在对话中产生的不同消息。


### Text Embedding Models

Text Embedding Models(文本嵌入模型)

文本嵌入模型与前面的两种类型不同，它并非生成文本，而是将文本转化为向量(Vector)
常用于RAG(检索增强生成)、语义搜索等。


---

Recent Update: 2026/5/9
