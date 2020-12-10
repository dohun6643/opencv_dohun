from cv2 import cv2 as cv

cap = cv.VideoCapture(0)

(width,height) = (640,480)
fps = 20.0
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)      #버전낮을경우 써줘야함
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)    #4.4 버전에서는 없어도됨
cap.set(cv.CAP_PROP_FPS, fps)                        

fourcc = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('imageforopencv/output.avi',fourcc, 20.0, (640,480))
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out_mp4 = cv.VideoWriter('imageforopencv/output.avi',fourcc, 20.0, (640,480))

while(True):
    ret,frame = cap.read()
    out_avi.write(frame)
    out_mp4.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out_avi.release()
out_mp4.release()