import speech_recognition as sr
import pyttsx3 as p
from functions import *
import wikipedia
import webbrowser
import datetime
import pyjokes
import json
import subprocess
from urllib.request import urlopen


rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

r = sr.Recognizer()

# Main program loop
activation_phrase = "Hello harry"
while True:
    clear()
    wishMe()
    command = listen().lower()
    if activation_phrase.lower() in command:
        speak("Hi Heena! how are you?")
        speak("How can i assist you?")
        while True:
            command = listen().lower()
            if "what" in command and "about" in command and "you" in command:
                speak("I'm having a good day maam")
            elif "Goodbye" in command:
                speak("Goodbye maam")
                break
            else:
                if "information" in command or "wikipedia" in command:
                    speak("You need information related which topic maam?")
                    listen()
                    speak("Searching wikipedia")
                    command = command.replace("wikipedia","")
                    results = wikipedia.summary(command)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'open youtube' in command:
                    speak("Here you go to youtube")
                    webbrowser.open("youtube.com")
                elif 'open google' in command:
                    speak("Here you go to google")
                    webbrowser.open('google.com')
                elif 'play music' in command:
                    speak('playing music')
                elif 'time' in command:
                    Time = datetime.datetime.now().strftime("% H:% M:% S") 
                    speak(f"Sir the time is {Time}")
                elif 'joke' in command:
                    speak(pyjokes.get_joke())
                elif 'news' in command:
                    
                    try:
                        jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=ba5091fab2e448268d5b7191c775d475")
                        data = json.load(jsonObj)
                        i = 1
                        
                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============'''+ '\n')
                        
                        for item in data['articles']:
                            
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                        
                        print(str(e))
                elif 'email to Heena' in command:
                    try:
                        speak("What should i say")
                        listen()
                        to = "Receiver email address"
                        sendEmail(to,command)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("I m not able to send this email")
                elif 'send a mail' in command:
                    try:
                        speak("What should i say")
                        listen()
                        speak("Whom should i send the mail")
                        to = input()
                        sendEmail(to,command)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("I m not able to send this email")
                elif 'who are you' in command:
                    speak("I'm your voice assistant created by Heena")
                elif 'shutdown' in command:
                    speak("Hold on a second! Your system is on its way to shut down.")
                    subprocess.call('shutdown / p / f')
            try:
                print("Recognizing...")
            except sr.UnknownValueError:
                speak("Sorry, I didn't understand that. Can you please repeat?")
            except sr.RequestError:
                speak("Sorry, I couldn't reach the speech recognition service.")
    
    elif 'goodbye' in command or 'bye' in command:
        speak("Goodbye maam")
        break
    else:
        continue
