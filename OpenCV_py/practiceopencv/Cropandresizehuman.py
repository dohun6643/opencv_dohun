from cv2 import cv2 as cv

img = cv.imread("/home/dohun/Documents/Develop/learn_opencv/imageforopencv/human.png")
cv.imshow("image", img)
print(img.shape)
# (361, 600, 3)

# imgResize = cv.resize(img, (1000, 500))
# cv.imshow("image Resize", imgResize)
# print(imgResize.shape)

print(type(img))
imgCropped = img[0:360, 0:190]
cv.imshow("image Cropped", imgCropped)

cv.waitKey(0)