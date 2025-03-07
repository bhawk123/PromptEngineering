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
        input_variables=["profession", "work_location"],
        template="You are a {profession}. Describe 3 ways AI has improved your daily work at the {work_location}..."
    )
    formatted_prompt = structured_prompt.format(profession="Doctor", work_location="Hospital")
    response = llm.invoke(formatted_prompt)
    print(response.content)
except Exception as e:
    print("Error:", str(e))
