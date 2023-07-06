#haarcascade und local binary patterns

import cv2 as cv

#img = cv.imread('kylie-jenner.jpg')
img = cv.imread('Mob.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('15_1_Haarcascade.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,255), thickness =2)

cv.imshow('detected',img)

cv.waitKey(0)