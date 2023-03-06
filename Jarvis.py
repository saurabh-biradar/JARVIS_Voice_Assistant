from Listen import Listen
from Speak import speak
import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Task import NonInputExecution

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

Name = "Jarvis"


def Main():
    while(True):
        sentence = Listen()
        if(sentence == "Say that again please..."):
            speak(sentence)
        else:
            break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                if reply[0] == '*':
                    speak(reply[1:])
                    exit()
                elif reply[0] == '_':
                    NonInputExecution(reply)
                else:
                    speak(reply)
    else:
        speak("Say that again please...")


speak("Sir, Please give your command")  
while True:
    Main()
