
from pathlib import Path
import cv2

# Step 1: Load video
video_path = Path(__file__).resolve().parent.parent / "videos" / "kitten.mp4"

cap = cv2.VideoCapture(str(video_path))

# Step 2: Check video
if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Step 3: Read and process video frames
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video ended!")
        break

    # Convert current frame into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display grayscale video
    cv2.imshow("Grayscale Kitten Video", gray)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Step 4: Release resources
cap.release()
cv2.destroyAllWindows()
