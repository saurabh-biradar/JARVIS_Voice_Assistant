import datetime
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


def NonInputExecution(query):
    query = str(query)

    match query:
        case "_time":
            Time()
        case "_date":
            Date()
        case "_day":
            Day()
