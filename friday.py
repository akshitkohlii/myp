import pyttsx3,datetime,speech_recognition,webbrowser,os
from subprocess import Popen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',130)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("GOOD MORNING")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")
    else: speak("GOOD EVENING")
    speak("how may I help you")

wishMe()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=5) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        return"Say That again please..."
    return str(query).lower()

while(True):
    query =  takeCommand()
    if (('search' in query) or ('google' in query)):
        query = query.replace('search', "").replace('google',"")
        webbrowser.open("https://google.com/search?q=%s" % query)
        
    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")

    elif 'open vs code' in query:
        Popen('E:\Microsoft VS Code\Code.exe')

    elif 'doc' in query:
        webbrowser.open("document.new")
    elif ('close browser' in query or 'close all browser' in query):
        os.system("taskkill /im firefox.exe /f")
        os.system("taskkill /im msedge.exe /f")
        os.system("taskkill /im chrome.exe /f")

    elif ('close vs code' in query):
        os.system("taskkill /im Code.exe /f")
    elif('open flipkart mini project' in query):
        webbrowser.open("http://127.0.0.1:8000/")
        os.system('cd C:\\Users\\Avnish Yadav\\Desktop\\flipkart\\ && python manage.py runserver')
    elif('shut down' in query or 'shutdown' in query):
        os.system("shutdown /s /t 3")
        break
    elif('open whatsapp' in query):
        webbrowser.open("https://web.whatsapp.com/")

    elif ('quit' in query or 'kill yourself' in query):
        speak('Going to sleep')
        break
    

    

    
    