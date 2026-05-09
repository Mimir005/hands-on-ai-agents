## Langchain Schema

langchain schema是Langchain框架中重要的概念，主要目的是标准化输入输出。



最常用的模块是Message：

```python
from langchain.messages import HumanMessage, AIMessage, ToolMessage
```

用于标准化用户、大模型、工具等的消息传递。
