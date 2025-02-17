import cv2
import os

class FaceRegistration:
    def __init__(self, student, save_dir="../data"):
        self.student = student
        self.save_dir = save_dir
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def record_video(self):
        student_dir = os.path.join(self.save_dir, str(self.student.roll_number))
        os.makedirs(student_dir, exist_ok=True)

        cap = cv2.VideoCapture(0)
        count = 0

        while count<=100:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                count += 1
                face = frame[y:y + h, x:x + w]
                file_path = os.path.join(student_dir, f"face_{count}.jpg")
                cv2.imwrite(file_path, face)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Recording Faces", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
                break

        cap.release()
        cv2.destroyAllWindows()

        return student_dir

    def update_student_folder(self):
        student_dir = self.record_video()
        self.student.image_folder_path = student_dir
        self.student.save()
