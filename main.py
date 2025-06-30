from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not firecrawl_api_key or not openai_api_key:
    raise ValueError("❌ Missing FIRECRAWL_API_KEY or OPENAI_API_KEY in environment.")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=openai_api_key
)

server_params = StdioServerParameters(
    command="npx",
    env={"FIRECRAWL_API_KEY": firecrawl_api_key},
    args=["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            print("\n🔧 Available Tools:", *[tool.name for tool in tools])
            print("-" * 60)

            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can scrape websites, crawl pages, and extract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user."
                }
            ]

            while True:
                user_input = input("\n🧑 You: ")
                if user_input.lower() in {"quit", "exit"}:
                    print("👋 Goodbye")
                    break

                messages.append({"role": "user", "content": user_input[:175000]})

                try:
                    agent_response = await agent.ainvoke({"messages": messages})
                    ai_message = agent_response["messages"][-1].content
                    print("\n🤖 Agent:\n" + ai_message)
                except Exception as e:
                    print("❌ Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
