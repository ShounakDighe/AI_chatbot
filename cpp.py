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

engine = gTTS(text="Hello, I am an ACE", lang="en", slow=False)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

def speak(text, slow=True):
    engine = gTTS(text=text, lang="en", slow=slow)
    engine.save("temp.mp3")
os.system("xdg-open temp.mp3")  

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
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
speak("Namaskar Mi tumchi khasi madat karu sahtke ? ")

while True:
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    
    elif 'open' in command:
        website = command.replace('open', '')
        webbrowser.open(website)
    
    elif 'weather' in command:
        speak("Please provide the name of the city")
        city = take_command()
        weather = python_weather.weather.Weather(unit='C')
        location = weather.lookup_by_location(city)
        condition = location.condition.text
        temperature = location.condition.temp
        speak(f"The weather in {city} is currently {condition} with a temperature of {temperature} degrees Celsius.")
    
   
    
    elif 'exit' in command:
        speak("Goodbye!")
        sys.exit()
    
    else:
        speak('Sorry! awaj nai aala parat bola')

speak("Namaskar Mi tumchi khasi madat karu sahtke ? ")
