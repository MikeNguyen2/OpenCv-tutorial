import cv2 as cv

img = cv.imread('MTP/lab.png')
cv.imshow('img',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Treshold
treshold, thresh = cv.threshold(gray, 175, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

# inverse Threshold
treshold, thresh_inv = cv.threshold(gray, 175, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv',thresh_inv)

# Adaptive Threshold: 11 Kernel size
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_thresh', adaptive_thresh)

cv.waitKey(0)