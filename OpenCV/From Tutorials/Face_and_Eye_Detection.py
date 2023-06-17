# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:40:45 2020

@author: LINJO
"""
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def detect(grey, frame):
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    #print(faces) # faces are a tuple having (x,y) of top left pos and w:width and h: height
    for [x,y,w,h] in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)
        roi_grey = grey[y:y+h,x:x+w]# zone of interest
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey,1.3,22)
        for [ex,ey,ew,eh] in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ex+eh), (0,255,0),2)
    
    return frame

video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(grey,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
video_capture.release()
cv2.destroyAllWindows()
            