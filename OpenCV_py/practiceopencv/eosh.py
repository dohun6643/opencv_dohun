from cv2 import cv2 as cv
import numpy as np

# 원본 이미지
img = cv.imread("datas/images/load_image.jpg")


def ShowRectangle(x1, y1, x2, y2):
    cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),1)
    cv.putText(img,"Hand",(150,80),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
    cv.imshow("image",img)


ShowRectangle(60, 120, 140, 60 )
ShowRectangle(330,340, 400,280)
ShowRectangle(420,300, 470,240)

def ShowCircle(x,y,r):
    cv.circle(img, (x,y),r,(0,0,255),1)
    cv.imshow("image",img)
# cv.circle(img,(230,100),50,(0,0,255),1)
# cv.putText(img,"Head",(220,40),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
# cv.imshow("image",img)

# cv.circle(img,(70,290),5,(200,0,0),60)
ShowCircle(70,290,50)
ShowCircle(230,100,50)
# cv.line(img,(70,290),(420,260),(0,140,0),3)
# cv.line(img,(70,290),(100,120),(0,140,0),3)
# cv.line(img,(70,290),(200,140),(0,140,0),3)
# cv.line(img,(70,290),(330,320),(0,140,0),3)
# cv.imshow("image",img)


# x, y, w, h = 310, 320, 150, 160
# cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2 )
# cv.putText(img, "Bounding Box", (x-10, y-10,),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
# cv.imshow("image",img)


cv.waitKey(0)
# cv.destroyAllWindows()