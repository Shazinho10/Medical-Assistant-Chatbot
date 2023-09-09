import os
import streamlit as st
from langchain.tools import BaseTool
from mail import appointment

class catheter_refilling(BaseTool):
    name = "Catheter Refill Form"
    description = "This will only be useful when the user request for a refill, otherwise dont use it"

    def _run(self):
        try:
            with st.sidebar.form("my_form", clear_on_submit=False):
                st.header("Catheter Refill Form Summary")
                username = st.text_input("Please Enter Your Name:")
                st.info(username)
                email = st.text_input("Please Enter Your Email:")
                st.info(email)

                print("*"*20)
                print(username)
                print("*"*20)

                filling_out_question1 = st.radio("Who is filling out this questionnaire?", [
                "I am the patient",
                "I am the caregiver (Please provide your name)",
                "I am the navigator (via phone call)",
                "Other (describe)"
            ])
                if filling_out_question1 == "I am the caregiver (Please provide your name)":
                    caregiver_name = st.text_input("Please provide your name:")
                else:
                    caregiver_name = ""
                filling_out_question2 = st.radio("Are you living in a Skilled Nursing Facility?", [
                    "No",
                    "Yes, I am in a skilled nursing facility"
                ])
                filling_out_question3 = st.radio("Are you currently on any Home Health Services?", [
                    "No",
                    "Yes, I am on Home Health Services"
                ])

                st.subheader("Catheter and Supplies Reorder")
                catheter_quantity = st.number_input("Enter the quantity of catheters:", min_value=0, step=1)
                supplies_quantity = st.number_input("Enter the quantity of supplies:", min_value=0, step=1)
                
                less_than_10_days = st.radio("Do you have 10 days or less of supplies?", ("No", "Yes"))
                
                st.write("Reorder Catheters:")
                reorder_catheters = st.radio("Catheters Reorder Option", ("No", "Yes"), key="reorder_catheters")
                
                if reorder_catheters == "Yes":
                    col1, col2 = st.beta_columns(2)
                    with col1:
                        reorder_catheters_quantity = st.number_input("Quantity:", min_value=0, step=1, key="reorder_catheters_quantity")
                    with col2:
                        st.empty()
                else:
                    reorder_catheters_quantity = 0
                    
                st.write("Reorder Lubricant:")
                reorder_lubricant = st.radio("Lubricant Reorder Option", ("No", "Yes"), key="reorder_lubricant")
                
                if reorder_lubricant == "Yes":
                    col1, col2 = st.beta_columns(2)
                    with col1:
                        reorder_lubricant_quantity = st.number_input("Quantity:", min_value=0, step=1, key="reorder_lubricant_quantity")
                    with col2:
                        st.empty()
                else:
                    reorder_lubricant_quantity = 0

                submit = st.form_submit_button('Submit information to TreatmentGPS')
                if submit:
                        appointment(username=username, email=email)
                        st.write("Succesfully submitted")
        except:
            return "Here is the form"

    def _arun(self, field: str):
        raise NotImplementedError("This tool does not support async")