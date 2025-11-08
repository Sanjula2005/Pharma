# # # from agents.iqvia_agent import IQVIAAgent
# # # from agents.exim_agent import EXIMAgent
# # # from agents.patent_agent import PatentAgent
# # # from agents.clinical_agent import ClinicalAgent
# # # from agents.web_agent import WebAgent
# # # from agents.internal_agent import InternalAgent
# # # from utils.report_generator import create_pdf_report
# # # from utils.summarizer import combine_summaries

# # # class MasterAgent:
# # #     def __init__(self):
# # #         self.iqvia = IQVIAAgent()
# # #         self.exim = EXIMAgent()
# # #         self.patent = PatentAgent()
# # #         self.clinical = ClinicalAgent()
# # #         self.web = WebAgent()
# # #         self.internal = InternalAgent()

# # #     def run(self, query):
# # #         iqvia_out = self.iqvia.run(query)
# # #         clinical_out = self.clinical.run(query)
# # #         patent_out = self.patent.run(query)
# # #         exim_out = self.exim.run(query)
# # #         internal_out = self.internal.run(query)
# # #         web_out = self.web.run(query)

# # #         combined = combine_summaries([
# # #             iqvia_out, clinical_out, patent_out, exim_out, internal_out, web_out
# # #         ])

# # #         report_path = create_pdf_report(query, combined)
# # #         return report_path





# # from agents.iqvia_agent import IQVIAAgent
# # from agents.exim_agent import EXIMAgent
# # from agents.patent_agent import PatentAgent
# # from agents.clinical_agent import ClinicalAgent   # ✅ Now uses live API
# # from agents.web_agent import WebAgent
# # from agents.internal_agent import InternalAgent
# # from utils.report_generator import create_pdf_report
# # from utils.summarizer import combine_summaries


# # class MasterAgent:
# #     def __init__(self):
# #         # Initialize all worker agents
# #         self.iqvia = IQVIAAgent()
# #         self.clinical = ClinicalAgent()   # ✅ live clinical trials data
# #         self.patent = PatentAgent()
# #         self.exim = EXIMAgent()
# #         self.internal = InternalAgent()
# #         self.web = WebAgent()

# #     def run(self, query):
# #         print(f"🔍 Starting full Agentic AI workflow for: {query}")

# #         # Run all agents in sequence (Worker-First pattern)
# #         iqvia_out = self.iqvia.run(query)
# #         clinical_out = self.clinical.run(query)  # ✅ Fetches live data
# #         patent_out = self.patent.run(query)
# #         exim_out = self.exim.run(query)
# #         internal_out = self.internal.run(query)
# #         web_out = self.web.run(query)

# #         # Combine all agent results
# #         combined = combine_summaries([
# #             iqvia_out,
# #             clinical_out,
# #             patent_out,
# #             exim_out,
# #             internal_out,
# #             web_out
# #         ])

# #         # Generate PDF report
# #         report_path = create_pdf_report(query, combined)
# #         print(f"✅ Report generated at: {report_path}")
# #         return report_path





# from concurrent.futures import ThreadPoolExecutor
# from agents.iqvia_agent import IQVIAAgent
# from agents.exim_agent import EXIMAgent
# from agents.patent_agent import PatentAgent
# from agents.clinical_agent import ClinicalAgent
# from agents.web_agent import WebAgent
# from agents.internal_agent import InternalAgent
# from utils.report_generator import create_pdf_report
# from utils.summarizer import combine_summaries

# class MasterAgent:
#     def __init__(self):
#         # Initialize all agents
#         self.agents = {
#             "iqvia": IQVIAAgent(),
#             "clinical": ClinicalAgent(),
#             "patent": PatentAgent(),
#             "exim": EXIMAgent(),
#             "internal": InternalAgent(),
#             "web": WebAgent()
#         }

#     def decide_agents(self, query: str):
#         """
#         Dynamically select which agents to invoke based on keywords in the query.
#         """
#         query_lower = query.lower()
#         selected_agents = []

