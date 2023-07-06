import cv2 as cv

vid = cv.VideoCapture('weird.mp4')

haar_cascade = cv.CascadeClassifier('15_1_Haarcascade.xml')

print(vid.read()[1][0])


while True:
    isTrue, frame = vid.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,255), thickness =2)

    cv.imshow('Video Anzeigen', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()
