# from llm_wrapper import llm_func
# from pydantic import BaseModel
# from langchain_openai import OpenAI

# llm = OpenAI()

# @llm_func
# def calculate_score() -> int:
#     """Returns an integer score based on the input text."""
#     pass

# @llm_func
# def is_valid() -> bool:
#     """Determines if the text meets certain criteria, returning True or False."""
#     pass

# class User(BaseModel):
#     name: str
#     age: int

# @llm_func
# def get_user_details() -> User:
#     """Extracts user details from the text and returns them as a User model."""
#     pass

# query = "Calculate the score for the following text..."
# score = calculate_score(llm=llm, query=query)
# print(score)  # Output will be of type int

# query = "Check if the following text is valid..."
# # Execute other functions as needed


from llm_wrapper import llm_func
from langchain_openai import OpenAI
import os

import openai

prompt = "Your Prompt Here"
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxx'
# print("key", OpenAI_key)

@llm_func
def famous_quote() -> str:
    """Returns a famous quote according to the subject provided."""
    pass

llm = OpenAI()
llm = openai.Completion.create(model_name="text-davinci-003",temperature=0.7,max_tokens=512,prompt=prompt, stop=None)

query = "Peace and War"
quote = famous_quote(llm=llm, query=query)
print(quote)  # Output: "Peace is not a relationship of nations. It is a condition of mind brought about by a serenity of soul. Peace is not merely the absence of war. It is also a state of mind. Lasting peace can come only to peaceful people. - Jawaharlal Nehru

@llm_func
def check_grammar() -> float:
    """Check the grammar of the sentence and return a float number between 0 and 1 reflecting its correctness."""
    pass

query = "I are a student."
correctness = check_grammar(llm=llm, query=query)
print(correctness)  # Output: 0.5
query = "I am a student."
correctness = check_grammar(llm=llm, query=query)
print(correctness)  # Output: 1.0