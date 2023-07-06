import cv2 as cv
import numpy as np

img = cv.resize(cv.imread('MTP/Test5.png'),(500,500), interpolation= cv.INTER_AREA)
cv.imshow('img',img)

#translation
def translate(img, x, y):
    transMat = np.float32(([1,0,x],[0,1,y]))
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, 100)
cv.imshow('translated',translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated',rotated)

#Fehler, eher rotate 90
rotated_rotated = rotate(rotated, 315)
cv.imshow('rotated_rotated',rotated_rotated)

#flip 0 oder 1
flip = cv.flip(img,-1)
cv.imshow('flip', flip)


cv.waitKey(0)