# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:44:22 2018

@author: arden
"""

import cv2
import numpy as np

def get_video():
    cap = cv2.VideoCapture(0)
    return cap

def get_cascade(filename):
    cascade = cv2.CascadeClassifier(filename)
    return cascade

def main(cascade_file):
    cap = get_video()
    cascade = get_cascade(cascade_file)
    
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = cascade.detectMultiScale(gray)
        
        for (x,y,w,h) in eyes:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main('../haarcascade/cascades/haarcascade_eye.xml')