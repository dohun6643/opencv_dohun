from cv2 import cv2 as cv
import numpy as np
import os
import pytesseract
import matplotlib.pyplot as plt
import pytesseract

def nothing():
    pass
cv.namedWindow("Canny Edge")
cv.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
cv.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)
img_gray = cv.imread('datas/images/shapes.png', cv.IMREAD_GRAYSCALE)
while True:
    low = cv.getTrackbarPos('low threshold','Canny Edge')
    high = cv.getTrackbarPos('high threshold','Canny Edge')
    img_canny = cv.Canny(img_gray, low, high)
    cv.imshow("Canny Edge", img_canny)
    if cv.waitKey(1) == ord('q'):
        break
    
