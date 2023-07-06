import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('MTP/lab.png')
cv.imshow('img',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)

gray_masked = cv.bitwise_and(gray,gray, mask=mask)
cv.imshow('gray masked',gray_masked)

col_masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('col masked',col_masked)

plt.figure()
plt.xlabel('Bins')
plt.ylabel('Pixel')
plt.xlim([0,256])

# Gray Histogramm
gray_hist = cv.calcHist([gray],[0],mask,[256], [0,256])

plt.title('Grayscale Histogram')
plt.plot(gray_hist)
plt.show()

# Color Histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.title('Color Histogram')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()