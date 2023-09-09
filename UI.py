import os
from langchain.vectorstores import FAISS
from openai.embeddings_utils import get_embedding, cosine_similarity
import os
import streamlit as st
from dotenv import load_dotenv


from test import *
from htmlTemplates import css, bot_template, user_template
import streamlit as st
from streamlit_chat import message
from cathe import *

vectorstore = FAISS.load_local('treatmentgps_db',
                            embeddings_openai)
st.title("Assistant TreatmentGPS")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
    else:
        st.write(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
prompt = st.chat_input("How can I help you today?", key="user_input")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.write(user_template.replace("{{MSG}}", prompt), unsafe_allow_html=True)
    message_placeholder = st.empty()
    
    # if "catheter" in prompt.lower() and "refil" in prompt.lower():
    #     catheter_refilling()
    
    # elif "catheter" in prompt.lower() and "finish" in prompt.lower():
    #     catheter_refilling()

    # if "catheter" in prompt.lower() and "empty" in prompt.lower():
    #     catheter_refilling()

    # else:
    message_placeholder = st.empty()
    result = ""
    result = agent(prompt)["output"]
    bot_response = result#"Bot's response"  # Replace this with your actual bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.write(bot_template.replace("{{MSG}}", bot_response), unsafe_allow_html=True)