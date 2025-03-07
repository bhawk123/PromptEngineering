import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
    structured_prompt = PromptTemplate(
        input_variables=["topic"],
        template="Provide a definition of {topic}, explain its importance, and list three key benefits."
    )
    formatted_prompt = structured_prompt.format(topic="Artificial Intelligence")  # Example topic
    response = llm.invoke(formatted_prompt)
    print(response.content)
except Exception as e:
    print("Error:", str(e))
