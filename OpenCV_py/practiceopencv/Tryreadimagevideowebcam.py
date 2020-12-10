######################## READ IMAGE ############################
from cv2 import cv2 as cv
import numpy as np


img = cv.imread("datas/images/lena.png")
cv.imshow("Lena Soderberg", img)

while True:
    data = cv.waitKey(0)
    if data == ord('a'):
        print("Hello")
    elif data == ord('b'):
        print("World!!!")
    

# cv.waitKey(0) == ord('q'):
# cv.waitKey(10) == ord('i'): 


# ######################### READ VIDEO #############################
# from cv2 import cv2 as cv
# frameWidth = 640
# frameHeight = 480
# cap = cv.VideoCapture("datas/videos/Armbot.mp4")
# while True:
#     success, img = cap.read()
#     img = cv.resize(img, (frameWidth, frameHeight))
#     # frameWidth = frameWidth + 20
#     # frameHeight = frameHeight + 20
#     cv.imshow("Result", img)
#     if cv.waitKey(0) == ord('q'):
#         break
# cap.release()

# # ######################### READ WEBCAM  ############################
# from cv2 import cv2 as cv
# frameWidth = 2250; frameHeight = 960;
# cap = cv.VideoCapture(2)
# cap.set(cv.CAP_PROP_FRAME_WIDTH , frameWidth);
# cap.set(4, frameHeight) # cv.CAP_PROP_FRAME_HEIGHT
# while cap.isOpened():
#     success, img = cap.read()
#     cv.imshow("Result", img)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

