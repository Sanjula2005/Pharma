# import json
# from langchain_community.llms import Ollama

# class IQVIAAgent:
#     def __init__(self):
#         self.llm = Ollama(model="llama3")

#     def run(self, query):
#         data = json.load(open("data/mock_market_data.json"))
#         prompt = f"""
#         You are a pharma market analyst. Using this data: {data},
#         summarize market size, CAGR, and competitive intensity for query: {query}.
#         """
#         return self.llm.invoke(prompt)
import json
import os
from groq import Groq

class IQVIAAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run(self, query):
        data = json.load(open("data/mock_market_data.json"))

        prompt = f"""
You are a pharma market analyst.

Using the following market data:
{json.dumps(data, indent=2)}

Analyze:
- Market size
- CAGR
- Competitive intensity

Query: {query}
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return {
            "agent": "iqvia",
            "title": "📊 Market & Competitive Landscape",
            "content": response.choices[0].message.content.strip()
        }
