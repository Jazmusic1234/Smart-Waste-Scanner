#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera_pi.py
#  
# https://github.com/Mjrovai/Video-Streaming-with-Flask/blob/master/camWebServer2/camera_pi.py  
#  
import time
import io
import threading
from numpy.lib.type_check import imag
import picamera
import picamera.array
import cv2
from basic import scanning
from wastescan import predict
import numpy as np
from PIL import Image
import os

img = ""
typeOfSort = ""

class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    global img
    # global typeOfSort
    # typeOfSort = typeOfSort

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:

            # camera setup
            camera.resolution = (320, 240)

            # let camera warm up
            camera.start_preview()
            time.sleep(2)
            
            stream = io.BytesIO()

            while True:
                camera.capture(stream, format='png')
                global img 
                img = Image.open(stream)
                
                
                data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                image = cv2.imdecode(data, 1)

                print(type(image))

                stream.seek(0)
                
            # if(typeOfSort == "scan"):
                img = scanning(image)
            # elif(typeOfSort == "classification"):
                prediction = predict(stream)

                is_success, buffer = cv2.imencode(".png", img)
                # stream = io.BytesIO(buffer)
                cls.frame = io.BytesIO(buffer).read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

            # if there hasn't been any clients asking for frames in
            # the last 10 seconds stop the thread
    #         if time.time() - cls.last_access > 10:
    #             break
        cls.thread = None           
    
    