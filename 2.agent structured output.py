from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.messages import SystemMessage, HumanMessage
from pprint import pprint
from pydantic import BaseModel

llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)

class Person(BaseModel):
    name: str
    age: int
    city: str

from langchain.agents import create_agent
agent = create_agent(llm, response_format=Person)

ask = HumanMessage(content="提取wxd的相关信息")

information = """
name : wxd
age : 24
city : beijing
"""
response = agent.invoke({'messages':[ask, information]})
pprint(response)

structured_response = response['structured_response']
print("\n=== 结构化输出 ===")
print(f"姓名: {structured_response.name}")
print(f"年龄: {structured_response.age}")
print(f"城市: {structured_response.city}")
