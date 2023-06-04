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
from decouple import config  # pip install python-decouple
from email.message import EmailMessage
import smtplib
from difflib import get_close_matches
import json

USERNAME = config('USER')
BOTNAME = config('BOTNAME')
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

patterns = []
mobileno = {}
emailAddress = {}
with open("contact.json", 'r') as json_data:
    data = json.load(json_data)
    patterns = data['patterns']
    mobileno = data['mobileno']
    emailAddress = data['emailAddress']


def greet_user():
    # Greets the user according to the time

    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(
            f"Good Morning {USERNAME}. I am {BOTNAME}, How may I assist you?")
    elif (hour >= 12) and (hour < 16):
        speak(
            f"Good afternoon {USERNAME}. I am {BOTNAME}, How may I assist you?")
    else:
        speak(
            f"Good Evening {USERNAME}. I am {BOTNAME}, How may I assist you?")


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
    video = Listen()
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


def send_email():
    try:
        speak("Who do you want to email")
        name = Listen()
        lst = get_close_matches(name, patterns)
        if(len(lst) <= 0):
            raise Exception(
                "Sorry, the person with this name doesn't exist in our database")
        name = lst[0]
        receiver_address = emailAddress[name]
        email = EmailMessage()
        speak("Please tell me subject of the Email")
        subject = Listen()
        speak("What should I say in Email")
        message = Listen()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        webbrowser.open("https://mail.google.com/mail/u/0/#sent")
        speak("Email has been sent sucessfully!")
        return True
    except Exception as e:
        speak(e)
        return False


def get_weather_report():
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=pune&appid={OPENWEATHER_APP_ID}").json()
    weather = res["weather"][0]["description"]
    temperature = round(float(res["main"]["temp"]) - 273.15, 2)
    feels_like = round(float(res["main"]["feels_like"]) - 273.15, 2)
    speak(
        f"It is {weather} in Pune city. Temperature is {temperature}℃ , but it feels like it is {feels_like}℃.")


def send_whatsapp_message():

    try:
        speak("Who do you want to message")
        name = Listen()
        lst = get_close_matches(name, patterns)
        if(len(lst) <= 0):
            raise Exception(
                "Sorry, the person with this name doesn't exist in our database")
        name = lst[0]
        number = mobileno[name]
        speak("Alright, what's the message")
        message = Listen()
        kit.sendwhatmsg_instantly(f"+91{number}", message, 15, True)
        # kit.sendwhatmsg_to_group_instantly("DcD72OzBGamIg9K3QUZBPi", "Hi everyone", 15, True)
    except Exception as e:
        speak(e)
    speak("Message sent successfully!")


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
        case "_send_email":
            send_email()
        case "_send_whatsapp_message":
            send_whatsapp_message()
        case "_greet_user":
            greet_user()
        case "_get_weather_report":
            get_weather_report()
