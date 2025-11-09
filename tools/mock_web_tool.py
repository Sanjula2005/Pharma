# tools/mock_web_tool.py

import json
from crewai.tools import tool  # ✅ For crewai-tools >= 1.3.0 and 1.4.1

@tool
def mock_web_intelligence_tool(query: str) -> str:
    """
    Simulates a web search for the molecule or indication and returns structured mock results.
    """
    query_lower = query.lower()

    if "tadalafil" in query_lower:
        results = {
            "topic": "Tadalafil new use",
            "key_findings": [
                "Recent studies (Lancet 2024) show efficacy in Chronic Thromboembolic Pulmonary Hypertension (CTEPH).",
                "FDA has not issued restrictions on new trials for pulmonary hypertension indications.",
                "Patient forums show strong acceptance for once-daily dosing."
            ],
            "citations": [
                {"title": "Lancet Respiratory Medicine 2024", "url": "https://mock.lancet.com/tadalafil"},
                {"title": "FDA Mock Report", "url": "https://mock.fda.gov/tadalafil"},
            ],
            "confidence": "High"
        }
    else:
        results = {
            "topic": query,
            "key_findings": ["No significant new data found online."],
            "citations": [],
            "confidence": "Low"
        }

    return json.dumps(results, indent=2)
