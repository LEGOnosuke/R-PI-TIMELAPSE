# -*- coding: utf-8 -*-

import numpy as  np
import sys
import cv2
import time
#-1 or 2
cap  = cv2.VideoCapture(-1)
before = None
fps = 0
start = time.time()
how_thresh = 10

while True:
    #start = time.time()
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    cv2.imshow("camera", frame)
    """    
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if before is None:
        before = gray.copy().astype("float")
        continue

    k = cv2.waitKey(1)
    if k == ord("r"):
        new = input("rere?")
        how_thresh = new
     
    cv2.accumulateWeighted(gray, before, 0.7)
    mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))
    cv2.imshow("MotionDetected Frame" , mdframe)
    
    ret,thresh2 = cv2.threshold(mdframe,how_thresh,255,cv2.THRESH_BINARY)
    #cv2.imshow("threshed2", thresh2)
    
    ret,thresh1 = cv2.threshold(gray,147,255,cv2.THRESH_BINARY)
    cv2.imshow("threshed1", thresh1)
    
    #contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(hierarchy)
    #frame = cv2.drawContours(thresh2, contours, -1, (0,255,0), 3)
    #print(frame)
    #cv2.imshow("test" , frame)

    #cd = frame
    #cd = cv2.rectangle(cd,(384,0),(510,128),(0,255,0),3)
    #cv2.namedWindow('cd', cv2.WINDOW_NORMAL)
    #print(type(cd))
    
    #cv2.imshow("cd" , cd)
    

    
    
   #if len(contours) > 0:
        #cv2.imshow("Found contours"  , contours)
    """
    
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord("h"):
        hold = frame
        cv2.imshow("cap" , hold)
    
    elif k == ord("s"):
        save = frame
        cv2.imwrite("kk.jpg", save)
        cv2.imshow("saved!", save)

    fps += 1
    stop = time.time()
    #fps = (stop - start)
    #fps = 1 / fps
    #print(stop - start)
    sec = (stop - start)
    if sec > 1:
        print("FPS: " + str(fps))
        fps = 0
        start = time.time()
    #print("FPS: " + str(fps))
    
    

cv2.destroyAllWindows()
cap.release

