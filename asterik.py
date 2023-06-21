import random 
import json
import torch
from brain import neuralNet
from neuralnetwork import bag_of_words,tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)
    

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = neuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#---------------------------------------------------------------------------------#
Name = "Asterik"

from listen import listen
from speak import speak
from speak import *
from tasks import *
from pprint import pprint

if __name__ == "__main__":

    greetMe()

    while True:

        sentence = listen().lower()

        sentence = tokenize (sentence) 
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1,X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)

        _ , predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim =1)
        prob = probs[0][predicted.item()]

        
        if prob.item()>0.75 :
            for intent in intents['intents']:
                if tag == intent['tag']:
                    reply = random.choice(intent['responses'])
                    if tag == 'parting':
                        hour = datetime.now().hour
                        if hour >= 21 and hour < 6:
                            speak("Goodnight sir, take care!")
                        else:
                            speak("Call me when in need sir! ")
                            speak(reply)
                            exit()

                    if "time" in reply:
                        NonInputExecution(reply)

                    elif "good night" in sentence:
                        speak(f"Goodnight {USERNAME}")
                        speak("shall i shut down sir?")
                        reply1 = listen()
                        if "yes" in reply1:
                            exit()

                    elif "date" in reply:
                        NonInputExecution(reply)

                    elif "day" in reply:
                        NonInputExecution(reply)
                    
                    elif 'ip address' in reply:
                        ip_address = find_my_ip()
                        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                        print(f'Your IP Address is {ip_address}')

                    elif "wikipedia" in reply:
                        Wikipedia(sentence)
                    
                    elif "whatsapp" in reply:
                        speak("Whom do you want to sent the text")
                        name_ = str(input("Name:")).lower()
                        speak("What's the message sir?")
                        msg = listen()
                        Whatsapp(name_,msg)

                    elif "youtube" in reply:
                        speak('What do you want to play on Youtube, sir?')
                        video = listen().lower()
                        play_on_youtube(video)

                    elif "google search" in reply:
                        search_on_google(sentence)

                    elif "weather" in reply:
                        ip_address = find_my_ip()
                        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                        speak(f"Getting weather report for your city {city}")
                        weather, temperature, feels_like = get_weather_report(city)
                        speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                        speak(f"Also, the weather report talks about {weather}")
                        speak("For your convenience, I am printing it on the screen sir.")
                        print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

                    elif "music" in reply:
                        lang = listen().lower()
                        path = f"C:\\Users\\ashwi\\Music\\Songs\\{lang}\\*.mp3"
                        music_playlist(path)

                    elif "email" in reply:
                        speak("On what email address do I send sir? Please enter in the console: ")
                        receiver_address = input("Enter email address: ")
                        speak("What should be the subject sir?")
                        subject = listen().capitalize()
                        speak("What is the message sir?")
                        message = listen().capitalize()
                        if send_email(receiver_address, subject, message):
                            speak("I've sent the email sir.")
                        else:
                            speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

                    elif "alarm" in reply:
                       alarm()

                    elif "news" in reply:
                       get_latest_news()    

                    elif "jokes" in reply:
                        speak(f"Hope you like this one sir")
                        joke = get_random_joke()
                        speak(joke)
                        # speak("For your convenience, I am printing it on the screen sir.")
                        # pprint(joke)

                    elif "remind message" in reply:
                        remind_message(sentence)

                    elif "reminder" in reply:
                        reminder()

                    elif 'camera' in reply:
                        open_camera()
       
                    else:
                        speak(reply)

          











