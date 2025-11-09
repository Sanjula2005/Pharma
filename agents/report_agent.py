# agents/report_agent.py
from crewai import Agent
from langchain_community.llms import Ollama
from tools.mock_report_tool import MockReportGeneratorTool

local_llm = Ollama(model="llama3:8b", base_url="http://localhost:11434")
report_tool = MockReportGeneratorTool()

report_generator_agent = Agent(
    role='Professional Report Generator',
    goal='Take the final AI summary and format it into a polished, professional report.',
    backstory='An AI agent that turns structured findings into beautiful reports.',
    tools=[report_tool],
    llm=local_llm,
    verbose=True
)

if __name__ == "__main__":
    summary = "Tadalafil shows potential in treating CTEPH with good adherence and low regulatory barriers."
    print("\n📄 Testing Report Generator Agent...\n")
    result = report_tool._run(summary)
    print(result)
