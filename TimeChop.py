# -*- coding: utf-8 -*-

import cv2
import sys
import os
import time
from stat import ST_CTIME
from sys import exit

def getImage(filename):
    if (not os.path.isfile(filename)):
        print("No such file<{}>".format(filename))
        exit(1)
    
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    if (img is None):
        print("Unable to open the image<{}>".format(filename))
        exit(1)
    return img
    
def getCreateTime(filename):
    status = os.stat(filename)
    return time.asctime(time.localtime(status[ST_CTIME]))

def RenderText(img, text):
    width, height = img.shape[:2]
    
    '''img = cv2.putText(img, text, (size), cv2.FONT_HERSHEY_COMPLEX,0.5,(128, 0, 0),1)'''
    '''Color (B,G,R,A)'''
    img = cv2.putText(img, text, (0, (height)), cv2.FONT_HERSHEY_COMPLEX,0.5,(0, 165, 255, 255), 1)
    return img
    
def runner(input):
    filename = input[1]
    outputPath = input[2]
    
    print("IN<{}>".format(filename))
    print("OUT<{}>".format(outputPath))
    
    img = getImage(filename)
    createTime = getCreateTime(filename)
    img = RenderText(img, createTime);
    
    cv2.imwrite(outputPath, img)
    exit(0)
    
def main():
    # print command line arguments
    if len(sys.argv) != 3:
        print("Usage: TimeChop.py InputImagePath OutputImagePath")
        exit(1)
    runner(sys.argv);
    
    '''for arg in sys.argv:
        print(arg, sys.argv.index(arg))'''
    exit(0)

if __name__ == "__main__":
    main()
