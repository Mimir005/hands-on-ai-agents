
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import os
load_dotenv()
web_search = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))

@tool
def web_search_tool(query: str) -> dict:
    """使用Tavily进行网络搜索，并返回搜索结果的摘要"""
    search_results = web_search.search(query)
    return search_results

llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)


agent = create_agent(llm, tools = [web_search_tool])

responses = agent.invoke({'messages': ['现在的美国总统是谁']})
