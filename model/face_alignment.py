import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
import redis
import msgpack
import time
import matplotlib.pyplot as plt


# Initialize Redis for caching
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Load InsightFace model (5-point landmark detection)
app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))  # Use GPU (ctx_id=0)

# Helper: Affine Transformation for face alignment
def align_face(img, landmarks, output_size=(112, 112)):
    # Reference points for aligned face
    src_pts = np.array([
        [38.2946, 51.6963],   # Left eye
        [73.5318, 51.5014],   # Right eye
        [56.0252, 71.7366],   # Nose
        [41.5493, 92.3655],   # Left mouth corner
        [70.7299, 92.2041]    # Right mouth corner
    ], dtype=np.float32)

    # Convert detected landmarks
    dst_pts = np.array(landmarks, dtype=np.float32)

    # Compute affine matrix and warp
    M = cv2.estimateAffinePartial2D(dst_pts, src_pts, method=cv2.LMEDS)[0]
    aligned_face = cv2.warpAffine(img, M, output_size, borderValue=0.0)

    return aligned_face

# Cache face embedding in Redis (with 1-hour expiration)
def cache_face_embedding(face_id, embedding):
    packed_data = msgpack.packb(embedding)
    redis_client.setex(face_id, 3600, packed_data)

# Retrieve face embedding from Redis
def retrieve_face_embedding(face_id):
    packed_data = redis_client.get(face_id)
    if packed_data:
        return msgpack.unpackb(packed_data)
    return None

# Process input from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Detect faces
    faces = app.get(frame)

    if faces:
        for face in faces:
            # Face bounding box and landmarks
            x1, y1, x2, y2 = face.bbox.astype(int)
            landmarks = face.kps

            # Align face using Affine Transformation
            aligned_face = align_face(frame, landmarks)

            # Generate unique face ID using facial features
            face_id = f"face_{int(time.time())}"

            # # Cache aligned face embedding
            # cache_face_embedding(face_id, face.embedding)

            # Visualize bounding box and aligned face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # cv2.imshow("Aligned Face", aligned_face)
            plt.imshow(cv2.cvtColor(aligned_face, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()

            print(f"Cached Face ID: {face_id}")

    # Display the frame
    # cv2.imshow("Webcam Feed", frame)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
