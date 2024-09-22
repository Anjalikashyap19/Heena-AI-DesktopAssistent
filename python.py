import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from browser import *
from YT_audio import *
import randfacts
import datetime
from shorts import *
import pywhatkit
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


today_date = datetime.datetime.now()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am Hena. your voice assistant")
    speak(
        "today is "
        + today_date.strftime("%d")
        + " of "
        + today_date.strftime("%B")
        + " and its currently "
        + (today_date.strftime(" %I "))
        + (today_date.strftime(" %M "))
        + (today_date.strftime("%p"))
    )
    speak("what can i do for you")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kumarsarwan1931@gmail.com", "19312817")
    server.sendmail("kumarsarwan1931@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    # takecommand()
    # speak("hello mam")
    wish()
    while True:
        if 1:
            query = takecommand().lower()

        # task

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            speak("opening notepad")

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("opening command prompt")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(2)
                if k == 5:
                    break

            cap.release()
            cv2.destroyAllWindows()
            speak("opening camera")

        elif "play music" in query:
            music_dir = "C:\\Users\\anjal\\Music\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music")

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:

            speak("what should i search on wikipedia")
            query = query.replace("wikipedia", "")
            query = takecommand().lower()
            result = wikipedia.summary(query, sentences=2)
            speak("accourding to wikipedia..")
            print(result)
            speak(result)

        elif "open youtube" in query:
            # webbrowser.open("www.youtube.com")
            speak("what you want to search ")
            speak("opening youtube...")
            query = query.replace("youtube", "")
            query = query.replace("youtube search", "")
            query = takecommand()
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("this is what you want")

        elif "open google" in query:
            import wikipedia as googlescrap

            speak("mam, what should i search on google")
            query = query.replace("open google", "")
            query = query.replace("google", "")

            query = takecommand().lower()

            try:
                pywhatkit.search(query)
                result = googlescrap.summary(query, 1)
                speak(result)

            except:
                speak("no speakable output available")

        elif "temperature" in query:
            search = "temprature in chennai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak("current{search} is {temp}")

        elif "send message " in query:
            kit.sendwhatmsg(
                "+918877229213", "hello i am hena developed by anjali", 11, 4
            )

        elif "email to suman" in query:
            try:
                speak("what should i type")
                content = takecommand().lower()
                to = "kumarsarwan1931@gmail.com"
                sendEmail(to, content)
                speak("email has been send to suman")

            except Exception as e:
                print(e)
                speak("sorry mam ,i am not able to send this email to suman")

        elif "information" in query:
            speak("you need information related to which topic?")
            query = takecommand()

            speak("searching {} on google".format(query))
            assist = infowl()
            assist.get_info(query)

        elif "play" and "video" in query:
            speak("you want to play which video")
            query = takecommand()

            speak("playing {} on youtube".format(query))
            assist = music()
            assist.get_info(query)

        elif "fact" and "facts" in query:
            speak("yes sure, ")
            x = randfacts.getFact()
            print(x)
            speak("did you know that, " + x)

        elif "shots" in query:
            speak("playing shorts video on youtube")
            assist = shorts()
            assist.get_info("beliver")

        elif "no thanks" in query:
            speak("thanks for using me mam , have a good day.")
            sys.exit()

        speak("mam,do you have any other query")
