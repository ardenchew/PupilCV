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

def main():
    cap = get_video()

if __name__ == "__main__":
    main()
