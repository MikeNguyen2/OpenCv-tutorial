import cv2 as cv

img = cv.imread('kartoffelpuffer.jpg')
cv.imshow('img',img)

# Mitteln
average = cv.blur(img,(7,7))
cv.imshow('average',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gauss',gauss)

# Median Blur (7 --> (7,7))
median = cv.medianBlur(img,7)
cv.imshow('median',median)

# Bilateral (kein Kernel, sondern Durchmesser), sigma = Anzahl der Farbbetrachtung
bilateral = cv.bilateralFilter(img, 15, 30, 30)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)