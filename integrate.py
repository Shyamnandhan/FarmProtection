import cv2
import keras
from keras.models import load_model
import numpy as np
import pygame 
import pygame
import pygame
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
import pyrebase
import random
import json
import numpy as np
0

config = {
  "apiKey": "AIzaSyAWi-rda7WT5pLUDMl6Tc_GnJskmTGokiM",
  "authDomain": "home-automation-49627.firebaseapp.com",
  "databaseURL": "https://home-automation-49627-default-rtdb.firebaseio.com",
  "storageBucket": "home-automation-49627.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Load the mp3 file

model = load_model("/home/admin/project/bestmodel.h5")


img2 = cv2.VideoCapture(0)
class_type = {0:'Bear',
 1:'Cheetah',
 2:'DOG',
 3:'Deer',
 4:'Elephant',
 5:'Fox',
 6:'Goat',
 7:'Lion',
 8:'Pig',
 9:'Tiger',
 10:'monkey'}
 
while True:
    
    GPIO.output(16,True)
    ret,frame = img2.read()
    frame = cv2.resize(frame, (224, 224))  # Resize to match input size of the model
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color space from BGR to RGB
    frame = frame / 255.0  # Normalize pixel values
    frame1 = np.expand_dims(frame, axis=0)


    # model = load_model("bestmodel_50.h5")
    # img = get_img_array(frame)
    c=np.argmax(model.predict(frame1))
    res2 = class_type[c]
    print(res2)
    
    cv2.imshow('predictions', frame)
    cv2.putText(frame, f'Prediction: {res2}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    pygame.mixer.init()
    if res2 == "Bird":
        GPIO.output(12,False)
        a=0
        data = {'animal':a}
        db.child("Status").push(data)
        db.update(data)
        pygame.mixer.music.load("/home/admin/project/SJRDHEP-firecrackers-burst.wav")
        pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
        #    continue

    elif res2 == "Elephant":
        GPIO.output(12,False)
        a=1
        data = {'animal':a}
        db.child("Status").push(data)
        db.update(data)
        pygame.mixer.music.load("/home/admin/project/SJRDHEP-firecrackers-burst.wav")
        pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
        #    continue

    elif res2 == "Sheep":
        GPIO.output(12,False)
        a=2
        data = {'animal':a}
        db.child("Status").push(data)
        db.update(data)
        pygame.mixer.music.load("/home/admin/project/SJRDHEP-firecrackers-burst.wav")
        pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
        #    continue 

    elif res2 == "Bear":
        GPIO.output(12,False)
        a=3
        data = {'animal':a}
        db.child("Status").push(data)
        db.update(data)
        pygame.mixer.music.load("/home/admin/project/FX57W9B-dogs-barking.wav")
        pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
        #    continue 
    
    else:
        GPIO.output(12,False)    
        a=4
        data = {'animal':a}
        db.child("Status").push(data)
        db.update(data)
        print("hii")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()
