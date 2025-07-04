import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# UI Setup
st.title("🧠 Groq Chatbot")
user_input = st.text_input("Ask something:")

if user_input:
    with st.spinner("Thinking..."):

        # Prompt and model setup
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "{input}")
        ])
        parser = StrOutputParser()
        model = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

        chain = prompt | model | parser

        # Run and display
        answer = chain.invoke({"input": user_input})
        st.success(answer)
