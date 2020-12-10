from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/lena.png")
# cv.imshow("lena",img)
cv.waitKey(0)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(imgGray.shape)
grayToBGR = cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)
print(grayToBGR.shape)

imgHor = np.hstack((grayToBGR,img,grayToBGR))
# cv.imshow("Horizontal", imgHor)

imgHor2 = np.hstack((img,grayToBGR,img))
# cv.imshow("Horizontal", imgHor2)

imgVer = np.vstack((imgHor, imgHor2))
# cv.imshow("Vertical",imgVer)

imgResize = cv.resize(imgVer, (1000, 800))
cv.imshow("image Resize", imgResize)
print(imgResize.shape)


cv.waitKey(0)
