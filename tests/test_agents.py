from agents.web_agent import web_intelligence_agent
from agents.report_agent import report_generator_agent
from tools.mock_web_tool import MockWebIntelligenceTool
from tools.mock_report_tool import MockReportGeneratorTool

def test_web_agent():
    tool = MockWebIntelligenceTool()
    print("\n🔍 Testing Web Tool:")
    print(tool._run("Tadalafil pulmonary hypertension"))

def test_report_agent():
    tool = MockReportGeneratorTool()
    print("\n🧾 Testing Report Generator Tool:")
    print(tool._run("Tadalafil repurposing summary text..."))

if __name__ == "__main__":
    test_web_agent()
    test_report_agent()
