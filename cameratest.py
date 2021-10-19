import RPi.GPIO as GPIO
import signal
import sys
import time
import picamera
import cv2
import os
from time import sleep

GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  #sw_status = GPIO.input (17)
  #if sw_status == 0:
  a=input()
  with picamera.PiCamera() as camera:
     camera.resolution = (1024, 768)
  if a==1:
      camera.start_preview()
      time.sleep(2)
      camera.capture('my_pic.jpg')
      print('Camera End!')
            
signal.pause()            


import cv2
import os

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, jpg), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')
