from datetime import datetime
from gettext import find
from glob import glob
from unittest import result
from urllib.parse import quote_from_bytes
from winsound import PlaySound
from decouple import config
from email.message import EmailMessage
import smtplib

from bs4 import BeautifulSoup
from flask import Config
from speak import speak #,USERNAME
from listen import listen
import requests  #used for requests from server
import wikipedia
import pywhatkit as kit
from time import sleep
import webbrowser
import pyautogui
import keyboard
import subprocess as sp

from playsound import playsound



def Time():
    now = datetime.now()
    time = now.strftime("%H:%M")
    speak(time)

def Date():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    speak(date)

def Day():
    now = datetime.now()
    day =  now.strftime("%A")
    speak(day)
    

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json').json()
    return ip_address["ip"]

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    sleep(4)
    # keyboard.press_and_release('space')

    while True:
        query = listen()
        if not "quit" in query:
        

            if "take" in query:
                sleep(2)
                keyboard.press_and_release('space')

            elif "video" in query:
                sleep(2)
                keyboard.press_and_release('up')

            elif "photo" in query:
                sleep(2)
                keyboard.press_and_release('down')

#Input type

def Wikipedia(query):
   
        query = str(query).replace("wikipedia","")
        try:
            # speak("how many sentences do you need sir")
            # no_of_lines = int(listen())
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        # return results
        except:
            print("Page not found")

    
def Whatsapp(name_,msg):
        webbrowser.open('https://web.whatsapp.com/')
        sleep(15)
        pyautogui.click(x=305, y=253)
        sleep(0.5)

        # msg = 'hello there automation testing'
        # name_ = 'pranesh'

        keyboard.write(name_)
        sleep(1)

        pyautogui.click(x=298, y=419)
        sleep(1)

        keyboard.write(msg)

        query = listen()

        if "send" in query:
            keyboard.press_and_release('enter')

        else:
            exit()

def play_on_youtube(video_name):
   kit.playonyt(video_name)


def search_on_google(query):
    kit.search(query)


OPENWEATHER_API_ID = config("OPENWEATHER_API_ID")

def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    # print(f"{temperature}℃", f"{feels_like}℃")
    return weather, f"{temperature}℃", f"{feels_like}℃"


def music_playlist(path):
    for song in glob(path):
        print("Playing..."+song)
        playsound(song)



# def send_email(receiver_address, subject, message):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email ['From'] = EMAIL
#         email.set_content(message)
#         content = email.get_content(message)
#         print(content)
#         s = smtplib.SMTP("smtp.gmail.com", 587)
#         s.starttls()
#         s.login(EMAIL,PASSWORD)
#         s.sendmail(EMAIL,receiver_address,message)
#         s.close()
#         return True
#     except Exception as e:
#         print(e)
#         return False

# send_email('ashwinpradeep01@gmail.com','testing',message)

def alarm():
    speak("Enter the time please")
    time = input("A:|Time (24hrs format):")

    while True:
        Time_curr = datetime.now()
        now = Time_curr.strftime("%H:%M:%S")
        if now == time:
            speak('Time to wakeup sir!')
            print("Playing the song")
            playsound('pirates_of_caribbean.mp3')
            speak('ALARM OFF!')
            sleep(5)
        
        if now>time:
            break




NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])    
    # for news in news_headlines:
    #     print(news)
    str = " \n ".join(news_headlines[:5])
    speak(str)
    return news_headlines[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def remind_message(query):
    print(query)
    remindMsg = query.remove('remind')
    remindMsg = remindMsg.remove('Asterik')
    speak("You want me to remind you that:"+remindMsg)
    remind = ('remind.txt','w')
    remind.write(remindMsg)
    remind.close()

def reminder():
    remindMsg = open('remind.txt','r')
    speak('Reminder:'+remindMsg)


EMAIL = config('EMAIL')
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
subject="Test email"
message = """ hello hi this is email testing  for the virtual assistant"""
RECEIVER = "ashwinpradeep01@gmail.com"
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(USERNAME,PASSWORD)
    print("login successful/logged in")
    server.sendmail(EMAIL,RECEIVER,message)
    print("Email has been sent to", RECEIVER)
    server.quit()

    


















































# #from random import choice
# # for mood in Music_dic:
# #   if mood == pred_emotion:
#         audio = choice(Music_dict[pred_emotion])
#         os.startfile(audio)
        

# Music_dict={
#     "Happy":["Music\\Happy\\Damakku_Damakku.mp3", 
#           "Music\\Happy\\Friendship_Anthem.mp3","Music\\Happy\\Mental_Manadhil.mp3","Music\\Happy\\Private_Party.mp3","Music\\Happy\\Mustafaa_Mustafaa.mp3"] ,
#     "Sad":["Music\\Sad\\Mella_Vidaikodu.mp3",
#         "Music\\Sad\\Pogathe.mp3", 
#         "Music\\Sad\\Kaadal_Endral.mp3","Music\\Sad\\EnIniyaThanimaiyae.mp3","Music\\Sad\\Usure.mp3"] ,
#     "Calm":["Music\\Calm\\Naan_Pizhai.mp3",
#           "Music\\Calm\\Moongil_Thottam.mp3","Music\\Calm\\Thendral_Vanthu.mp3","Music\\Calm\\Malargal_Kaetaen.mp3","Music\\Calm\\Aanantha_Yazhai.mp3"] ,
#     "Excited":["Music\\Excited\\Jalabula_Jung.mp3",
#             "Music\\Excited\\Jai_Sulthan.mp3","Music\\Excited\\Rowdy_Baby.mp3","Music\\Excited\\AadungadaYennaSuthi.mp3","Music\\Excited\\Aaluma_Doluma.mp3"]}


        
