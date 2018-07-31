# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:24:37 2018

@author: arden
"""

import urllib.request
import cv2
import numpy as np
import os
from glob import glob

def store_raw_images(link, loc):
    
    neg_images_url = urllib.request.urlopen(link).read().decode()
    neg_images_url = neg_images_url.split('\n')
    neg_images_url = [i for i in neg_images_url if i != '']
    neg_images_url = [i.replace('\r','') for i in neg_images_url]
    
    errors = 0
    start_idx = 47
    
    for i, url in enumerate(neg_images_url):
        
        try:
            print(url)
            
            img_name = os.path.join(loc,(str(i-errors+start_idx)+'.jpg'))
            urllib.request.urlretrieve(url, img_name)
            img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (100,100))
            cv2.imwrite(img_name, img)
            
        except Exception as e:
            errors += 1
            print(str(e))
            
def write_bg_file(oper_loc, bg_loc):
    
    cwd = os.getcwd()
    os.chdir(oper_loc)
    
    prefix = bg_loc.replace(oper_loc, '')
    imgs = glob(os.path.join(prefix,'*'))
    
    for i in imgs:
        with open('bg.txt', 'a') as f:
            f.write(i)
    
    os.chdir(cwd)

if __name__ == "__main__":
    link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893'
    loc = 'C:\\Users\\arden\\Dropbox (Personal)\\github\\pupilcv\\images\\neg'
    store_raw_images(link,loc)
    oper_loc = 'C:\\Users\\arden\\Dropbox (Personal)\\github\\pupilcv\\haarcascade\\dev'
    write_bg_file(oper_loc,loc)
