import cv2 as cv

img=cv.imread('MTP/lab.png')
#cv.imshow('cat', img)

#resize
#resize = cv.resize(img,(500,500), interpolation= cv.INTER_AREA)
#cv.imshow('resize',resize)

#Vergrauen
#gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#Blurr
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#Kanten
canny = cv.Canny(blur,100,200)
cv.imshow('canny',canny)

#Erweitern
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)

#erodieren
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Crop
crop = img[0:500,0:500].copy()
cv.imshow('crop',crop)

cv.waitKey(0)
cv.destroyAllWindows()