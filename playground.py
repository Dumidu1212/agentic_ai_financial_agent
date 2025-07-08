from agno.agent import Agent
from agno.models.groq import Groq 
from agno.tools.yfinance import YFinanceTools 
from agno.tools.duckduckgo import DuckDuckGoTools 
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground

agent_storage: str = "tmp/agents.db"

## Web Search Agent
web_search_agent = Agent(
  name = "Web Search Agent",
  role = "Search the web for information",
  model = Groq(id = "Meta-Llama/Llama-4-Maverick-17b-128e-instruct"),
  tools = [DuckDuckGoTools()],
  instructions = ["Always include the source of the information you find."],
  storage=SqliteStorage(table_name="web_agent", db_file="agents.db"),
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
  storage=SqliteStorage(table_name="web_agent", db_file="agents.db"),
  show_tool_calls = True,
  markdown = True,
)

playground_app = Playground(agents=[finance_agent, web_search_agent])
app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("playground:app", reload=True)