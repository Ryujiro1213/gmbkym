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
