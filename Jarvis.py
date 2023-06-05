from Listen import Listen
import sys
import time
from Speak import speak
import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Task import NonInputExecution
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import Loader
from JarvisUi import Ui_JarvisVirtualAssistent

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        speak("Sir, Please give your command")
        while(True):
            self.Main1()

    def Main1(self):
        while(True):
            self.sentence = Listen()

            if(self.sentence == "Say that again please..."):
                speak(self.sentence)
            else:
                break
        self.sentence = self.sentence.replace("jarvis", "")
        self.sentence = tokenize(self.sentence)
        X = bag_of_words(self.sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        print("Probability : ", prob.item())

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    self.reply = random.choice(intent["responses"])
                    if self.reply[0] == '*':
                        speak(self.reply[1:])
                        exit()
                    elif self.reply[0] == '_':
                        NonInputExecution(self.reply)
                    elif self.reply[0] == '^':
                        speak(self.reply[1:])
                        time.sleep(5)
                    else:
                        speak(self.reply)
        else:
            # self.reply = random.choice(intents['error'])
            # speak(self.reply)
            speak("Say that again please...")
        return True


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisVirtualAssistent()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "main-Comp-1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec())
