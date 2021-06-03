# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera
from picamera import PiCamera
import logging
import socketserver
from threading import Condition
from http import server
from time import sleep
import base64
import requests, signal, _thread, sys

#camera = PiCamera()

prediction = "Prediction"

# PATH_IMG = '/home/pi/Pictures/image.jpg'



# camera =  picamera.PiCamera(resolution='640x480', framerate=24)

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

output = StreamingOutput()

# Take Photo
# def take_photo():
#     # Quickly blink status light
#     sleep(1)
#     # Start the camera preview
#     camera.start_preview(alpha=200)
#     # wait 2s or more for light adjustment
#     sleep(2) 
#     # Optional image rotation for camera
#     # --> Change or comment out as needed
#     #camera.rotation = 270
#     #Input image file path here
#     # --> Change image path as needed
#     camera.capture(PATH_IMG)
#     #Stop camera
#     camera.stop_preview()
    # #white_led.off()
    # sleep(1)
    # #print("Picture taken")

def predict(img):
    # Create base64 encoded string
    # with open(img, "rb") as f:
    global prediction
    image_string = base64.b64encode(img.getvalue()).decode("utf-8")
        
    # Get response from POST request
    response = requests.post(
        url="http://192.168.1.127:38101/v1/predict/c4c761fa-2662-4d55-8d6a-4923145e46c7",
        json={"image": image_string},
    )
    data = response.json()
    results = data["predictions"][0]
    prediction = results["label"]
    return data




class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        PAGE="""\
        <html>
        <head>
        <meta http-equiv="refresh" content="7" />
        <title>Waste Scanner</title>
        </head>
        <body>
        <center><h1>Waste Scanner</h1></center>
        <center><img src="stream.mjpg" width="640" height="480"></center>
        <p> Prediction : %s </p>
        </body>
        </html>
        """ % (prediction)
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True




def server_start():        
    

    print("Server start")
    address = ('', 1337)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
    print("Server stopped.")

# def main():
#     while(1):
#         camera.wait_recording(1)
#         take_photo()
#         predictions = predict()
#         global prediction
#         results = predictions["predictions"][0]
#         prediction = results["label"]
#         # Print the top predicted label and its confidence
#         print("predicted label:\t{}\nconfidence:\t\t{}"
#             .format(results["label"], results["confidence"]))
#         #sleep(2)



# def quit(signo, _frame):
#     print("Interrupted by %d, shutting down" % signo)
#     camera.stop_recording()
#     sys.exit(0)

# if __name__ == '__main__':

#     camera.start_recording(output, format='mjpeg')

#     for sig in ('TERM', 'HUP', 'INT'):
#         signal.signal(getattr(signal, 'SIG'+sig), quit)

#     try:
#         _thread.start_new_thread( server_start, () )
#         _thread.start_new_thread( main, () )
#     except:
#        print ("Error: unable to start thread")

#     while 1:
#        pass


#     camera.stop_recording()
