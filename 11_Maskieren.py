import cv2 as cv
import numpy as np

img = cv.imread('kartoffelpuffer.jpg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked',masked)

print(img.shape[0])
print(img.shape[1])

cv.waitKey(0)