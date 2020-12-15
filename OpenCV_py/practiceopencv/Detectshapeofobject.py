from cv2 import cv2 as cv

img_color = cv.imread('datas/images/shapes.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, _ = cv.findContours(img_binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv.contourArea(cnt)
    cv.drawContours(img_color,[cnt],0,(255,0,0),2)
cv.imshow("result",img_color)
cv.waitKey(0)