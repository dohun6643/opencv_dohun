from cv2 import cv2 as cv
import numpy as np
# import os
# import pytesseract
# import matplotlib.pyplot as plt
# import pytesseract

img = cv.imread("datas/images/lena.png")
imgCanny = cv.Canny(img,150,200)
cv.imshow("Canny Image",imgCanny)

kernel = np.ones((5,5),np.uint8)
imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
cv.imshow("Dialation Image",imgDialation)
imgEroded = cv.erode(imgDialation,kernel,iterations=1)
cv.imshow("Eroded Image",imgEroded)

cv.waitKey(0)
cv.destroyAllWindows()

# from cv2 import cv2 as cv
# img = cv.imread("datas/images/lena.png")
# imgCanny = cv.Canny(img,150,200)
# cv.imshow("Canny Image",imgCanny)

# import numpy as np
# kernel = np.ones((5,5),np.uint8)
# imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
# cv.imshow("Dialation Image",imgDialation)
# imgEroded = cv.erode(imgDialation,kernel,iterations=1)
# cv.imshow("Eroded Image",imgEroded)
# cv.waitKey(0)
# cv.destroyAllWindows()