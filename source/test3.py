import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
from googletrans import Translator
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()

camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera)
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image - this array
    # will be 3D, representing the width, height, and # of channels
    img = frame.array

    # show the frame
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
