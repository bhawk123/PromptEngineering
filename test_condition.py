import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
from jinja2 import Template
from dotenv import load_dotenv

load_dotenv()


def get_completion(prompt, model="gpt-4o-mini"):
    ''' Get a completion from the OpenAI API 
    Args:
        prompt (str): The prompt to send to the API
        model (str): The model to use for the completion
    Returns:
        str: The completion text
    '''
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

# Test the function
prompt_text = "What is the capital of France?"
completion = get_completion(prompt_text)

print("Response:", completion)