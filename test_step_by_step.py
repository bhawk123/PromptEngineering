problem_solving_prompt = PromptTemplate(
  input_variables=["problem"],
  template="""Solve the following problem step by step:
  Problem: {problem}
  Solution:
  1)"""
)

