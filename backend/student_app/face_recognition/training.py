import cv2
import os
import numpy as np

class FaceTrainer:
    def __init__(self, dataset_dir="face_datasets", model_file="face_recognizer.yml"):
        self.dataset_dir = dataset_dir
        self.model_file = model_file
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def train_model(self):
        faces, ids = [], []
        for student_folder in os.listdir(self.dataset_dir):
            student_path = os.path.join(self.dataset_dir, student_folder)
            if not os.path.isdir(student_path):
                continue

            for img_name in os.listdir(student_path):
                img_path = os.path.join(student_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

                faces.append(img)
                ids.append(int(student_folder))  # Use student roll number or ID

        self.recognizer.train(faces, np.array(ids))
        self.recognizer.save(self.model_file)
        return True
