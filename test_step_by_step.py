import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Initialize the ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4o-mini")
# Test the setup
try:
  problem_solving_prompt = PromptTemplate(
    input_variables=["problem"],
    template="""Solve the following problem step by step:
    Problem: {problem}
    Solution:
    1)"""
  )
  formatted_prompt = problem_solving_prompt.format(problem="global warming")
  response = llm.invoke(formatted_prompt)
  print(response.content)
except Exception as e:
  print("Error:", str(e))