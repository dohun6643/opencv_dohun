from cv2 import cv2 as cv

img_color_approx = cv.imread('datas/images/namecard_01.jpg')
imgResize = cv.resize(img_color_approx,(1000,700))
imgGray = cv.cvtColor(imgResize, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
cv.imshow('Canny with Blur shapes', imgCanny)

ret, img_binary = cv.threshold(imgCanny, 127, 255, 0)
contours,_ = cv.findContours(img_binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(x,y,x+w,y+h)
    epsilon = 0.02 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    print(len(approx))
    cv.drawContours(img_color_approx,[approx],0,(0,255,255),2)
cv.imshow("result",img_color_approx)
cv.waitKey(0)

