from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/load_image.jpg")


cv.rectangle(img,(60,120),(140,60),(0,0,255),1)
cv.putText(img,"Hand",(150,80),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
cv.imshow("image",img)

cv.circle(img,(230,100),50,(0,0,255),1)
cv.putText(img,"Head",(220,40),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
cv.imshow("image",img)

cv.rectangle(img,(330,340),(400,280),(0,0,255),1)
cv.putText(img,"Ball",(400,320),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
cv.imshow("image",img)

cv.rectangle(img,(420,300),(470,240),(0,0,255),1)
cv.putText(img,"Feet",(480,260),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,250),1)
cv.imshow("image",img)

cv.circle(img,(70,290),5,(200,0,0),60)
cv.line(img,(70,290),(420,260),(0,140,0),3)
cv.line(img,(70,290),(100,120),(0,140,0),3)
cv.line(img,(70,290),(200,140),(0,140,0),3)
cv.line(img,(70,290),(330,320),(0,140,0),3)
cv.imshow("image",img)


# x, y, w, h = 310, 320, 150, 160
# cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2 )
# cv.putText(img, "Bounding Box", (x-10, y-10,),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
# cv.imshow("image",img)


cv.waitKey(0)
# cv.destroyAllWindows()