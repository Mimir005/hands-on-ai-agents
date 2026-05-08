from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
