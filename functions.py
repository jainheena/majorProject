import pyttsx3 as p
import smtplib
import speech_recognition as sr
import datetime
import os


engine = p.init()
clear = lambda:os.system('cls')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
    speak("I am your Assistant")

def speak(text):
        engine.say(text)
        engine.runAndWait()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # enable low security in gmail
    server.login('Your email id','Your email password')
    server.sendmail('your email id',to,content)
    server.close()

r = sr.Recognizer()
def listen():
        with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source,1.2)
                print("Listening...")
                audio = r.listen(source)
        try:
                print("Recognizing...")
                query = r.recognize_google(audio,language='en-in')
                print("You said:", query)
                return query
        except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                return ""
        except sr.RequestError:
                print("Sorry, I'm unable to process your request.")
                return ""

