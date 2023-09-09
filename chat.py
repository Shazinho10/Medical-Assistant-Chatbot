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
import streamlit as st
from streamlit_chat import message
from htmlTemplates import css, bot_template, user_template
vectorstore = FAISS.load_local('treatmentgps_db',
                            embeddings_openai)
st.title("Chat with TreatmentGPS")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        result = ""
        result = agent(prompt)["output"]
        message_placeholder.markdown(result)
    st.session_state.messages.append({"role": "assistant", "content": result})