import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    im2 = cv2.resize(img,(640,480))

    bbox, label, conf = cv.detect_common_objects(im2)
    output = draw_bbox(im2,bbox,label,conf)
    out = label
    def convert(text):
        audio = gTTS(text)
        audio.save('output.mp3')
        playsound('output.mp3')
    convert('Your list contains: {}'.format(out))
    print(out)
    cv2.imshow("image",img)

    k=cv2.waitKey(1)
    if k ==27 & 0xFF ==ord('q'):

        break

cap.release()
cv2.destroyAllWindows()