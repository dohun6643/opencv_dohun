import cv2
 
cap = cv2.VideoCapture("datas/videos/roadway_01.mp4") 

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('Camera Window', frame)
        key = cv2.waitKey(10) & 0xFF
        if (key == 27): 
            break

cap.release()
cv2.destroyAllWindows()