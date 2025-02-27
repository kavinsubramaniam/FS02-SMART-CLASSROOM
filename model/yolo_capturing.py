import cv2
import torch
import os
import time
from ultralytics import YOLO

# Load YOLO model (Ensure correct path and export format)
model = YOLO('yolov11n-face.engine', task='detect')

# Create directory to save cropped faces
save_dir = './projects'
os.makedirs(save_dir, exist_ok=True)

# Open camera
cap = cv2.VideoCapture(0)
start = time.time()
count = 0

# Function to calculate distance from image center
def distance_from_center(box, frame_shape):
    img_center_x = frame_shape[1] / 2
    img_center_y = frame_shape[0] / 2
    box_center_x = (box[0] + box[2]) / 2
    box_center_y = (box[1] + box[3]) / 2
    return ((box_center_x - img_center_x) ** 2 + (box_center_y - img_center_y) ** 2) ** 0.5

while count < 100:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Run YOLO face detection
    results = model(frame, conf=0.85)
    copy_frame = frame.copy()

    # Store all detected boxes
    detected_faces = []

    for result in results:
        for box in result.boxes.xyxy:
            detected_faces.append(box.cpu().numpy())

    # If faces are detected, prioritize the closest to center
    if detected_faces:
        best_face = min(detected_faces, key=lambda box: distance_from_center(box, frame.shape))
        x1, y1, x2, y2 = map(int, best_face)

        # Draw rectangle around the centered face
        cv2.rectangle(copy_frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

        # Save the cropped face
        face = frame[y1:y2, x1:x2]
        face_path = os.path.join(save_dir, f'face_{count}.jpg')
        cv2.imwrite(face_path, face)
        print(f"Saved: {face_path}")

        count += 1

    # Display the frame
    cv2.imshow("Frame", copy_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Captured 100 face images.")
print(f"Time taken: {time.time()-start}")
