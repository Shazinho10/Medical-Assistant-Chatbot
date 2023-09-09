import os
from langchain.tools import BaseTool
from langchain.agents import initialize_agent
import openai, numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity

os.environ["OPENAI_API_KEY"] = "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"
api_key = "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"
openai.api_key = api_key


doctors = {
    "urologist": "Dr Daniel, Urologist, contact: daniel@treatmentgps.com",
    "urology": "Dr Daniel, Urologist, contact: daniel@treatmentgps.com",
    "cardiologist": "Dr Albert, Cardiologist, contact: albert@tratmentgps.com",
    "cardiology": "Dr Albert, Cardiologist, contact: albert@tratmentgps.com",
    "general surgeon": "Dr Daive Dimarco, General Surgeon, contact: d.dimarco@treatmentgps.com",
    "general surgery": "Dr Daive Dimarco, General Surgeon, contact: d.dimarco@treatmentgps.com",
    "medical specialist": "Dr Phill, Medical Specialist, contact: phill@treatmentgps.com"
}

class doc_tool(BaseTool):
    name = "Doctor Recommender"
    description = '''use this tool when you need suggest the doctor if user asks based on the problem they are facing such has urology, cardiac isues etc.'''
    def _run(self, field:str):
        field = field.lower()
        texts = list(doctors.keys())

        resp = openai.Embedding.create(
            input= texts,
            engine="text-similarity-davinci-001")

        resp2 = openai.Embedding.create(
            input= field,
            engine="text-similarity-davinci-001")

        li = []
        for ele in resp['data']:
            li.append(ele["embedding"])

        scores = []
        for i in range(len(texts) - 1):
          scores.append(np.dot(resp['data'][i]['embedding'], resp2['data'][0]['embedding'])*100)

        relevant_word = texts[np.argmax(scores)]

        return doctors[relevant_word]

    def _arun(self, field: str):
        raise NotImplementedError("This tool does not support async")



class catheter_refil(BaseTool):
    name = "Catheter Refill Form"
    description = "use this tool when user asks for a refill of the catheter"
    def _run(self, field:str):
        return f""" Kindly fill out the following form to get a refill of your catheter
        https://treatmentgps.com/treatment/catheter-fill-request-survey/"""

    def _arun(self, field: str):
        raise NotImplementedError("This tool does not support async")
