# 🔎 Simple AI Agent with Firecrawl + OpenAI + MCP

This is a lightweight AI agent powered by [Firecrawl](https://firecrawl.dev), [LangGraph](https://github.com/langchain-ai/langgraph), and [OpenAI's GPT-4o](https://platform.openai.com/), orchestrated through a message control protocol (MCP).

It allows you to interactively:
- 🔍 Crawl websites
- 🧠 Reason with scraped data
- ⚡️ Run tool-augmented tasks from the terminal

---

## 🚀 Features

- 🧠 LLM agent with GPT-4o-mini
- 🔧 Tool usage via Firecrawl's `firecrawl-mcp`
- 🌐 Web data extraction in real time
- ⚙️ Fully event-driven using LangGraph and MCP

---

## 📦 Requirements

- Python 3.10+
- Node.js (for `npx firecrawl-mcp`)
- OpenAI API Key
- Firecrawl API Key

---

## ⚙️ Setup

### 1. Install dependencies

```bash
uv init
uv add langchain-openai langgraph python-dotenv langchain-mcp-adapters
```

### 2. Configure environment

Create a `.env` file with:

```env
OPENAI_API_KEY=your-openai-key
FIRECRAWL_API_KEY=your-firecrawl-key
```

### 3. Run the agent

```bash
uv run main.py
```

---

## 🧠 Agent Prompt

The system prompt defines the agent as a helpful assistant capable of crawling and extracting data step-by-step using tools from Firecrawl MCP.

> "You are a helpful assistant that can scrape websites, crawl pages, and extract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user."

---

## 💬 Sample Usage

```bash
🧑 You: Search for latest AI research from DeepMind
🤖 Agent:
Using Firecrawl Search...
Crawling DeepMind research page...
Summarized 3 papers:
1. ...
2. ...
```

---

## 🧼 Tips

- Type `quit` or `exit` to stop the session
- Use direct questions like "scrape all headlines from bbc.com"

---

## 🛡️ .gitignore Suggestion

Make sure your `.env` file is ignored:

```
.env
```

---

## 🧪 Testing

You can simulate various prompts or connect this agent to other LLM frameworks like CrewAI or Agentic SDKs with minimal modification.

---

## 📝 License

MIT License — feel free to adapt, extend, or fork.

---

## ✨ Credits

- [LangChain](https://www.langchain.com/)
- [Firecrawl](https://firecrawl.dev)
- [LangGraph](https://github.com/langchain-ai/langgraph)