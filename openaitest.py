import os
import openai
from config import API_KEY


openai.api_key = API_KEY

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="",
    temprature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)