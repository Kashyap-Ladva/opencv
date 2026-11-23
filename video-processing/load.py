
from pathlib import Path
import cv2

# Step 1: Load video
video_path = Path(__file__).resolve().parent.parent / "videos" / "kitten.mp4"

cap = cv2.VideoCapture(str(video_path))

# Step 2: Check video
if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Step 3: Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Step 4: Display properties
print("Video FPS:", fps)

print("Video Width:", int(width))

print("Video Height:", int(height))

print("Video Resolution:", int(width), "x", int(height))

print("Total Frames:", int(total_frames))

# Step 5: Read and display video
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video ended!")
        break

    cv2.imshow("Kitten Video", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Step 6: Release resources
cap.release()
cv2.destroyAllWindows()
