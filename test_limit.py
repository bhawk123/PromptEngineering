import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
  limited_fact_check_prompt = PromptTemplate(
  input_variables=["statement"],
  template="""Evaluate the following statement for factual
  accuracy. If it's incorrect, provide the correct information in five words or less:
  Statement: {statement} 
  Evaluation:"""
)
  formatted_prompt = limited_fact_check_prompt.format(statement="Trump is King of the Canada")
  response = llm.invoke(formatted_prompt)
  print(response.content)
except Exception as e:
  print("Error:", str(e))