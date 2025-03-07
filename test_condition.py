import os
import openai
from jinja2 import Template
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-4o-mini"):
    ''' Get a completion from the OpenAI API 
    Args:
        prompt (str): The prompt to send to the API
        model (str): The model to use for the completion
    Returns:
        str: The completion text
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]