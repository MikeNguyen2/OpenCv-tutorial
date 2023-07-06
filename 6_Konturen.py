import cv2 as cv
import numpy as np

img = cv.imread('MTP/lab.png')
cv.imshow('img',img)

blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny = cv.Canny(blur, 125,175)
cv.imshow('canny',canny)

# Treshold
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# Konturen      
# TREE: Hierarchien; EXTERNAL= Am Rand?, LIST: alle
# NONE: keine; SIMPLE: Linienvorhersage
#
# contours: Koordinaten; hierarchies: Formen
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours), ' Konturen gefunden')

# -1: Anzahl der Konturen
contours_drawn = cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('contours_drawn', contours_drawn)

cv.waitKey(0)