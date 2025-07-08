# 🧠 Agentic AI Finance Agent

> Multi-agent assistant that fuses live market data with web-scraped news—powered by [Agno](https://pypi.org/project/agno/).

---

## ✨ Features

| Capability | Details |
|------------|---------|
| **Web Search Agent** | Queries DuckDuckGo, returns concise answers with clickable citations. |
| **Finance Agent** | Pulls live quotes, fundamentals, analyst calls, and company news from Yahoo Finance. |
| **Coordinator Agent** | Orchestrates both specialised agents for richer multi-modal answers. |
| **Streaming** | Responses appear token-by-token for snappy UX. |
| **Tabular Output** | Numerical data is formatted in Markdown tables out-of-the-box. |
| **Persistent Memory** | Optional SQLite storage remembers previous chats. |
| **FastAPI Playground** | Beautiful web UI for interactive exploration. |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[User Prompt] --> C(Multimodal<br/>Coordinator Agent)
    C -- delegates --> WS[Web Search Agent]
    C -- delegates --> FA[Finance Agent]
    WS -->|DuckDuckGo API| DDG[🌐 Web]
    FA -->|YahooFinance| YF[📈 Market&nbsp;Data]
    subgraph Tools
        DDG
        YF
    end
    WS & FA --> C
    C -->|Stream<br/>Markdown| U[User]
