# import json
# from langchain_community.llms import Ollama

# class EXIMAgent:
#     def __init__(self):
#         self.llm = Ollama(model="llama3")

#     def run(self, query):
#         data = json.load(open("data/mock_exim_data.json"))
#         prompt = f"Analyze API sourcing trends and trade risks for {query} using {data}"
#         return self.llm.invoke(prompt)
# agents/exim_agent.py
class EXIMAgent:
    def run(self, query):
        print(f" - Running EXIM Agent for: {query}")
        # FIX: Changed ** to <b> and </b>
        # return f"<b>EXIM/Supply Chain:</b> The API sourcing for the molecule related to '{query}' is 80% concentrated in India, posing a moderate sourcing risk, but is currently stable."
        return {
        "agent": "exim",
        "title": "API Sourcing & Supply Chain Risk",
        "content": "The API sourcing for Amoxicillin is 80% concentrated in India, posing a moderate sourcing risk but currently stable."
        }
