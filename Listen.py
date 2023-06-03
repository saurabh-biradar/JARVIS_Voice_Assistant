import speech_recognition as sr  # pip install speech_recognition

def Listen():
    r = sr.Recognizer()  # object creation
    with sr.Microphone() as source:  # use the default microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1
        # listen for the first phrase and extract it into audio data
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # recognize speech using Google Speech Recognition
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")
    except:
        return "Say that again please..."
    query = str(query)
    return query.lower()
