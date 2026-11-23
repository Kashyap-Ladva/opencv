
from pathlib import Path
import cv2

# Step 1: Define output path
output_folder = Path(__file__).resolve().parent.parent / "recordings"

output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / "webcam_recording.mp4"

# Step 2: Access webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam!")
    exit()

# Step 3: Define recording FPS
fps = 20.0

writer = None

print("Webcam connected!")
print("Press Q to stop recording.")

# Step 4: Capture and record webcam frames
while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot capture frame!")
        break

    # Get actual frame dimensions
    height, width = frame.shape[:2]

    # Initialize VideoWriter using actual frame size
    if writer is None:

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        writer = cv2.VideoWriter(
            str(output_path),
            fourcc,
            fps,
            (width, height)
        )

        if not writer.isOpened():
            print("Error: Cannot create video file!")
            break

        print("Recording started!")
        print("Resolution:", width, "x", height)

    # Write current frame into video
    writer.write(frame)

    # Display webcam feed
    cv2.imshow("Webcam Recorder", frame)

    # Press Q to stop recording
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Step 5: Release resources
cap.release()

if writer is not None:
    writer.release()

cv2.destroyAllWindows()

print("Recording stopped!")

if output_path.exists():
    print("Video saved successfully at:")
    print(output_path)
