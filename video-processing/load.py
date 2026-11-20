from pathlib import Path
import cv2

video_path = Path(__file__).resolve().parent.parent / "videos" / "kitten.mp4"
cap = cv2.VideoCapture(str(video_path))

# Step 2: Check whether video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Step 3: Read and display video frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended!")
        break

    cv2.imshow("dog", frame)

    # Wait for 25 milliseconds
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Step 4: Release resources
cap.release()

cv2.destroyAllWindows()
