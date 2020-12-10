from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/lena.png")
# cv.imshow("lena",img)
cv.waitKey(0)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(imgGray.shape)
grayToBGR = cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)
print(grayToBGR.shape)

imgHor = np.hstack((grayToBGR,img))
cv.imshow("Horizontal", imgHor)

imgVer = np.vstack((grayToBGR,img))
cv.imshow("Vertical",imgVer)

imgStack = stackImages(0.5,([img,imgGray,img],[imgGray,img,imgGray]))
cv.imshow("Stack",imgStack)


cv.waitKey(0)
