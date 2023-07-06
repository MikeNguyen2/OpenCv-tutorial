import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('15_1_Haarcascade.xml')

img = cv.imread('kartoffelpuffer.jpg')
cv.imshow('img',img)

people = ['a','b','c','d','e']
DIR = r'C:\Users\mikep\OneDrive\Dokumente\Projekte\OpenTest'

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect =  haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

features =  np.array(features)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained,yml')

np.save('features.npy',features)
np.labels('labels.npy',labels)

cv.waitKey(0)