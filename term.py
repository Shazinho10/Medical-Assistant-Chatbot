import os
from langchain.vectorstores import FAISS
import openai, numpy as np
import os
import streamlit as st
from dotenv import load_dotenv
import langchain
import random
import time
from test import *
import streamlit as st
from streamlit_chat import message
from cathe import *
from quest import *
#from ex import quest
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
            if user_input == 'stop':
                break

            if "catheter" in user_input.lower() and 'refill' in user_input.lower():
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
            # continue_interaction = input("Bot: Do you want to continue? (yes/no): ")
            # if continue_interaction.lower() != "yes":
            #     break


if __name__ == "__main__":
    chatbot = CommandLineChatbot()
    chatbot.run()
