import cv2
import face_recognition

img1 = face_recognition.load_image_file('Sandesh.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1 = cv2.resize(img1,(640,640))

img2 = face_recognition.load_image_file('biden.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img2,(640,640))

face = face_recognition.face_locations(img1)[0]
#print(face)
encodeFace = face_recognition.face_encodings(img1)[0]
#print(encodeFace)
cv2.rectangle(img1,(face[3],face[0]),(face[1],face[2]),(0,255,0),5)



faceTest = face_recognition.face_locations(img2)[0]
#print(faceTest)
encodefaceTest = face_recognition.face_encodings(img2)[0]
#print(encodefaceTest)
cv2.rectangle(img2,(faceTest[3],faceTest[0]),(faceTest[1],faceTest[2]),(0,255,0),5)

result = face_recognition.compare_faces([encodeFace],encodefaceTest)
face_distance = face_recognition.face_distance([encodeFace],encodefaceTest)
print(type(result))
if (result[0] == True):
    cv2.putText(img2,"Sandesh",(faceTest[3],faceTest[0]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

else:
    cv2.putText(img2, "Unknown", (faceTest[3],faceTest[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#print(result, face_distance)
#cv2.imshow("frame",img1)
cv2.imshow("test",img2)
cv2.waitKey()
cv2.destroyAllWindows()