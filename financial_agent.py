from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

## Web Search Agent
web_search_agent = Agent(
  name = "Web Search Agent",
  role = "Search the web for information",
  model = Groq(id = "Meta-Llama/Llama-4-Maverick-17b-128e-instruct"),
  tools = [DuckDuckGoTools()],
  instructions = ["Always include the source of the information you find."],
  show_tool_calls = True,
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
   model = Groq(id = "Meta-Llama/Llama-4-Maverick-17b-128e-instruct"),
  instructions = ["Always include sorces","Use tables to display the data"],
  show_tool_calls = True,
  markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)