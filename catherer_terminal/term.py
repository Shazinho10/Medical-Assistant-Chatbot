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
import os
import streamlit as st
from dotenv import load_dotenv
import langchain
import random
import time
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain.chains import RetrievalQA
from test import *
from htmlTemplates import css, bot_template, user_template
import streamlit as st
from streamlit_chat import message
vectorstore = FAISS.load_local('treatmentgps_db',
                            embeddings_openai)

class CommandLineChatbot:
    def __init__(self):
        self.responses = {}

    def ask_question(self, question):
        user_input = input(f"Bot: {question}\nYou: ")
        self.responses[question] = user_input

    def run(self):
        print("Bot: Hey! How can I assist you today?")    
        while True:
            user_input = input("You: ")
            if "catherer" in user_input.lower():
                print("Bot: Sure, let's get started with the questionnaire!")
                question_list = [
                                    "Who is filling out this questionnaire?",
                                    "Are you living in a Skilled Nursing Facility?",
                                    "Are you currently on any Home Health Services?",
                                    "What is your address?",
                                    "What insurance are we billing?",
                                    "Have there been any changes to the type of catheters or supplies you are using?",
                                    "What brand, size and style catheter size are you using?",
                                    "How many catheters are you using daily?",
                                    "Do you have 10 days or less of supplies?",
                                    "Would you like to reorder catheters?",
                                    "Would you like to reorder lubricant?",
                                    "Do you have any questions or comments for the navigator?"
                                ]
                for question in question_list:
                    self.ask_question(question)
                print("Bot: Thank you for answering the questions!")
            else:
                result = agent(user_input)["output"]
                print("Bot:", result)


if __name__ == "__main__":
    chatbot = CommandLineChatbot()
    chatbot.run()
