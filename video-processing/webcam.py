
import cv2

# Step 1: Access webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam!")
    exit()

print("Webcam connected successfully!")

frame_count = 0

# Step 2: Capture live frames
while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot capture frame!")
        break

    frame_count += 1

    # Step 3: Display frame
    cv2.imshow("Live Webcam", frame)

    # Print information for first 5 frames
    if frame_count <= 5:

        print("Frame:", frame_count)
        print("Frame Shape:", frame.shape)
        print("--------------------")

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Step 4: Release resources
cap.release()

cv2.destroyAllWindows()

print("Total frames captured:", frame_count)
