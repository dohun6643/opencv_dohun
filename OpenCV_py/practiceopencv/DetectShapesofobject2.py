from cv2 import cv2 as cv

img_color_approx = cv.imread('datas/images/shapes.png')
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours,_ = cv.findContours(img_binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    print(x,y,w,h)
    epsilon = 0.02 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    print(len(approx))
    cv.drawContours(img_color_approx,[approx],0,(0,255,255),2)
cv.imshow("result",img_color_approx)
cv.waitKey(0)