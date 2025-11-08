import requests
import json
from langchain_community.llms import Ollama


class PatentAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.api_url = "https://serpapi.com/search.json"
        self.api_key = "fab5a9439fcf74e29a0cd97376db8e6777a6eea7406708a04f96fd05cd7c89dd"  # 🔑 paste your real key here

    def run(self, query):
        print(f"🔍 Fetching patent data for: {query}")

        params = {
            "engine": "google_patents",
            "q": query,
            "api_key": self.api_key
        }

        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()

            patents = []
            for item in data.get("organic_results", []):
                patents.append({
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "snippet": item.get("snippet"),
                    "publication_date": item.get("publication_date")
                })

            structured = {
                "source": "Google Patents",
                "query": query,
                "count": len(patents),
                "patents": patents
            }

            summary_prompt = (
                f"Summarize key patent expiry trends, innovation focus, and FTO risks for "
                f"{query} based on this structured patent data: {json.dumps(structured, indent=2)}"
            )

            summary = self.llm.invoke(summary_prompt)

            return {"summary": summary, "data": structured}

        except Exception as e:
            return {"error": f"Patent fetch failed: {str(e)}"}
