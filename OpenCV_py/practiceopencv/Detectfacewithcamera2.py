from cv2 import cv2 as cv


cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")
cascade1 = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_eye.xml")
cascade2 = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_mcs_nose.xml")

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
    eyes = cascade1.detectMultiScale(imgGray, 1.1, 4)
    # nose = cascade2.detectMultiScale(imgGray, 1.1 ,4)
    for ((x1, y1, w1, h1), (x2, y2, w2, h2)) in zip(faces, eyes):
        cv.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 2)
        cv.rectangle(img, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 2)
            # for (x, y, w, h) in nose:
            #     cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow("Result", img)
    cv.waitKey(1)


cap.release()
cv.destroyAllWindows()
