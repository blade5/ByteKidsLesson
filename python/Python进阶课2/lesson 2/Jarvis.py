import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

MASTER = "Caihua"


# this function will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning " + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)

    # speak("I am Jarvis. How may i help you?")


def takeCommand():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
    try:
        audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        query = None
    return query


# Speak function will pronouce the string which is pased to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("harry@codewithharry.com", to, content)
    server.close()
# Main Program starts here..
#speak("Initializing Jarvis...")
def main():
    wishMe()
    query = takeCommand()

    # Logic for executing tasks
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentence=2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")
    elif 'play music' in query.lower():
        songs_dir = "musicDirectory"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H%M:%S")
        speak(f"{MASTER} the time is {strTime}")
    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'email to caihua' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "harry@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            speak("Say that again")

main()

