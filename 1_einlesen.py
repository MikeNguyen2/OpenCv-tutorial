import cv2 as cv

#Bild einlesen
img = cv.imread('Kartoffel.jpg')

cv.imshow('Bild anzeigen',img)
cv.waitKey(0)

#Video einlesen -- mkv nicht geeignet?
vid = cv.VideoCapture('weird.mp4')

i=0
while True:
    isTrue, frame = vid.read()
    cv.imshow('Video Anzeigen', frame)
    i=i+1
    #0xFF==ord('a') fuer den bestimmten Knopf a     
    #cv.waitKey(0) fuer jeden Knopf
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

print(i)
vid.release()

cv.waitKey(0)
cv.destroyAllWindows()


    