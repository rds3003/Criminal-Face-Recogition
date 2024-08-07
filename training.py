
import cv2
import os

import numpy as np

from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    faceSamples=[]
    
    ids = []
    ids_names = []
    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')

        img_numpy = np.array(PIL_img,'uint8')

        name = os.path.split(imagePath)[-1].split(".")[0]
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        faceSamples.append(img_numpy)

        ids.append(id)
        ids_names.append([id, name])
        
    return faceSamples,ids,ids_names

faces,ids,ids_names = getImagesAndLabels('dataset')

recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

import csv
f = open("names.csv", 'w', newline="")
writer = csv.writer(f)
writer.writerow(["id", "name"])
writer.writerows(ids_names)
f.close()

print('done....')