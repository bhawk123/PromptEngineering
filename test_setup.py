import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
    response = llm.invoke("Hello! Are you working correctly?")
    print("Setup successful! Response:", response.content)
except Exception as e:
    print("Error:", str(e))
