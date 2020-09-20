import pyttsx3 #pip install pyttsx3 ---> for voice
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia ---> to get wikipedia content
import webbrowser  # ---> for opening browser links
import os     #---> local operating disc
import smtplib  #---> for sending emails
from random import randint

engine = pyttsx3.init('sapi5')
male_voice = engine.getProperty('voices')
engine.setProperty('voice', male_voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning!")

    elif hr>=12 and hr<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Karan. Please tell me how may I help you")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karan.kk7575@gmail.com', 'my-password')
    server.sendmail('karan.kk7575@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            #change directory according to music folder
            music_dir = 'C:\\Users\\Documents\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            random_num = randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.date.today()
            print(f"The date is {strDate}")
            speak(f"The date is {strDate}")

        elif 'open code' in query:
            codePath = "C:\\Users\\I531722\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Karan' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "karan.kk7575@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'quit' in query:
            print("Karan is quiting...")
            speak("Karan is quiting")
            exit()
 