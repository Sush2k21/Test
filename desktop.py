import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import webbrowser
import os
import random
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)  # Set property for voice... 0 for male 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    if hour>=12 and hour<18:
        speak("Good Noon")
    if hour>=18 and hour<24:
        speak("Good evening")

def takeCommand():
    '''it takes input through microphone and return output as string'''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=3
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)   
    server.ehlo()
    server.starttls()
    # f=open("pass.txt","w+")
    server.login('elsagpta1010@gmail.com','')
    server.sendmail('elsagpta1010@gmail.com',to,content)
    server.close()


if __name__=='__main__':
    speak("Hello Sushmita")
    wishMe()
    # takeCommand()
    # query=takeCommand().lower()
    query="jarvis email to sushmita"
    
    if 'wikipedia' in query:
        speak('Searching wikipedia....')
        query=query.replace('wikipedia',"")
        result=wikipedia.summary(query,sentences=2)
        speak('according to wikipedia')
        speak(result)
    
    if 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")
    
    if 'open google' in query:
        webbrowser.open("google.com")
    
    if 'play music' in query:
        music_dir='F:\Songs'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[random.randint(0,30)]))
    
    if 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is:{strTime}")

    if 'open code' in query:
        codepath="C:\\Users\\Anonymous\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    if 'email to sushmita' in query:
        try:
            print('What should i say?')
            content=" "
            to="abhijeet.gpta12@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry my friend. It is unable to send")

    if 'open gmail' in query:
        webbrowser.open("gmail.com")
    
    if 'open git' in query:
        path="C:\Program Files\Git\git-bash.exe"
        os.startfile(path)

    # if 'open whatsapp' in query:
    #     path="C:\Users\Anonymous\AppData\Local\WhatsApp\WhatsApp.exe"
    #     os.start(path)
        

