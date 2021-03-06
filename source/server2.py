from flask import Flask, render_template, Response
import imutils
import picamera
import cv2
import socket
import io
from imutils.video import VideoStream
import threading
import datetime
import time
from camera_pi2 import Camera

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/scan-page.html')
def scan():
  category = Camera().get_prediction()
  return render_template('/scan-page.html', category=category)

def gen(camera):
    # """Video streaming generator function."""
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/learn-more.html')
def learnmore():
  return render_template('/learn-more.html')

@app.route('/about.html')
def about():
  return render_template('/about.html')


if __name__ == '__main__':
  app.run(host='192.168.1.50', port=8080, debug=True, threaded=True)
