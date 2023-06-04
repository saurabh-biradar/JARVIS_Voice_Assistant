import datetime
import webbrowser
import os
import cv2
import wikipedia
from Speak import speak
from requests import get
from Listen import Listen
import pyjokes  # pip install pyjokes
import pywhatkit as kit
import pyautogui
import random
import requests
from bs4 import BeautifulSoup


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(time)


def Date():
    date = datetime.date.today()
    speak(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(day)


def youtube():
    speak("opening the youtube")
    speak("sir,which video i need to play")
    video = Listen.Listen()
    kit.playonyt(video)


def facebook():
    speak("opening the facebook")
    webbrowser.open("www.facebook.com")


def linkedin():
    speak("opening the linkedin")
    webbrowser.open("www.linkedin.com")


def twitter():
    speak("opening the twitter")
    webbrowser.open("www.twitter.com")


def google():
    speak("What should I search on google")
    query = Listen()
    kit.search(query)


def command_prompt():
    speak("opening the command prompt")
    os.system("start cmd")


def camera():
    speak("opening the camera")
    cap = cv2.VideoCapture(0)
    img_counter = 0
    speak("press space button to take the photo and press Escape button to close camera")
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            speak("Escape hit,closing the app")
            break
        elif k % 256 == 32:
            img_name = f"opencv_fram_{img_counter}.png"
            cv2.imwrite(img_name, img)
            speak("image is captured")
            img_counter += 1
    cap.release()
    cv2.destroyAllWindows()


def wikipedia_search():
    speak("What should i search on Wikipedia...")
    query = Listen()
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    speak(results)


def ipaddress():
    ip = get('https://api.ipify.org').text
    speak(f"your IP address is {ip}")


def joke():
    joke = pyjokes.get_joke()
    speak(joke)


def alarm():
    nn = int(datetime.datetime.now().hour)
    speak("for what time i need to set alarm")
    tm = Listen()
    if nn == tm:
        music_dir = "E:\\music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))


def shutdown():
    speak("sir, turning off the system")
    os.system("shutdown /s /t 5")


def restart():
    speak("sir, restarting the system")
    os.system("shutdown /r /t 5")


def screenshot():
    speak("sir,please tell me the name for this screenshot file")
    name = Listen()
    speak("please hold the screen for few seconds, I am taking screenshot")
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("I am done sir, the screenshoot is saved in our main folder.now i am ready for next command")


def music():
    speak("playing the song")
    music_dir = 'E:\\music'
    songs = os.listdir(music_dir)
    no = random.randint(0, 4)
    os.startfile(os.path.join(music_dir, songs[no]))


def movies():
    speak("playing the movie")
    video_dir = 'E:\\movies'
    movies = os.listdir(video_dir)
    os.startfile(os.path.join(video_dir, movies[0]))


def notepad():
    speak("opening the notepad")
    npath = "C:\windows\system32\\notepad.exe"
    os.startfile(npath)


def vol_up():
    pyautogui.press("volumeup")


def vol_down():
    pyautogui.press("volumedown")


def NonInputExecution(query):
    query = str(query)

    match query:
        case "_time":
            Time()
        case "_date":
            Date()
        case "_day":
            Day()
        case "_youtube":
            youtube()
        case "_facebook":
            facebook()
        case "_linkedin":
            linkedin()
        case "_twitter":
            twitter()
        case "_google":
            google()
        case "_cmd":
            command_prompt()
        case "_camera":
            camera()
        case "_wikipedia":
            wikipedia_search()
        case "_ipaddress":
            ipaddress()
        case "_joke":
            joke()
        case "_alarm":
            alarm()
        case "_shutdown":
            shutdown()
        case "_restart":
            restart()
        case "_screenshot":
            screenshot()
        case "_music":
            music()
        case "_movies":
            movies()
        case "_notepad":
            notepad()
        case "_volumeup":
            vol_up()
        case "_volumedown":
            vol_down()
