import cv2 as cv
import numpy as np

img = cv.imread('MTP/lab.png')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b, g, r = cv.split(img)

cv.imshow('Blau',b)
cv.imshow('Gruen',g)
cv.imshow('rot',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blaus',blue)
cv.imshow('Gruens',green)
cv.imshow('rots',red)

cv.waitKey(0)