#         # Clinical / research focused
#         if any(word in query_lower for word in ["clinical", "trial", "efficacy", "repurpos"]):
#             selected_agents.append("clinical")
#         if any(word in query_lower for word in ["drug", "repurpos", "off-label"]):
#             selected_agents.append("patent")
#             selected_agents.append("internal")

#         # Market / business focused
#         if any(word in query_lower for word in ["market", "export", "competitor", "sales"]):
#             selected_agents.append("iqvia")
#             selected_agents.append("exim")

#         # Web / general info
#         if any(word in query_lower for word in ["news", "update", "latest"]):
#             selected_agents.append("web")

#         return list(set(selected_agents))  # Remove duplicates

#     def run(self, query: str):
#         print(f"🔍 Starting Dynamic MasterAgent workflow for: {query}")

#         # Determine which agents to run
#         agents_to_run = self.decide_agents(query)
#         print(f"🤖 Agents selected: {agents_to_run}")

#         results = {}

#         # Run selected agents in parallel
#         with ThreadPoolExecutor() as executor:
#             futures = {
#                 executor.submit(self.agents[agent].run, query): agent
#                 for agent in agents_to_run
#             }
#             for future in futures:
#                 agent_name = futures[future]
#                 try:
#                     results[agent_name] = future.result()
#                 except Exception as e:
#                     results[agent_name] = f"Error: {e}"

#         # Combine results into a summary
#         combined_summary = combine_summaries(results.values())

#         # Generate PDF report
#         report_path = create_pdf_report(query, combined_summary)
#         print(f"✅ Report generated at: {report_path}")

#         return report_path




from concurrent.futures import ThreadPoolExecutor
from agents.iqvia_agent import IQVIAAgent
from agents.exim_agent import EXIMAgent
from agents.patent_agent import PatentAgent
from agents.clinical_agent import ClinicalAgent
from agents.web_agent import WebAgent
from agents.internal_agent import InternalAgent
from utils.report_generator import create_pdf_report
from utils.summarizer import combine_summaries


class MasterAgent:
    def __init__(self):
        # Initialize all agents (using your existing files)
        self.agents = {
            "iqvia": IQVIAAgent(),
            "clinical": ClinicalAgent(),
            "patent": PatentAgent(),
            "exim": EXIMAgent(),
            "internal": InternalAgent(),
            "web": WebAgent(),
        }

    def decide_agents(self, query: str):
        """
        Dynamically select which agents to invoke based on query type.
        """
        q = query.lower()
        selected = []

        # Clinical or medical questions
        if any(word in q for word in ["interaction", "side effect", "trial", "dosage", "clinical", "safety"]):
            selected += ["clinical", "internal", "web"]

        # Patent or innovation-related
        if any(word in q for word in ["patent", "innovation", "research", "study"]):
            selected += ["patent", "web"]

        # Market, business, or trade
        if any(word in q for word in ["market", "sales", "demand", "export", "competitor", "iqvia", "trade"]):
            selected += ["iqvia", "exim", "web"]

        # Default fallback
        if not selected:
            print("⚠️ No specific agents matched, using default (internal + web).")
            selected = ["internal", "web"]

        return list(set(selected))

    def run(self, query: str):
        print(f"🔍 Starting Dynamic MasterAgent workflow for: {query}")

        selected_agents = self.decide_agents(query)
        print(f"🤖 Agents selected: {selected_agents}")

        results = {}

        # Run selected agents in parallel
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self.agents[agent].run, query): agent
                for agent in selected_agents
            }
            for future in futures:
                agent_name = futures[future]
                try:
                    results[agent_name] = future.result()
                except Exception as e:
                    results[agent_name] = f"Error in {agent_name}: {str(e)}"

        # Combine all outputs
        combined_summary = combine_summaries(results.values())

        # Generate the PDF report
        report_path = create_pdf_report(query, combined_summary)
        print(f"✅ Report generated at: {report_path}")

        return report_path
