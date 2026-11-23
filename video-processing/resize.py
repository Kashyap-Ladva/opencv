
from pathlib import Path
import cv2

# Step 1: Load video
video_path = Path(__file__).resolve().parent.parent / "videos" / "kitten.mp4"

cap = cv2.VideoCapture(str(video_path))

# Step 2: Check video
if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Step 3: Read and resize video frames
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video ended!")
        break

    # Original frame dimensions
    original_height, original_width = frame.shape[:2]

    # Resize frame
    resized_frame = cv2.resize(frame, (480, 270))

    # Display original and resized dimensions
    print("Original:", original_width, "x", original_height)
    print("Resized:", 480, "x", 270)

    # Display resized video
    cv2.imshow("Resized Kitten Video", resized_frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Step 4: Release resources
cap.release()
cv2.destroyAllWindows()
