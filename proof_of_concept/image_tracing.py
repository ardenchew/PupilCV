# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:49:45 2018

@author: arden
"""

import cv2
import numpy as np

def get_image(filename):
    img= cv2.imread(filename)
    return img

def get_cascade(filename):
    cascade = cv2.CascadeClassifier(filename)
    return cascade

def main(image_file, cascade_file):
    img = get_image(image_file)
    cascade = get_cascade(cascade_file)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray)
    
    for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('img',img)
    
    cv2.waitKey(0)

if __name__ == "__main__":
    main('../images/eyes/sample_1.jpg', '../haarcascade/cascades/haarcascade_eye.xml')
