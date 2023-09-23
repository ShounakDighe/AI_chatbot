import datetime
import speech_recognition as sr
from gtts import gTTS
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import python_weather
import os
import smtplib
import sys
from time import sleep
sys.path.append('/home/shounak/Documents/Fundamentals-of-ds/c_programs')

from AI_chatbot.custom_voice import speak

engine = gTTS(text="Hello, I am ACE", lang="en", slow=False)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)



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

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


wishme()
speak(" Hello Shounak,How can I help you ? ")

wakeup_command = "hey man"
sleep_command = "sleep"
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
            command = command.replace('wikipedia', '')
            info = wikipedia.summary(command, sentences=2)
            print(info)
            speak(info)

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

        elif 'weather' in command:
            speak("Please provide the name of the city")
            city = take_command()
            weather = python_weather.weather.Weather(unit='C')
            location = weather.lookup_by_location(city)
            condition = location.condition.text
            temperature = location.condition.temp
            speak(f"The weather in {city} is currently {condition} with a temperature of {temperature} degrees Celsius.")
        
        elif 'spotify' in command:    
            playlist_uri = 'https://open.spotify.com/playlist/4q52Yjq4F0ZACxwJx6XxnU?si=89080a3b0db34a68'
    
            os.system(f'spotify --uri {playlist_uri}')
    
        elif 'open note' in command:
            speak("Just a sec opening gedit")
            os.system("gedit &")
        elif 'close note' in command:
            os.system("pkill gedit")
            speak("Gedit is closed")
    
        elif 'open code' in command:
            speak("Just a sec openning Visual Studio Code")
            os.system("code")
        elif 'close code' in command:
            os.system("pkill code")
            speak("Visual Studio Code is closed")

        elif 'open' in command:
            website = command.replace('open', '')
            webbrowser.open(website)


        elif 'exit' in command:
            speak("Goodbye!")
            sys.exit()

        elif 'shutdown' in command:
            speak('Logging out in 10 second')
            sleep(10)
            os.system("shutdown /s /t 1")

        elif 'restart' in command:
            speak('Restarting out in 10 second')
            sleep(10)
            os.system("shutdown /r /t 1")


        else:
            speak('Sorry,can you repeat it again!!')

            
    # Check for the wake-up command
    if wakeup_command in command.lower():
        speak("Hello Shounak, how can I help you?")
        listening = True
        
    # Check for the sleep command
    if sleep_command in command.lower():
        speak("Going to sleep. Wake me up when you need assistance.")
        listening = False
        