
import cv2
import MTCNN

#todo: crop face first for best results!
face = cv2.imread('face.jpg')
id = cv2.imread('id.jpg')

detector = MTCNN()
face_face = detector.detect_faces(face)
id_face = detector.detect_faces(id)

x, y, w, h = face_face[0]['box']
cv2.imwrite('a.png', face[y:y+h, x:x+w])

x, y, w, h = id_face[0]['box']
cv2.imwrite('b.png', id[y:y+h, x:x+w])
