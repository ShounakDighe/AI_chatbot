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
from colorama import init, Fore, Style
init(autoreset=True)

sys.path.append('/home/shounak/Documents/Fundamentals-of-ds/c_programs')

from AI_chatbot.custom_voice import speak

def animate_text(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    styles = [Style.NORMAL, Style.BRIGHT]
    
    for style in styles:
        for color in colors:
            print(f"{style}{color}{text}")



engine = gTTS(text="Hello, I am ACE", lang="en", slow=False)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)



def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-IN")
            print("User said:", command)
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
        speak("Welcome back Shounak Sir, Good Morning!")
    elif 12 <= hour < 18:
        speak("Welcome back Shounak Sir, Good Afternoon!")
    else:
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
speak("Say 'hey man' to wake me up.")

wakeup_command = "hey man"
sleep_command = "exit"
listening = False 
while True:
    command = take_command()

    if listening:
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
    
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

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

    
        elif 'open note' in command:
            speak("Just a sec opening gedit")
            os.system("gedit &")
        elif 'close note' in command:
            os.system("pkill gedit")
            speak("Gedit is closed")
    
        elif 'open v s' in command:
            speak("Just a sec openning Visual Studio Code")
            os.system("code")
        elif 'close v s' in command:
            os.system("pkill code")
            speak("Visual Studio Code is closed")

        elif 'open' in command:
            website = command.replace('open', '')
            webbrowser.open(website)


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

        else:
            speak('Sorry,can you repeat it again!!')  
    
    if wakeup_command in command.lower():
        speak("Hello Shounak, how can I help you?")
        listening = True                 