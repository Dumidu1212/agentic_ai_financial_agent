<!--
  _____                 _        _        _        _ _          _             
 |  __ \               | |      | |      | |      (_) |        | |            
 | |  | | _____   _____| | ___  | |_ ___ | |_ __ _ _| | ___  __| | ___  _ __  
 | |  | |/ _ \ \ / / _ \ |/ _ \ | __/ _ \| __/ _` | | |/ _ \/ _` |/ _ \| '_ \ 
 | |__| |  __/\ V /  __/ |  __/ | || (_) | || (_| | | |  __/ (_| | (_) | | | |
 |_____/ \___| \_/ \___|_|\___|  \__\___/ \__\__,_|_|_|\___|\__,_|\___/|_| |_|
                                                                              
  A g e n t i c   A I   F i n a n c e   A g e n t
-->

<p align="center">
  <br/>
  <img alt="Agno logo" src="https://raw.githubusercontent.com/dumidu1212/agentic-ai-finance-agent/main/docs/banner.svg" height="180"/>
  <br/><br/>
  <b>Your personal, multi-agent finance research assistant powered by <a href="https://pypi.org/project/agno/">Agno</a></b>
  <br/><br/>
</p>

<p align="center">
  <a href="https://github.com/dumidu1212/agentic-ai-finance-agent/actions">
    <img src="https://github.com/dumidu1212/agentic-ai-finance-agent/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
  </a>
  <a href="https://pypi.org/project/agno/">
    <img src="https://img.shields.io/pypi/v/agno?color=brightgreen" alt="Agno Version"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-informational" alt="License MIT"/>
  </a>
</p>

---

> **TL;DR**  Ask *one* question and instantly receive:
> - Live market quotes & fundamentals  
> - Analyst recommendation consensus  
> - The most recent company news headlines  
> with proper **citations** & **Markdown tables**, streamed in real-time.

---

## 📑 Table of Contents
1. [Features](#-features)  
2. [Architecture](#-architecture)  
3. [Prerequisites](#-prerequisites)  
4. [Quick Start](#-quick-start)  
5. [Configuration](#-configuration)  
6. [Usage Examples](#-usage-examples)  
7. [Project Structure](#-project-structure)  
8. [Run the Playground UI](#-run-the-playground-ui)  
9. [Testing](#-testing)  
10. [Roadmap](#-roadmap)  
11. [Contributing](#-contributing)  
12. [License](#-license)  

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
