import pyttsx3  # pip install pyttsx3


def speak(Text):
    engine = pyttsx3.init('sapi5')  # object creation
    # pyttsx3 supports three TTS engine:
    # sapi5 - Windows
    # nsss - Mac OS
    # espeack - for other platform

    # These two lines will set jarvis voice, it's rate if device doesn't have it set
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 200)
    # say method on the engine that passing input text to be spoken
    print(f"\nJarvis : {Text}\n")
    engine.say(Text)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
