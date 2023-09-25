# Imported lib from the pip 
import datetime
import speech_recognition as sr
from gtts import gTTS
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import os
import sys
from time import sleep
import subprocess
from playsound import playsound
from colorama import init, Fore, Style
import threading
from bs4 import BeautifulSoup
import requests
from pywikihow import search_wikihow
import pyautogui

init(autoreset=True)

sys.path.append('/home/shounak/Documents/Fundamentals-of-ds/c_programs')

from custom_voice import speak

def animate_text(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    styles = [Style.NORMAL, Style.BRIGHT]
    
    for style in styles:
        for color in colors:
            print(f"{style}{color}{text}")

thread_lock = threading.Lock()

engine = gTTS(text="Hello, I am ACE", lang="en", slow=False)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)



def take_command():
    try:
        with sr.Microphone() as source:            
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing")
            command = recognizer.recognize_google(audio, language="en-IN")
            print("User said:", command)
            with thread_lock:
                return command.lower()
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    return ""

animate_text("Hello, I am ACE")

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        playsound("/home/shounak/Downloads/Startup Sound.mp3")
        speak("Welcome back Shounak Sir, Good Morning!")
    elif 12 <= hour < 18:
        playsound("/home/shounak/Downloads/Startup Sound.mp3")
        speak("Welcome back Shounak Sir, Good Afternoon!")
    else:
        playsound("/home/shounak/Downloads/Startup Sound.mp3")
        speak("Welcome back Shounak Sir, Good Evening!")

def play_spotify_playlist():
    try:
        subprocess.run(["spotify", "--uri", "https://open.spotify.com/playlist/2L8OHyMte0Msmt78ifX2SU?si=4fc854915d5b48d5"])
        speak("Playing the Spotify playlist.")
    except Exception as e:
        speak("An error occurred while trying to play the playlist.")


    except Exception as e:
        speak("An error occurred while trying to play the playlist.")

wishme()
speak("Say activate to wake me up.")

wakeup_command = "activate"
sleep_command = "exit"
listening = False 

wakeup_command = "activate"
sleep_command = "exit"
listening = False 

def listen_for_commands():
    global listening
    

    while True:
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "hey woman" in command:
            speak("listening sir")
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif "how to" in command:
            try:
                speak("Getting Data...")
                op = command.replace("mark","")
                max_result=1
                how_to=search_wikihow(op,max_result)
                assert len(how_to)==1
                how_to[0].print()
                speak(how_to[0].summary)

            except:
                speak("Say it correctly")

        elif 'wikipedia' in command:
            speak("Searching...")
            query = command.replace('wikipedia', '')
            try:
                info = wikipedia.summary(query, sentences=2)
                print(info)
                speak(info)
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I couldn't find any information about {query} on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Multiple results found for {query}. Please specify your search.")
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f'Today is {current_date}')

        elif 'who are you' in command:
            speak('I am an Artificial Conversation entity and I was developed by MANAS , SHOUNAK , YASHVARDHAN  , SIDDESH  ')

        elif 'are you single' in command:
            speak('I am in a relationship with wifi')

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'spotify' in command:    
            play_spotify_playlist()

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open github' in command:
            webbrowser.open("https://github.com")

        elif 'open note' in command:
            speak("Just a sec opening gedit")
            os.system("gedit &")
        elif 'close note' in command:
            os.system("pkill gedit")
            speak("Gedit is closed")

        elif 'open vs code' in command:
            speak("Just a sec openning Visual Studio Code")
            os.system("code")
        elif 'close vs code' in command:
            os.system("pkill code")
            speak("Visual Studio Code is closed")

        elif 'open' in command:
            website = command.replace('open', '')
            webbrowser.open(website)

        elif "remind me" in command:
            rememberMsg = command.replace("remember that","")
            rememberMsg = rememberMsg.replace("mark","")
            speak("you tell me to remind:" + rememberMsg)
            remember = open("data.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in command:
            remember= open("data.txt","r")
            speak("you tell me to remind"+remember.read())

        elif "news" in command:
            speak("reading news")
            try:
               type=command
               if type == "business news":
                   type="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d2705285623b4bfab2c9f1ad9e827687"
               elif type == "top news" or type == "news":
                   type="https://newsapi.org/v2/top-headlines?country=in&apiKey=d2705285623b4bfab2c9f1ad9e827687"
               elif type == "health news":
                   type="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=d2705285623b4bfab2c9f1ad9e827687"
               elif type == "science news":
                   type="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d2705285623b4bfab2c9f1ad9e827687"
               elif type == "sports news":
                   type="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d2705285623b4bfab2c9f1ad9e827687"
               elif type == "technology news":
                   type="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d2705285623b4bfab2c9f1ad9e827687"      
               main_news = type
               news = requests.get(main_news).json()
               article = news["articles"]
               news_article = []
               link=news["articles"]
               link_url=[]
               for arti in article:
                   news_article.append(arti["title"])
                   link_url.append(arti["url"])
               for i in range(5):
                   print(i + 1, news_article[i])
                   print(link_url[i])
                   speak(news_article[i])
            except Exception as e:
                print(e)
        
        elif "temperature" in command:
            search="tempeature in pune"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"{search} is {temp}")

        elif "volume up" in command or "increase" in command:
            pyautogui.press("volumeup")

        elif "volume down" in command or "decrease" in command:
                pyautogui.press("volumedown")

        elif "volume mute" in command or "mute" in command:
                pyautogui.press("volumemute")

        elif "pause video" in command:
                pyautogui.press("k")

        elif "start" in command:
                pyautogui.press("k")

        elif "last" in command:
                pyautogui.press("shift" + "p")

        elif "next" in command:
                pyautogui.press("end")

        elif "forward" in command:
                pyautogui.press("right")

        elif "backward" in command:
            pyautogui.press("left")

        elif 'finish' in command:
            speak("Goodbye!")
            sys.exit()
        
        elif 'shutdown' in command:
            speak('Logging out in 10 second')
            sleep(10)
            os.system("shutdown -h +1")

        elif 'restart' in command:
            speak('Restarting out in 10 second')
            sleep(10)
            os.system("shutdown -r +1")

        elif sleep_command in command.lower():
            speak("Going to sleep. Wake me up when you need assistance.")
            listening = False

        elif wakeup_command in command.lower():
            speak("Hello Shounak, how can I help you?")
            listening = True

        


if __name__ == "__main__":
    listen_for_commands()


listening_thread = threading.Thread(target=listen_for_commands)
listening_thread.daemon = True
listening_thread.start()                 