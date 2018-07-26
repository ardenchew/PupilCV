# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:24:37 2018

@author: arden
"""

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images(link, loc):
    
    neg_images_url = urllib.request.urlopen(link).read().decode()
    
    for i, url in enumerate(neg_images_url.split('\n')):
        
        try:
            print(url)
            
            img_name = os.path.join(loc,(i+'.jpg')
            urllib.request.urlretrieve(url, img_name)
            img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, 100)
            cv2.imwrite(img_name)
            
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    store_raw_images('','')
