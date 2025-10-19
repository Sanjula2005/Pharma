import json
from langchain_community.llms import Ollama

class EXIMAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        data = json.load(open("data/mock_exim_data.json"))
        prompt = f"Analyze API sourcing trends and trade risks for {query} using {data}"
        return self.llm.invoke(prompt)
