import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('MTP/lab.png')
cv.imshow('img',img)

# Grau
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow('lab',lab)

# RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

#plt.imshow(rgb)
#plt.show()

# Konvertierung von hsv zu gray über bgr

cv.waitKey(0)