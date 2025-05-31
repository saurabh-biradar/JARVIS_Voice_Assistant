# Jarvis Virtual Assistant

### Jarvis is one such virtual assistant that uses a user's audio as input and responds to the query in audio version. Jarvis is named after Tony Stark's AI assistant in the Marvel Comics and movies. Jarvis is a software program that is designed to simulate human intelligence and perform tasks based on voice commands.
### The software program has the capability to understand natural language and respond to user queries in real-time. The software program has the potential to revolutionize the way we interact with our devices and make our lives easier.



## Hardware Requirements :-

| Hardware / Software  | Requirement |
| ------------- | ------------- |
| RAM  | 2GB  |
| Processor  | Intel Core i3 |
| Hard Disk  | 512 MB |
| Operating System | Microsoft Windows 7 or Higher |


## Installation

- Install Python v3.6 or higher
- pip install SpeechRecognition PyAudio pyttsx3 torch numpy nltk PyQt5 opencv-python wikipedia pyjokes pywhatkit python-decouple 
- To avoid jarvis stuck in listening mode update audio = r.listen(source, 0, 5) in Listen.py file
- Run following command in python file :- 
    nltk.download('punkt')

### After installing all these modules, update contact details in .env file
