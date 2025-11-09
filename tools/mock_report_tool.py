# tools/mock_report_tool.py
import json
from crewai_tools import BaseTool

class MockReportGeneratorTool(BaseTool):
    name = "Mock Report Generator Tool"
    description = "Simulates creating a professional report from the final AI summary."

    def _run(self, final_summary: str) -> str:
        """Simulate saving a report and returning path."""
        report_path = "/reports/Tadalafil_Repurposing_Report.pdf"
        word_count = len(final_summary.split())
        print("\n📄 Report successfully created and archived!")
        print(f"Word count: {word_count}")
        print(f"File saved at: {report_path}\n")

        return json.dumps({
            "status": "success",
            "file_path": report_path,
            "word_count": word_count,
            "message": "Report archived successfully."
        }, indent=2)
