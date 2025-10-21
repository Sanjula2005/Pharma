# import json
# from langchain_community.llms import Ollama

# class ClinicalAgent:
#     def __init__(self):
#         self.llm = Ollama(model="llama3")

#     def run(self, query):
#         data = json.load(open("data/mock_clinical_data.json"))
#         prompt = f"List active/completed clinical trials for {query} from {data}"
#         return self.llm.invoke(prompt)


import requests
import json

class ClinicalAgent:
    """
    Clinical Agent that fetches live data from the new ClinicalTrials.gov API (v2).
    """
    def __init__(self):
        self.api_url = "https://clinicaltrials.gov/api/v2/studies"

    def run(self, query, max_results=10):
        try:
            params = {
                "query.term": query,
                "pageSize": max_results,
            }
            response = requests.get(self.api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # parse the results
            studies = []
            for item in data.get("studies", []):
                protocol = item.get("protocolSection", {})
                identification = protocol.get("identificationModule", {})
                description = protocol.get("descriptionModule", {})
                status = protocol.get("statusModule", {})
                sponsor = protocol.get("sponsorCollaboratorsModule", {})
                location = protocol.get("contactsLocationsModule", {})

                studies.append({
                    "NCTId": identification.get("nctId"),
                    "Title": identification.get("briefTitle"),
                    "Condition": description.get("conditions"),
                    "OverallStatus": status.get("overallStatus"),
                    "Phase": status.get("phase"),
                    "SponsorName": sponsor.get("leadSponsor", {}).get("name"),
                    "LocationCountry": location.get("locations", [{}])[0].get("country"),
                    "StartDate": status.get("startDateStruct", {}).get("date"),
                    "CompletionDate": status.get("completionDateStruct", {}).get("date")
                })

            result = {
                "query": query,
                "count_returned": len(studies),
                "studies": studies
            }

            return {"source": "clinicaltrials.gov", "data": result}

        except requests.exceptions.RequestException as e:
            return {"error": f"ClinicalTrials.gov request failed: {str(e)}"}
