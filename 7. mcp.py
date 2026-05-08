import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage

async def main():
    # 1. 连接 LangChain 官方文档 MCP
    mcp_client = MultiServerMCPClient({
        "langchain_docs": {
            "transport": "http",
            "url": "https://docs.langchain.com/mcp"
        }
    })

    # 2. 正确 await 获取工具
    tools = await mcp_client.get_tools()

    print(f"成功加载工具数量: {len(tools)}")
    for t in tools:
        print(f"- {t.name}")

    # 3. 配置你的本地 LLM（LM Studio）
    llm = ChatOpenAI(
        model="my_local_model",          # 改成你实际加载的模型名
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
        temperature=0.0,
    )

    # 4. 创建 Agent
    agent = create_agent(llm, tools= tools)

    # 5. 调用 Agent
    query_question = "从 langchain.prompts 导入 PromptTemplate 这个模块能否正常导入？"

    response = await agent.ainvoke({
        "messages": [HumanMessage(content=query_question)],
    })

    print("\n=== Agent 回答 ===")
    print(response["messages"][-1].content)


# =============== 运行 ===============
if __name__ == "__main__":
    asyncio.run(main())