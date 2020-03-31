#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import datetime
from time import sleep
import sys
import os
dirname = "Img"
dirname2 = "Img2"

cap = None
cap2 = None
count=0
camera_port = 2   # USBカメラのデバイスは0 (/dev/video0)
cap = cv2.VideoCapture(camera_port)
cap2 = cv2.VideoCapture(-1)

"""
frame = 60*30
rec_s = 5*60*60
wait = int(rec_s) / frame
print("合計"+str(frame)+"枚の画像データです。")
print("推定で最大"+str(frame * 0.07)+"MG、"+str(frame * 0.07 / 1000)+"GBの画像データになります。")
print(""+str(rec_s)+"秒撮影します。")
print("一枚撮るごとに"+str(wait)+"秒待ちます。")

"""
sec = input("作成する動画の秒数は？")
frame = int(sec*30)
print("合計"+str(frame)+"枚の画像データです。")
print("推定で最大"+str(frame * 0.07)+"MG、"+str(frame * 0.07 / 1000)+"GBの画像データになります。")
rec_h = input("何分撮影するの？")
rec_s =  int(rec_h) *60
print(""+str(rec_s)+"秒撮影します。")
wait = int(rec_s) / frame
print("一枚撮るごとに"+str(wait)+"秒待ちます。")


ans = ""
ans = str(input("録画を開始するには、1を入力してください。"))
ans2 = str(ans)

for i in range(frame):
  ret, im = cap.read()
  ret2, im2 = cap2.read()
  print(str(i+1)+"回目の撮影です。")
  last = frame - (i+1)
  print("あと" + str(last) + "回、"+str(last*wait/60)+"分です。")
  tm=datetime.datetime.today().strftime("%Y/%m/%d %X")
  ftm=datetime.datetime.today().strftime("%Y%m%d%H%M%S")
  cv2.putText(im,tm,(20,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))
  cv2.putText(im2,tm,(20,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))
  file_name = os.path.join(dirname,"[Window]"+str(ftm)+".jpg")
  file_name2 = os.path.join(dirname2,"[Desk]"+str(ftm)+".jpg")

  print ("ファイル名:"+str(file_name))
  print ("ファイル名:"+str(file_name2))
  cv2.imwrite(file_name, im)
  cv2.imwrite(file_name2, im2)
  print("保存完了")
  sleep(wait)


#This is BACKUP
"""

while(True):

  for i in range(10):
  ret, im = cap.read()
    if ret==True:
        if i==9:
            
            tm=datetime.datetime.today().strftime("%Y/%m/%d %X")
            ftm=datetime.datetime.today().strftime("%Y%m%d%H%M%S")
            cv2.putText(im,tm,(20,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))
            file_name = "" + ftm + ".jpg"
            
            print (file_name)
            cv2.imwrite(file_name, im)
            print("File written")
            sleep(1)
"""

print("録画が完了しました。")
cap.release()
cv2.destroyAllWindows()
