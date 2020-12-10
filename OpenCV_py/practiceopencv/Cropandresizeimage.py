from cv2 import cv2 as cv

img = cv.imread("datas/images/lambo.png")
cv.imshow("image", img)
print(img.shape)
# (462, 623, 3)

imgResize = cv.resize(img, (1000, 500))
cv.imshow("image Resize", imgResize)
print(imgResize.shape)



print(type(img))
imgCropped = img[90:400, 360:500]
cv.imshow("image Cropped", imgCropped)

cv.waitKey(0)