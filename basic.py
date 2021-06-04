import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
from googletrans import Translator

def classify( packaging_tags ):
    words = []
    for packaging in packaging_tags:
        packaging = packaging.replace('-', ' ').split(' ')
        for i in packaging:
            words.append(i.lower())
    plastic_keywords = ['plastic']
    glass_keywords = ['glass']
    paper_keywords = ['paper']
    metal_keywords = ['metal', 'aluminium', 'aluminum']
    cardboard_keywords = ['cardboard', 'carton'] 
    
    translation_obj = translator.translate(words, dest='en')
    translated_words = [obj.text for obj in translation_obj]
    words.extend(translated_words)

    
    for keyword in plastic_keywords:
        if keyword in words:
            return 'plastic'

    for keyword in glass_keywords:
        if keyword in words:
            return 'glass'

    for keyword in paper_keywords:
        if keyword in words:
            return 'paper'

    for keyword in metal_keywords:
        if keyword in words:
            return 'metal'

    for keyword in cardboard_keywords:
        if keyword in words:
            return 'cardboard'

    return "Nothing found"

 
# img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
translator = Translator()

previous_scan = ""
while True:
    _, img = cap.read()
    # Display the resulting frame
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame',gray)
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
            packaging_tags = response['product']['packaging_tags']
            print( "Packaging Tags:", packaging_tags )
            if "image_front_small_url" not in response['product']:
                print( "Error: No picture found for product! Barcode read: " + myData )
                image = ""
            else:
                image = response['product']['image_front_small_url']
            print( "Image:", image )

            # packaging
            print( classify(packaging_tags) )

    cv2.imshow('Result',img)
    
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
