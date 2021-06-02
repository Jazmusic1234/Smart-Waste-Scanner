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
import numpy as np
from PIL import Image
import os


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    global img

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
            # output = io.StringIO()
            # for foo in camera.capture_continuous(stream, 'png',
                                                #  use_video_port=True):
            # for i, filename in enumerate(camera.capture_continuous('source/images/image{counter:02d}.png')):
            
            while True:
                camera.capture(stream, format='png')
                img = Image.open(stream)
                # img.save(stream, format='PNG')
                # imgByteArr = stream.getvalue()
                data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                image = cv2.imdecode(data, 1)

                # img = Image.frombuffer('RGB', (640,480), stream.getvalue())

                # with open('home\pi\Documents\Smart-Waste-Scanner\source\images\image01.png','wb') as f:
                #     f.write(imgByteArr)

                # with Image.open('home\pi\Documents\Smart-Waste-Scanner\source\images\image01.png', 'r') as im:
                #     im.show()
                # store frame
                # print("here")
                stream.seek(0)
                # _stream = stream.getvalue()
                # data = np.fromstring(_stream, dtype=np.uint8)
                # img = cv2.imdecode(data, 1)
                # yield img
                # file_bytes = np.asarray(bytearray(stream.read()), dtype=np.uint8)
                # img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                
                # f = open('home\pi\Documents\Smart-Waste-Scanner\source\images\image01.png', 'w')
                # b = stream.getvalue()
                # f.write(b.decode('utf-16'))
                # img = scanning('home\pi\Documents\Smart-Waste-Scanner\source\images\image01.png') 

                # b = open(img, 'r')
                # cls.frame = b.read()
                
                # Decode
                # data = stream.read().decode("utf-8", 'ignore')

                # with io.open('home\pi\Documents\Smart-Waste-Scanner\source\images\image01.png', 'w') as f:
                #     f.write(data)

                img = scanning(image)

                # im = Image.open(img)
                # im_resize = im.resize((500, 500))
                # buf = io.BytesIO()
                # im_resize.save(buf, format='PNG')
                is_success, buffer = cv2.imencode(".png", img)
                # stream = io.BytesIO(buffer)
                cls.frame = io.BytesIO(buffer).read()
                # decode_img = cv2.imdecode(np.frombuffer(io_buf.getbuffer(), np.uint8), -1)
                

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

            # if there hasn't been any clients asking for frames in
            # the last 10 seconds stop the thread
    #         if time.time() - cls.last_access > 10:
    #             break
        cls.thread = None           
    
    
         # with picamera.array.PiRGBArray(camera) as stream:
            #     camera.resolution = (320, 240)

            #     while True:
            #         camera.capture(stream, 'bgr', use_video_port=True)
            #         # stream.array now contains the image data in BGR order
            #         cv2.imshow('frame', stream.array)
            #         if cv2.waitKey(1) & 0xFF == ord('q'):
            #             break
            #         # reset the stream before the next capture
            #         stream.seek(0)
            #         stream.truncate()

            #     cv2.destroyAllWindows()

