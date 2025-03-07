import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
  fact_check_prompt = PromptTemplate(
  input_variables=["statement"],
  template="""Evaluate the following statement for factual
  accuracy. If it's incorrect, provide the correct information:
  Statement: {statement}
  Evaluation:"""
)
  formatted_prompt = fact_check_prompt.format(problem="Trump is King of the USA")
  response = llm.invoke(formatted_prompt)
  print(response.content)
except Exception as e:
  print("Error:", str(e))