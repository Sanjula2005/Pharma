# # import requests
# # import json
# # from langchain_community.llms import Ollama


# # class PatentAgent:
# #     def __init__(self):
# #         self.llm = Ollama(model="llama3")
# #         self.api_url = "https://serpapi.com/search.json"
# #         self.api_key = "fab5a9439fcf74e29a0cd97376db8e6777a6eea7406708a04f96fd05cd7c89dd"  # 🔑 paste your real key here

# #     def run(self, query):
# #         print(f"🔍 Fetching patent data for: {query}")

# #         params = {
# #             "engine": "google_patents",
# #             "q": query,
# #             "api_key": self.api_key
# #         }

# #         try:
# #             response = requests.get(self.api_url, params=params)
# #             response.raise_for_status()
# #             data = response.json()

# #             patents = []
# #             for item in data.get("organic_results", []):
# #                 patents.append({
# #                     "title": item.get("title"),
# #                     "link": item.get("link"),
# #                     "snippet": item.get("snippet"),
# #                     "publication_date": item.get("publication_date")
# #                 })

# #             structured = {
# #                 "source": "Google Patents",
# #                 "query": query,
# #                 "count": len(patents),
# #                 "patents": patents
# #             }

# #             summary_prompt = (
# #                 f"Summarize key patent expiry trends, innovation focus, and FTO risks for "
# #                 f"{query} based on this structured patent data: {json.dumps(structured, indent=2)}"
# #             )

# #             summary = self.llm.invoke(summary_prompt)

# #             return {"summary": summary, "data": structured}

# #         except Exception as e:
# #             return {"error": f"Patent fetch failed: {str(e)}"}


# import os
# import json
# import requests
# from langchain_community.llms import Ollama


# class PatentAgent:
#     def __init__(self):
#         self.llm = Ollama(model="llama3")
#         self.api_url = "https://serpapi.com/search.json"
#         import os

#         self.api_key = os.getenv("SERPAPI_KEY")
#         if not self.api_key:
#             raise EnvironmentError("SERPAPI_KEY not set")

#     def run(self, query):
#         print(f"🔍 Fetching patent data for: {query}")

#         params = {
#             "engine": "google_patents",
#             "q": f"latest innovation for {query}",
#             "api_key": self.api_key
#         }

#         try:
#             response = requests.get(
#                 self.api_url,
#                 params=params,
#                 timeout=20
#             )
#             response.raise_for_status()

#             data = response.json()

#             if "error" in data:
#                 raise RuntimeError(data["error"])

#             patents = []
#             for item in data.get("organic_results", []):
#                 patents.append({
#                     "title": item.get("title"),
#                     "link": item.get("link"),
#                     "snippet": item.get("snippet"),
#                     "publication_date": (
#                         item.get("publication_date")
#                         or item.get("priority_date")
#                         or item.get("filing_date")
#                     )
#                 })

#             structured = {
#                 "source": "Google Patents (SerpAPI)",
#                 "query": query,
#                 "count": len(patents),
#                 "patents": patents
#             }

#             summary_prompt = f"""
#             You are a pharmaceutical IP strategist.

#             Using the patent dataset below, analyze:
#             - Innovation focus areas
#             - Patent expiry or lifecycle signals
#             - Freedom-to-operate (FTO) risks

#             Patent data:
#             {json.dumps(structured, indent=2)}
#             """

#             summary = self.llm.invoke(summary_prompt)

#             return {
#                 "summary": summary,
#                 "data": structured
#             }

#         except Exception as e:
#             return {
#                 "error": f"Patent fetch failed: {str(e)}",
#                 "query": query
#             }
import os
import json
import requests
from groq import Groq

class PatentAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.api_url = "https://serpapi.com/search.json"
        self.api_key = os.getenv("SERPAPI_KEY")

        if not self.api_key:
            raise EnvironmentError("SERPAPI_KEY not set")

    def run(self, query):
        params = {
            "engine": "google_patents",
            "q": f"{query} pharmaceutical innovation",
            "api_key": self.api_key
        }

        response = requests.get(self.api_url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        patents = data.get("organic_results", [])[:5]

        prompt = f"""
You are a pharmaceutical IP strategist.

Based on the following patent data:
{json.dumps(patents, indent=2)}

Analyze:
- Innovation focus
- Patent lifecycle
- Freedom-to-operate risks
"""

        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return {
            "agent": "patent",
            "title": "📑 Patent & IP Landscape",
            "content": completion.choices[0].message.content.strip()
        }
