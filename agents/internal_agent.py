# from langchain_community.llms import Ollama

# class InternalAgent:
#     def __init__(self):
#         self.llm = Ollama(model="llama3")

#     def run(self, query):
#         prompt = f"Summarize key takeaways from internal documents for {query}."
#         return self.llm.invoke(prompt)
import os
from groq import Groq

class InternalAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run(self, query):
        prompt = f"""
You are an internal pharma strategy analyst.

Summarize key internal insights, risks, and opportunities for:
{query}
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return {
            "agent": "internal",
            "title": "🏢 Internal Strategic Insights",
            "content": response.choices[0].message.content.strip()
        }
