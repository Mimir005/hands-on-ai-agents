"""
给agent添加自定义上下文信息
"""
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool, ToolRuntime

from dataclasses import dataclass



@dataclass
class CustomContext:
    user_name: str = '王允承'
    user_age: int = 24
    user_hobby: str = '编程'

@tool
def get_user_info(runtime: ToolRuntime[CustomContext]) -> str:
    """获取用户的基本信息"""
    return f"用户姓名: {runtime.custom_context.user_name}, 年龄: {runtime.custom_context.user_age}, 爱好: {runtime.custom_context.user_hobby}"

llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)

agent = create_agent(llm, tools = [get_user_info])

responses = agent.invoke({'messages': [HumanMessage(content="请介绍一下我自己")]})
print(responses['messages'][-1].content)
print('Agent完整信息：\n')
print(responses)
