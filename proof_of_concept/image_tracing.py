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

def main():
    img = get_image()

if __name__ == "__main__":
    main()
