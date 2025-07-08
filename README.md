# 🧠 Agentic AI Finance Agent

> Multi-agent research assistant for live market data, analyst ratings, and web-scraped news—built with [**Agno**](https://pypi.org/project/agno/).

---

## ✨ Features
| Capability           | Details                                                                                                                         |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Web Search Agent** | Uses DuckDuckGo to retrieve up-to-date articles and returns answers with clickable citations.                                   |
| **Finance Agent**    | Pulls quotes, fundamentals, analyst recommendations, and news from Yahoo Finance via `YFinanceTools`.                           |
| **Coordinator**      | A parent “multimodal” agent orchestrates both specialists to deliver richer answers in a single response.                       |
| **Streaming Output** | Responses are streamed token-by-token for real-time UX.                                                                         |
| **Markdown Tables**  | Numerical data (prices, ratios, etc.) are auto-formatted into tidy tables.                                                      |
| **SQLite Memory**    | Optional long-term conversation storage using `SqliteStorage`, so the agent “remembers” context between sessions.               |
| **FastAPI UI**       | Comes with a ready-to-run Playground (FastAPI + Uvicorn) for chat-style exploration in the browser.                             |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    U[User Prompt] --> C(Multimodal<br/>Coordinator Agent)
    C --delegates--> WS[Web Search Agent]
    C --delegates--> FA[Finance Agent]
    WS --> DDG[🌐 DuckDuckGo]
    FA --> YF[📈 Yahoo Finance]
    WS & FA --> C
    C -->|stream| R[Response<br/>(tables + citations)]
