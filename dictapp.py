import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty("voices")
#engine.getProperty("voice",voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp ={"paint":"paint", "word":"winword","excel":"excel","chrome":"chrome","vscode":"code","command promt":"cmd"}

def openappweb(query):
    speak("now launching")
    if ". com" in query or ".co.in" in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://www.(query)")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dictapp[app]}")



def closeappweb(query):
    speak("now closing")
    if "one tab" in query or " 1 tab " in query:
        pyautogui.hotkey("ctrl","w")

    elif " 2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs close")

    elif " 3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs close")

    elif " 4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs close")

    elif " 5  tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs close")


    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f/im {dictapp[app]}.exe")
