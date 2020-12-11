from cv2 import cv2 as cv
import numpy as np

def frame_diff(prev_frame, cur_frame, nextframe):
    diff_frames_1 = cv.absdiff(next_frame, cur_frame)
    diff_frames_2 = cv.absdiff(next_frame, prev_frame)
    return_diff = cv.absdiff(diff_frames_1, diff_frames_2)
    threshold = len(return_diff[np.where(return_diff > 2)])
    if threshold > 500:
        print('threshold > 200: ',threshold)
    return return_diff

def get_frame(cap, scaling):
    _,frame = cap.read()
    frame = cv.resize(frame, None,fx=scaling,fy=scaling,interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    return gray

cap = cv.VideoCapture(0)
scaling = 0.5
prev_frame = get_frame(cap, scaling)
cur_frame = get_frame(cap, scaling)
next_frame = get_frame(cap, scaling)

while True:
    cv.imshow('Object Movement', frame_diff(prev_frame,cur_frame,next_frame))
    prev_frame = cur_frame
    cur_frame = next_frame
    next_frame = get_frame(cap,scaling)
    key = cv.waitKey(10)
    if key == 27:
        break
    
cv.destroyAllWindows()

