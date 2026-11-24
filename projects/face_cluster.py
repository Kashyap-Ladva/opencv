import cv2
import os
import numpy as np
from deepface import DeepFace
from sklearn.cluster import DBSCAN

VIDEO_PATH = r"D:\opencv\videos\Footage.mp4"
OUTPUT_FOLDER = "Face_Clustering"
FRAME_INTERVAL = 1       # Read one frame every 1 second
EPS = 0.30               # DBSCAN distance threshold
MIN_SAMPLES = 2

embeddings = []
face_images = []

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    raise Exception("Could not open video. Check VIDEO_PATH.")

fps = cap.get(cv2.CAP_PROP_FPS)
frame_step = max(1, int(fps * FRAME_INTERVAL))
frame_number = 0

print("Extracting faces and generating embeddings...")

while True:
    success, frame = cap.read()

    if not success:
        break

    if frame_number % frame_step == 0:
        try:
            faces = DeepFace.represent(
                img_path=frame,
                model_name="Facenet",
                detector_backend="opencv",
                enforce_detection=True
            )

            for face in faces:
                embeddings.append(face["embedding"])

                area = face["facial_area"]
                x, y = area["x"], area["y"]
                w, h = area["w"], area["h"]

                crop = frame[y:y+h, x:x+w]
                face_images.append(crop)

        except ValueError:
            pass  # No face detected in this frame

    frame_number += 1

cap.release()

print("Total faces detected:", len(face_images))

if len(face_images) == 0:
    print("No faces found.")
    raise SystemExit

# Group similar face embeddings
print("Clustering faces...")

labels = DBSCAN(
    eps=EPS,
    min_samples=MIN_SAMPLES,
    metric="cosine"
).fit_predict(np.array(embeddings))

# Save each group in a separate folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for i, (face_image, label) in enumerate(zip(face_images, labels)):

    if label == -1:
        folder = "Unclustered"
    else:
        folder = f"Person_{label + 1}"

    folder_path = os.path.join(OUTPUT_FOLDER, folder)
    os.makedirs(folder_path, exist_ok=True)

    image_path = os.path.join(folder_path, f"face_{i + 1}.jpg")
    cv2.imwrite(image_path, face_image)

print("Clustering completed!")
print("People found:", len(set(labels)) - (1 if -1 in labels else 0))
print("Output saved in:", OUTPUT_FOLDER)
