import cv2
import face_recognition


cap = cv2.VideoCapture(0)

img1 = face_recognition.load_image_file('Sandesh.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
face =face_recognition.face_locations(img1)[0]
encodeFace = face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1, (face[3], face[0]), (face[1], face[2]), (0, 255, 0), 5)

while True:
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    frame = frame1[:, :,::-1]
    faceTest = face_recognition.face_locations(frame)[0]
    encodefaceTest = face_recognition.face_encodings(frame)[0]
    cv2.rectangle(frame1, (faceTest[3], faceTest[0]), (faceTest[1], faceTest[2]), (0, 255, 0), 5)
#img2 = face_recognition.load_image_file('test1.jpg')
    #for (top, right, bottom, left),encodefaceTest in zip(faceTest,encodefaceTest):
    result = face_recognition.compare_faces([encodeFace], encodefaceTest)
    face_distance = face_recognition.face_distance([encodeFace], encodefaceTest)
    print(type(result))
    if (result[0] == True):
        cv2.putText(frame1, "Sandesh", (faceTest[3], faceTest[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    #else:
        #cv2.putText(frame1, "Unknown", (faceTest[3], faceTest[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("test", frame1)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

