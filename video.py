#liberary import 
#object of videocapture class
#use it inside a while loop

import os
import cv2
import sys

path =r"C:\Users\kusha\OneDrive\Documents\video_sample.mp4"
if not os.path.exists(path):
    print(f'file not found: {path}')
    sys.exit(1)
    
cam=cv2.VideoCapture(path)  #save video to cam through path given
while True:
    state,frame=cam.read()  #read video through .read() in from of state and frame
    if not state:   # if not state then break and not run
        break
    #resize
    frame1=cv2.resize(frame,(500,500))
    frame2=cv2.resize(frame,(0,0),fx=0.25,fy=0.5)    #resize by scale, fx=0.5 means reduce x axis to half
    cv2.imshow('video resized',frame1)
    cv2.imshow('video resied by scale',frame2)
    if cv2.waitKey(10) == ord('q'): #video will reun for 10s if without interrupt
        break