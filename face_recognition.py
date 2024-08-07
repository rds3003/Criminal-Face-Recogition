import cv2
import os
import time
import numpy as np
import time
import pandas as pd

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)
df=pd.read_csv('names.csv')

while True:
        ret, im =cam.read()

        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.2,5)


        for(x,y,w,h) in faces:

            cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

            Id,i = recognizer.predict(gray[y:y+h,x:x+w])

            print(Id, i)

            if i < 50:
                name=df.loc[(df['id']==Id)]['name'].values[0]
                cv2.putText(im, name, (x,y-40), font, 2, (255,255,255), 3)
            else:
                cv2.putText(im, "unknown", (x,y-40), font, 2, (255,255,255), 3)

        cv2.imshow('im',im)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
           
cam.release()
cv2.destroyAllWindows()
