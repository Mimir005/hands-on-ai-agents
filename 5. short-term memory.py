"""
使用短期记忆来增强智能体的能力。
短期记忆允许智能体在对话过程中保留上下文信息，从而更好地理解用户的意图并提供更相关的响应。

"""
from pprint import pprint

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from langchain.messages import HumanMessage, SystemMessage, ToolMessage
from langchain.tools import tool

from langgraph.checkpoint.memory import InMemorySaver

llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)


talk1 = HumanMessage(content="我最喜欢的动物是猫")

talk2 = HumanMessage(content="我最喜欢的动物是？")

# 1. 第一次对话，模型没有任何上下文信息，无法回答关于用户喜欢的动物的问题。
# agent = create_agent(llm, tools = [])
#
# response = agent.invoke({'messages': [talk1]})
# pprint(f"第一次询问\n 模型回答:\n{response['messages'][-1].content}")
# pprint(f'模型详细信息\n {response}')
#
# response = agent.invoke({'messages': [talk2]})
# pprint(f"第二次询问\n 模型回答:\n{response['messages'][-1].content}")


# 2. 带有上下文的对话，模型能够理解用户之前提到的信息，并正确回答关于用户喜欢的动物的问题。
agent_with_memory = create_agent(llm, tools = [], checkpointer=InMemorySaver())
config = {'configurable': {'thread_id': '1'}}
response = agent_with_memory.invoke({'messages': [talk1]}, config)
pprint(f"第一次询问\n 模型回答:\n{response['messages'][-1].content}")
pprint('=' * 50)
pprint(f'模型详细信息\n {response}')
pprint('=' * 50)

response = agent_with_memory.invoke({'messages': [talk2]}, config)
pprint(f"第二次询问\n 模型回答:\n{response['messages'][-1].content}")
pprint('=' * 50)
pprint(f'模型详细信息\n {response}')
