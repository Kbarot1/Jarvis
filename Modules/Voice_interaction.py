import speech_recognition as sr
import pyttsx3
import os
import sys


def takeCommand():
    # Takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

        # todo:test the errors.
        try:
            say("ok")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Listening timeout. No speech detected.")
            return "a"
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return "b"
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
            sys.exit(0)  # Exit the program:
        except Exception as e:
            return "ERROR!"


def say(text):
    os.system(f"say {text}")