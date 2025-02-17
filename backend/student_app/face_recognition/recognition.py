import cv2
import numpy as np

class FaceRecognition:
    def __init__(self, model_file="face_recognizer.yml"):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(model_file)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def recognize_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        results = []
        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            id_, confidence = self.recognizer.predict(face)
            results.append((id_, confidence, (x, y, w, h)))

        return results
