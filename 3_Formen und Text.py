import cv2 as cv
import numpy as np

img = cv.imread('kartoffel.jpg')
blank = np.zeros((500,500,3), dtype= 'uint8')

#anmalen
blank[:] = 0,0,1
blank[150:300,150:300] = 255,0,0

#Rechteck thickness = cv.FILLED oder -1 
cv.rectangle(blank,(0,0),(250,blank.shape[0]),(0,0,255), thickness=2)

#Kreis
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=3)

#Linie
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness=3)

#Text
cv.putText(blank,'Schinken',(225,225), cv.FONT_HERSHEY_TRIPLEX,1,(100,100,100),2)

#cv.imshow('katze',img)
cv.imshow('blank',blank)

cv.waitKey(0)
