import os
import wikipedia
import pyjokes
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modules')))
from Modules import Voice_interaction
from Modules.Voice_interaction import say, takeCommand
from Modules.AI import ai, chat
from Modules import time_utilities
from Modules import web_utilities


Wake_word = "Jarvis"


def main():
    print('Jarvis AI...')
    Voice_interaction.say("Hello I am Jarvis your Virtual assistant..")

    while True:
        print("Listening...")
        query = takeCommand()
        print("Responding..")

        sites = [
            ["youtube", "https://youtube.com"],
            ["wattpad", "https://wattpad.com"],
            ["wikipedia", "https://wikipedia.com"],
            ["google", "https://google.com"]
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                Voice_interaction.say(f"Opening {site[0]} Madam...")
                web_utilities.open_website(site[1])

        if "music" in query:
            musicPath = '/Users/kairabarot/Desktop/Krishna.mp3'
            os.system(f"open {musicPath}")

        elif "wikipedia" in query:
            Voice_interaction.say("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=7)
            print(result)
            Voice_interaction.say(result)

        elif "the time" in query:
            Voice_interaction.say(time_utilities.get_time())

        elif "open FaceTime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app ")

        elif "Using artifical intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "joke" in query:
            say(pyjokes.get_joke())

        elif "open code" in query:
            codepath = "/Volumes/My Passport/PYcharm projects/Jarvis A.I/main.py"
            os.startfile(codepath)

        elif "Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
            Voice_interaction.say(query)  # properly indented

if __name__ == '__main__':
    main()