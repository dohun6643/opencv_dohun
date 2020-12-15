from cv2 import cv2 as cv
import numpy as np
import os
import pytesseract
import matplotlib.pyplot as plt
import pytesseract
# namecard   #세우고 그레이로 색변환
# img = cv.imread("datas/images/namecard_01.jpg")
# imgResize = cv.resize(img, (1000, 500))
# cv.imshow("image Resize", imgResize)
# width,height = 250,350
# pts1 = np.float32([[334,144],[777,170],[80,365],[800,415]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv.warpPerspective(imgResize,matrix,(width,height))
# cv.imshow("Output",imgOutput)
# cv.waitKey(0)

#번호판

# img = cv.imread("datas/images/licenseplate_03.jpg")
# imgResize = cv.resize(img, (1000, 500))
# cv.imshow("image Resize", imgResize)
# width,height = 800,450
# pts1 = np.float32([[302,344],[522,353],[304,381],[521,387]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv.warpPerspective(imgResize,matrix,(width,height))
# imgGray = cv.cvtColor(imgOutput,cv.COLOR_BGR2GRAY)
# def threshholding(images):
#     return cv.threshhold(images, 50, 255, cv.THERSH_BINARY+cv.THRESH_OPSU)[1]
#     img = threshholding(imgGray)
#     cv.imshow(['threshold', img])
 
# cv.imshow("Output",imgGray)

# cv.waitKey(0)

# img = cv.imread("datas/images/poem.jpg")
# imgResize = cv.resize(img, (1000, 800))
# cv.imshow("image Resize", imgResize)
# width,height = 800,450
# pts1 = np.float32([[30,195],[690,117],[142,788],[996,749]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv.warpPerspective(imgResize,matrix,(width,height))
# imgGray = cv.cvtColor(imgOutput,cv.COLOR_BGR2GRAY)
# # cv.imshow("Output",imgGray)

# cv.waitKey(0)

try:
   img = cv.imread('datas/images/poem.jpg', cv.IMREAD_GRAYSCALE)
   imgResize = cv.resize(img, (1000, 800))
    cv.imshow("image Resize", imgResize)
    width,height = 800,450
    pts1 = np.float32([[30,195],[690,117],[142,788],[996,749]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(imgResize,matrix,(width,height))
   ret,thresh1 = cv.threshold(img,100,255,cv.THRESH_BINARY)
 
   titles = ['Original Image','BINARY']
   images = [img, thresh1]
 
   def threshholding(images):
       return cv.threshhold(images, 50, 255, cv.THERSH_BINARY+cv.THRESH_OPSU)[1]
 
 
       img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
       img = threshholding(img_gray)
       cv.imshow(['threshold', img])
 
   import pytesseract
   from pytesseract import Output
 
   custom_config = r'--oem 3 --psm 6 -l kor+kor_vert+eng'
   words_string = pytesseract.image_to_string(img)
   words = pytesseract.image_to_data(img, config = custom_config, output_type=Output.DICT)
 
   print(words.keys())
   n_boxes = len(words['text'])
   for i in range(n_boxes):
       if int(words['conf'][i]) > 30:
           (x,y,w,h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
           img = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
           cv.imshow('Resource', img)
          
   cv.waitKey(0)
 
except:
   pass

