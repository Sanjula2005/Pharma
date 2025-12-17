# tools/mock_web_tool.py
import json

class MockWebIntelligenceTool:
    def run(self, query: str) -> str:
        return json.dumps({
            "topic": query,
            "key_findings": [
                "Recent studies show new therapeutic potential.",
                "Regulatory updates indicate ongoing interest."
            ],
            "confidence": "High"
        })