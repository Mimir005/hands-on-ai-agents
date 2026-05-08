"""
2026-5-7：
使用Tavily进行网络搜索，获取最新信息。
虽然查询时间这种简单的任务都失败了，但至少证明了工具调用的流程是正确的。
笑死了，工具调用成功了，但工具本身失败了。

改变提示词，要么日期变成昨天，要么具体时间错误。
"""
from pprint import pprint

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

import os
load_dotenv()

tavily_api_key = os.getenv('TAVILY_API_KEY')

tavily_client = TavilyClient(api_key=tavily_api_key)

# 函数版，测试用
def text_web_search(query: str) -> dict:
    """使用Tavily进行网络搜索，并返回搜索结果的摘要"""
    search_results = tavily_client.search(query)
    return search_results

@tool
def web_search(query: str) -> dict:
    """使用Tavily进行网络搜索，并返回搜索结果的摘要"""
    search_results = tavily_client.search(query)
    return search_results


qwen2 = ChatOpenAI(
    model='qwen2',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)
agent = create_agent(model=qwen2, tools = [web_search])


if __name__ == "__main__":
    mode = input('输入text，使用函数版；输入agent，使用agent调用工具：')
    if mode == 'text':
        print("=== 开始网络搜索 ===\n")
        query = "请帮我搜索一下今天的日期"
        response = text_web_search(query)
        pprint(f"搜索结果摘要:\n{response}")
        print("\n=== 搜索完成 ===")
        print(type(response))

    elif mode == 'agent':
        print("=== 开始网络搜索 ===\n")
        query = '现在的美国总统是谁，使用工具'# "请帮我搜索一下今天的日期（北京时间），并告诉我你查询的网站具体网址是什么？（使用工具）"
        response = agent.invoke({'messages': [query]})
        pprint(f"搜索结果摘要:\n{response}")
        pprint(f"模型回答:\n{response['messages'][-1].content}")
        print("\n=== 搜索完成 ===")
        print(type(response['messages'][-1].content))

    else:
        print("输入无效，请输入 'text' 或 'agent'。")


