# 🧠 Agentic AI Finance Agent

> Multi-agent assistant that fuses live market data with web-scraped news—powered by [Agno](https://pypi.org/project/agno/).

---

## ✨ Features
| Capability           | Details                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------|
| **Web Search Agent** | Fetches fresh articles via DuckDuckGo and returns answers with clickable citations.                               |
| **Finance Agent**    | Pulls quotes, fundamentals, analyst recommendations, and news from Yahoo Finance via `YFinanceTools`.             |
| **Coordinator**      | Orchestrates both specialists to deliver richer answers in a single response.                                     |
| **Streaming Output** | Responses stream token-by-token for a snappy user experience.                                                     |
| **Markdown Tables**  | Numerical data (prices, ratios, etc.) are auto-formatted into tidy tables.                                        |
| **SQLite Memory**    | Optional long-term conversation storage with `SqliteStorage`.                                                     |
| **FastAPI Playground** | Comes with a ready-to-run browser UI for interactive exploration.                                               |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    U([User Prompt]) --> C{{Coordinator Agent}}
    C --|delegates|--> WS[Web Search Agent]
    C --|delegates|--> FA[Finance Agent]
    WS --> DDG[DuckDuckGo]
    FA --> YF[Yahoo Finance]
    C --|stream|--> R[Response (tables & citations)]
