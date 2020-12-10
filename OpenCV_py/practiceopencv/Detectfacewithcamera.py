from cv2 import cv2 as cv


cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
cap.set(cv.CAP_PROP_BRIGHTNESS,150)

while(True):
    result,img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(imgGray, 1.1, 4)
    
    for (x, y, w, h) in faces:

        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.imshow("Result", img)
    cv.waitKey(1)

cap.release()
cv.destroyAllWindows()

