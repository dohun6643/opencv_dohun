import cv2 as cv
import numpy as np

imgL = cv.imread("datas/images/lena.png")
imgResize = cv.resize(imgL, (240, 240))
# cv.imshow("image Resize", imgResize)

# frameWidth = 640
# frameHeight = 480
cap = cv.VideoCapture(0)
cap1 = cv.VideoCapture("datas/videos/Armbot.mp4")
cap2 = cv.VideoCapture(2)
frameWidth = 0
frameHeight = 0

while True:
    result, img = cap1.read()
    cap1Resize = cv.resize(img, (240, 240))

    result, img = cap2.read()
    cap2Resize = cv.resize(img, (480, 240))

    success, img = cap.read()
    capResize = cv.resize(img, (240, 240))

    imgHor = np.hstack((cap1Resize,capResize,imgResize))
    # cv.imshow("Horizontal", imgHor)
    imgHor2 = np.hstack((imgResize,cap2Resize))
    # cv.imshow("Horizontal", imgHor2)
    
    imgMulti = np.vstack((imgHor, imgHor2))
    cv.imshow("Horizontal", imgMulti)

    cv.waitKey(1)