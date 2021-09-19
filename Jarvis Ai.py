import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    else:
        speak("Good Evening Boss!")
    speak("I am Jarvis Sir. Please tell me how may I help you") 


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Wait for a moment")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        #print(e)
        speak("Say that again please")
    return query    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            musicdir="E:\\Songs"
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir, songs[0]))

        elif 'open code' in query:
            codePath ="C:\\Users\\ashfa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath1 ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath1)
        
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(Time)

