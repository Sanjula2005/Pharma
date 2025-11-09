# agents/web_agent.py

from crewai import Agent               # ✅ Needed for agent creation
from langchain_ollama import OllamaLLM  # ✅ Correct import for latest LangChain versions
from tools.mock_web_tool import mock_web_intelligence_tool  # ✅ Import your tool

# Initialize your local Ollama LLM
local_llm = OllamaLLM(model="llama3:8b", base_url="http://localhost:11434")

# Define the Web Intelligence Agent
web_intelligence_agent = Agent(
    role="Real-time Web Intelligence Specialist",
    goal="Perform web-like searches and summarize recent findings about a molecule or indication.",
    backstory="A digital researcher scanning web sources for recent scientific and patient insights.",
    tools=[mock_web_intelligence_tool],
    llm=local_llm,
    verbose=True
)

if __name__ == "__main__":
    # Test the web agent directly
    query = "Tadalafil new use"
    print("\n🧠 Running Web Intelligence Agent...")
    result = mock_web_intelligence_tool(query)
    print("\n✅ Tool Output:\n", result)
