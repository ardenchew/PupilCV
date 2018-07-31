# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:36:15 2018

@author: arden
"""

import cv2
import numpy as np
import os
from glob import glob

def pre_processing(pos_dir, loc):
    
    imgs = glob(os.path.join(pos_dir,'*'))
    if not os.path.exists(loc): os.mkdir(loc)
    
    for i in imgs:
        
        img = cv2.imread(i, 0)
        img = cv2.resize(img, (50,50))
        filename = os.path.join(loc, os.path.basename(i))
        cv2.imwrite(filename, img)

def write_info_file(oper_loc, info_loc, size, obj_count=1):
    
    cwd = os.getcwd()
    os.chdir(oper_loc)
    
    prefix = info_loc.replace(oper_loc, '')
    imgs = glob(os.path.join(prefix,'*'))
    
    for i in imgs:
        line = '{} {} {} {} {} {}\n'.format(i,obj_count,size[0],size[1],size[2],size[3])
        with open('info.dat', 'a') as f:
            f.write(line)
    
    os.chdir(cwd)
    
    
if __name__ == "__main__":
    pos_dir = 'C:\\Users\\arden\\Dropbox (Personal)\\github\\pupilcv\\images\\iris'
    loc = 'C:\\Users\\arden\\Dropbox (Personal)\\github\\pupilcv\\images\\iris_pos'
    pre_processing(pos_dir, loc)
    oper_loc = oper_loc = 'C:\\Users\\arden\\Dropbox (Personal)\\github\\pupilcv\\haarcascade\\dev'
    size = (0, 0, 50, 50)
    write_info_file(oper_loc, loc, size)
    