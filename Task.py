import datetime
import webbrowser
import os
import cv2
from Speak import speak


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
    webbrowser.open("www.youtube.com")

def facebook():
    webbrowser.open("www.facebook.com")

def linkdin():
    webbrowser.open("www.linkdin.com")

def twitter():
    webbrowser.open("www.twitter.com")

def command_prompt():
    os.system("start cmd")

def camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret,img = cap.read()
        cv2.imshow('webcam',img)
        k = cv2.waitKey(50)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows()

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
        case "_linkdin":
            linkdin()
        case "_twitter":
            twitter()
        case "_cmd":
            command_prompt()
        case "_camera":
            camera()
