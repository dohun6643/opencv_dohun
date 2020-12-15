from cv2 import cv2 as cv
import numpy as np
import os
import pytesseract
import matplotlib.pyplot as plt

img = cv.imread("datas/images/cards.jpg")
cv.imshow("image",img)
width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img,matrix,(width,height))
imgGray = cv.cvtColor(imgOutput,cv.COLOR_BGR2GRAY)
cv.imshow("Output",imgGray)

cv.waitKey(0)
