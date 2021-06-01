from flask import Flask, render_template, Response
# import imutils
# import picamera
# import cv2
# import socket
# import io
# from imutils.video import VideoStream
# import threading
# import datetime
# import time
from test2 import BarcodeScan, get_frame
# outputFrame = None
# lock = threading.Lock()


app = Flask(__name__)

# vs = VideoStream(usePiCamera=1).start()
# time.sleep(2.0)

@app.route('/')
def index():
  return render_template('/index.html')

# def barcode_scan():
#   global vs, outputFrame, lock
  
#   bs = BarcodeScan(vs)
#   frame = bs.get_frame()
#   with lock:
#     outputFrame = frame.copy()


def gen(test2):
  # global outputFrame, lock

  # while True:
  #   with lock:
  #     if outputFrame is None:
  #       continue
      
  #     (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

  #     if not flag:
  #       continue
      
  frame = get_frame()
  yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen(BarcodeScan()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/scan-page.html')
def scan():
  return render_template('/scan-page.html')

@app.route('/learn-more.html')
def learnmore():
  return render_template('/learn-more.html')

@app.route('/about.html')
def about():
  return render_template('/about.html')


if __name__ == '__main__':
  app.run(host='192.168.1.50', port=8080, debug=True, threaded=True)