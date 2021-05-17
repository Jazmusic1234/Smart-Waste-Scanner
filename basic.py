import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
 
# img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

previous_scan = ""
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

        if( myData == previous_scan ):
            continue
        else:
            print("new data read " + myData)
            previous_scan = myData
            response = requests.get("https://world.openfoodfacts.org/api/v0/product/" + myData + ".json").json()
            if "product" not in response:
                print( "Error: This product cannot be found! Barcode read: " + myData )
                continue
            if "packaging_tags" not in response['product']:
                print( "Error: This product has no packaging information! Barcode read: " + myData )
                continue
            packaging = response['product']['packaging_tags']
            print( "Packaging: " + packaging )
            if "image_front_small_url" not in response['product']:
                print( "Error: No picture found for product! Barcode read: " + myData )
                image = ""
            else:
                image = response['product']['image_front_small_url']
            print( "Image: " + image )

    cv2.imshow('Result',img)
    cv2.waitKey(1)