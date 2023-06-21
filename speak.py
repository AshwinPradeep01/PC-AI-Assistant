import pyttsx3
from decouple import config
# from utils import opening_text
# from random import choice
import datetime 

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    # print(voices)
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate', 180)
    engine.setProperty('volume',1.0)
        
    """speaks the text passed to it"""
    print("     ")
    print(f'Asterik: {text}')
    engine.say(text)
    engine.runAndWait()
    print("\n")

# speak('hello there')

def greetMe():
    """ Greets the user """
    hour = datetime.datetime.now().hour
    if (hour >= 6) and ( hour<12 ):
        speak(f"Good Morning {USERNAME}")
    
    elif (hour >= 12) and (hour <16):
        speak(f"Good Afternoon {USERNAME}")

    elif( hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")

    speak(f"{BOTNAME} here. How may i help you?")

# greetMe()