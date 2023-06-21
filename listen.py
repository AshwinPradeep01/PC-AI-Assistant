import speech_recognition as sr
from speak import speak
from utils import opening_text
from random import choice

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\nClearing the BG noise.Please Wait...!")
        r.adjust_for_ambient_noise(source,duration = 1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,phrase_time_limit=10)
        
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}")
        # speak(choice(opening_text))
    
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'

    query = str(query)
    return query.lower()

listen()

    