import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
    basic_prompt = "Explain the concept of prompt engineering in one sentence."
    response = llm.invoke(basic_prompt)
    print(response.content)
except Exception as e:
    print("Error:", str(e))
