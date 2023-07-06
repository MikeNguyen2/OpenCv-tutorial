import cv2 as cv


#Resizing und Rescaling (live und video)
def rescaleFrame(frame, scale):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# alternativ (nur live)
def setRes(width, height):
    vid.set(3,width)
    vid.set(4,height)

#Bild
img = cv.imread('kartoffel.jpg')

cv.imshow('resized Bild',rescaleFrame(img,0.75))
cv.waitKey(0)

#Video
vid = cv.VideoCapture('emanuelV.mkv')

while True:
    isTrue, frame = vid.read()
    frame2 = rescaleFrame(frame,0.75)
    cv.imshow('resized Video', frame2)

    #0xFF==ord('a') fuer den bestimmten Knopf a
    if cv.waitKey(20) & cv.waitKey(0):
        break

vid.release()
cv.waitKey(0)
cv.destroyAllWindows()