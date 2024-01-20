# Q&A Chatbot
from langchain.llms import OpenAI

import streamlit as st
import os



## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm=OpenAI(openai_api_key = 'please enter API Key like this: sk-cabpqouOpg91vT3BlbkFJ964owDSrV6Zgek1Zxnse', model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)



