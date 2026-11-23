
from pathlib import Path
import cv2

# Step 1: Load video
video_path = Path(__file__).resolve().parent.parent / "videos" / "kitten.mp4"

cap = cv2.VideoCapture(str(video_path))

# Step 2: Check video
if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Step 3: Select a particular frame
frame_number = 100

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Step 4: Read the selected frame
ret, frame = cap.read()

# Step 5: Display the frame
if ret:
    print("Successfully extracted frame:", frame_number)

    cv2.imshow("Selected Frame", frame)

    cv2.waitKey(0)

else:
    print("Error: Cannot read the selected frame!")

# Step 6: Release resources
cap.release()

cv2.destroyAllWindows()
