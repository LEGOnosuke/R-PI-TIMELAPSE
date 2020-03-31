#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("インポート中...")
import cv2
import datetime
from time import sleep
import sys
import os
print("インポート完了...")

#SETTINGs
dirname_r = "Img"  #r...RaspberryPi_camera
dirname_w = "Img2"  #w...Web_camera
picture_gb = 0.07 
picamera_port = -1
webcamera_port = 2   # USBカメラのデバイスは0 (/dev/video0)


cap = None
cap2 = None
count=0
sec = input("作成する動画の秒数は何秒ですか？")
frame = int(sec*30)
print("合計"+str(frame)+"枚の画像データです。")
print("一箇所ごとに推定で最大"+str(frame * picture_gb)+"MG、"+str(frame * picture_gb / 1000)+"GBの画像データになります。")
rec_h = input("何分撮影しますか？")
rec_s =  int(rec_h) *60
print(""+str(rec_s)+"秒撮影します。")
wait = int(rec_s) / frame
print("一枚撮るごとに"+str(wait)+"秒待ちます。")

camera_r = False
camera_r_flip = False
camera_w = False
camera_w_flip = False
if (int(input("ラズパイカメラを使用しますか？はい→1 いいえ→0 : ")) == 1):
  camera_r = True
  if (camera_r == True):
    cap_r = cv2.VideoCapture(picamera_port)
    camera_r_text = raw_input("ラズパイカメラで記録する固有の場所名は？(例:Window) : ")
    if (int(input("ラズパイカメラの画像を上下左右反転しますか？はい→1 いいえ→0 : ")) == 1):
      camera_r_flip= True
if (int(input("WEBカメラを使用しますか？はい→1 いいえ→0 : ")) == 1):
  camera_w = True
  if (camera_w == True):
    cap_w = cv2.VideoCapture(webcamera_port)
    camera_w_text = raw_input("WEBカメラで記録する固有の場所名は？(例:Window) : ")
    if (int(input("WEBカメラの画像を上下左右反転しますか？はい→1 いいえ→0 : ")) == 1):
      camera_w_flip= True

print("録画の保存データは、ラズパイカメラ:"+dirname_r+"、ウェブカメラ:"+dirname_w+"に保存されます。")
print("※保存先の変更は、cc2.pyの編集で行えます。")
ans = int(input("録画を開始するには、1を入力してください。"))
if not (ans == 1):
  sys.exit()

for i in range(frame):
  if (camera_r == True):
    ret, im_r = cap_r.read()
  if (camera_w == True):
    ret2, im_w = cap_w.read()
  print(str(i+1)+"回目の撮影です。")
  last = frame - (i+1)
  print("あと" + str(last) + "回、"+str(last*wait/60)+"分、"+str(last * picture_gb * 1000)+"mgです。")

  tm=datetime.datetime.today().strftime("%Y/%m/%d %X")
  ftm=datetime.datetime.today().strftime("%Y%m%d%H%M%S")
  if (camera_r == True):
    if (camera_r_flip == True):
      im_r = cv2.flip(im_r , -1)
    cv2.putText(im_r,tm,(20,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))
    file_name = os.path.join(dirname_r,camera_r_text+str(ftm)+".jpg")
    print ("[保存完了]ファイル名:"+str(file_name))
    cv2.imwrite(file_name, im_r)
  if (camera_w == True):
    if (camera_w_flip == True):
      im_w = cv2.flip(im_w , -1)
    cv2.putText(im_w,tm,(20,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))
    file_name2 = os.path.join(dirname_w,camera_w_text+str(ftm)+".jpg")
    print ("[保存完了]ファイル名:"+str(file_name2))
    cv2.imwrite(file_name2, im_w)

  sleep(wait)


print("全録画が完了しました。")
cap.release()
cv2.destroyAllWindows()
