from openai import OpenAI
from config import API_KEY
client = OpenAI(api_key=API_KEY)
import os
from Voice_interaction import say

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n ************************* \n\n"
    response = client.completions.create(model="text-davinci-003",
    prompt=prompt,
    temprature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

    #todo: Wrap this in try and catch block
    #print(response ["choice"][0]["text"])
    text += response.choice[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #with open (f"Openai/Prompt- {random.randint(1,23976249)}","w") as f:
    with open (f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt","w") as f:
        f.write(text)
    print(response)

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Kashish: {query}\n Jarvis: "
    response = client.completions.create(model="text-davinci-003",
    prompt=chatStr,
    temprature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

    #todo:wrap in try and catch block
    say(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text