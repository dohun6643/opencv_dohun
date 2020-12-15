def getContours(img):
    contours, hierarchy = cv.findContours(
        img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print('hierarchy : ', hierarchy)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            # print(peri)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, objectType,
                       (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7,
                       (0, 0, 0), 2)


path = 'datas/images/shapes.png'
img = cv.imread(path)
cv.imshow('resource shapes', img)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
cv.imshow('Canny with Blur shapes', imgCanny)

imgContour = img.copy()
getContours(imgCanny)
cv.imshow('detected shapes', imgContour)


cv.waitKey(0)
cv.destroyAllWindows()
