from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

## Web Search Agent
web_search_agent = Agent(
  name = "Web Search Agent",
  role = "Search the web for information",
  model = Groq(id = "Meta-Llama/Llama-4-Maverick-17b-128e-instruct"),
  tools = [DuckDuckGo()],
  instructions = ["Always include the source of the information you find."],
  show_tools_calls = True,
  markdown = True,
)

## Financial Agent
finance_agent = Agent(
  name = "Finance Agent",
  model = Groq(id = "Meta-Llama/Llama-4-Maverick-17b-128e-instruct"),
  tools=[
    YFinanceTools(
      stock_price=True, 
      analyst_recommendations=True, 
      stock_fundamentals=True,
      company_news=True),
  ],
  instructions = ["Use tables to display the data"],
  show_tool_calls = True,
  markdown = True,
)

## Multimodal Agent
multi_ai_agent = Agent(
  team = [web_search_agent, finance_agent],
  instructions = ["Always include sorces","Use tables to display the data"],
  show_tool_calls = True,
  markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)