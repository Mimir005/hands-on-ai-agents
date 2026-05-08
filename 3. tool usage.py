from pprint import pprint

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)


# 默认情况下，工具名称为函数名,但也可以通过name参数自定义工具名称
# 工具描述可以通过docstring提供，agent会在调用工具前将其作为提示的一部分传递给模型，以帮助模型理解工具的功能和使用方法。
# 工具描述默认使用函数的docstring，如果没有提供docstring，则工具将没有描述。
@tool
def add_numbers(a: int, b: int) -> int:
    """将两个数字相加并返回结果"""
    return a + b
"""
@tool("add_numbers", "将两个数字相加并返回结果")
def tooll(a: int, b: int) -> int:
    return a + b
"""

agent = create_agent(llm, tools=[add_numbers])
question = "请帮我计算一下 5 + 7 的结果。"
response = agent.invoke({'messages': [question]})

print(f"模型回答: {response['messages'][-1].content}")

print("\n=== 工具调用详细过程 ===")
pprint(response)
