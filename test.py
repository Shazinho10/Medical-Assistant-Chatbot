import os
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.agents import Tool
from langchain.tools import BaseTool
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentExecutor
import openai, numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
from cathe import catheter_refilling

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


embeddings_openai = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
vectorstore = FAISS.load_local('treatmentgps_db',
                            embeddings_openai)

#defining the model
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.0)

general_system_template = """
          You are a helpful assistant of TreatmentGPS company. Answer to the questions regarding the TreatmentGPS content, products and services only.
          If the users say any greetings such as hello, hey or hi etc. respond back with a greeting polietly.
          If the users are asing about catheter refilling, then ask them to wait while the team reaches them back.
          If the question asked is irrelevant and the answer cant be found in the database, dont asnwer, just say, you are not familiar with it.
          {context}
          ----
          """
general_user_template = "Question:```{question}```"

messages = [
SystemMessagePromptTemplate.from_template(general_system_template),
HumanMessagePromptTemplate.from_template(general_user_template)
]
qa_prompt = ChatPromptTemplate.from_messages(messages)

memory = ConversationBufferMemory(
memory_key='chat_history', return_messages=True)

# building the conversation chain
conversation_chain = ConversationalRetrievalChain.from_llm(
llm=llm,
retriever=vectorstore.as_retriever(),
combine_docs_chain_kwargs={"prompt": qa_prompt},
memory=memory)

#converting the conversation chain into a tool
conv_tool = Tool(
name="Normal Query",
return_direct=True,
func=conversation_chain.run,
description= '''This is more suitable for the generic questions regarding products and services of TreatmentGPS.'''
)
tools = [doc_tool(), catheter_refilling(), conv_tool]
agent = initialize_agent( tools,
                          llm,
                          agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                          verbose=False)



if __name__ == "__main__":
    while True:
        txt = input("Enter your query:  ")
        if txt == "break":
            break
        else:
            print(agent(txt)["output"])