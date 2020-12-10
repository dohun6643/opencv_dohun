from cv2 import cv2 as cv
import os

cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")

directoryname = os.getcwd() + '/imageforopencv'
img = cv.imread('datas/images/faces.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(imgGray, 1.1, 4)

cnt = 0
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    imgResize = cv.resize(img, (1300, 800))
    cv.imshow("image Resize", imgResize)
    imgCropped = img[y:y+h, x:x+w,]
    cv.imshow("image Cropped", imgCropped)
    cnt = cnt + 1
    cv.imwrite(directoryname + "/face_" +str(cnt)+ ".png",imgCropped )

cv.waitKey(0)
cv.destroyAllWindows()



