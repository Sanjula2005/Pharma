
from groq import Groq
import os

class WebAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run(self, query: str) -> str:
        prompt = f"""
You are a pharmaceutical web intelligence agent.

Task:
- Analyze the user query
- Summarize recent scientific, clinical, regulatory, or news insights
- Keep it concise and factual

User Query:
{query}
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()
