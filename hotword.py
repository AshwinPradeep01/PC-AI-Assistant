import os
import speech_recognition as sr
from time import sleep
import speak
def listen():
    r = sr.Recognizer()
    
    r.pause_threshold = 5
    with sr.Microphone() as source:
        print("\n\nClearing the BG noise.Please Wait...!")
        r.adjust_for_ambient_noise(source,duration = 0.5)
        print("HOTWORD PLEASE...")
        audio = r.listen(source,0,phrase_time_limit=4)
        
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}")
        # speak(choice(opening_text))
    
    except Exception:
        # speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'

    query = str(query)
    return query.lower()

if __name__ == "__main__":   

        hotword = listen().lower()

        if "asterik" or "asterisk" or"astrix"or "wake up" in hotword:
            print("Hotword Detected!")
            sleep(2)
            os.startfile("D:\\Major Project\\Friday\\main.py")
        
        else:
            print('hotword not detected.pls try again')
            
         
             

