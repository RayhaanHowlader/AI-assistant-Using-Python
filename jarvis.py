import datetime
import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary
import wikipedia
import webbrowser
import smtplib
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<15:
        speak("Good Aftertoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir Please Tell how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Youremail','Yourpassword')
    server.sendmail('Youremail',to,content)
    server.close()



d = PyDictionary()
def get_meaning(word):
    meaning = d.meaning(word)
    return meaning


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # Logic of excuting Tasks based on query
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")
        elif 'open try hack me' in query:
            speak("opening try hack me")
            webbrowser.open("tryhackme.com")
        elif 'the time' in query:
            sTrtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {sTrtime}")
        elif 'email to rehan' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "Youremail"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
        elif 'meaning' in query:
            query = query.replace('meaning','')
            meaning = get_meaning(query)
            print(meaning)
            speak(meaning)
        elif 'exit' in query:
            speak("Thanks for using jarvis ")
            speak("exiting...")
            break
        elif 'calculate' and '+' in query:
            query = query.replace('calculate','')
            query = query.split('+')
            results = int(query[0])+int(query[1])
            speak(f"The answer is {results}")
        elif 'calculate' and '-' in query:
            query = query.replace('calculate','')
            query = query.split('-')
            print(query)
            a = int(query[0])
            b= int(query[1])
            result = a-b
            print(result)
            speak(f"calculate is {result}")
        elif 'who are you' in query:
            speak("I am a simple ai assintant developed in python by rayhaan")

