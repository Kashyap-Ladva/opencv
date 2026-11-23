
import cv2

# Step 1: Access webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam!")
    exit()

# Step 2: Get original camera properties
original_fps = cap.get(cv2.CAP_PROP_FPS)

original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

original_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Original Webcam Properties")
print("FPS:", original_fps)
print("Width:", original_width)
print("Height:", original_height)

# Step 3: Request new resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Step 4: Get updated camera properties
new_fps = cap.get(cv2.CAP_PROP_FPS)

new_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

new_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("\nUpdated Webcam Properties")
print("FPS:", new_fps)
print("Width:", new_width)
print("Height:", new_height)

# Step 5: Capture and display webcam
while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot capture frame!")
        break

    # Get actual frame dimensions
    frame_height, frame_width = frame.shape[:2]

    cv2.imshow("My Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Step 6: Release resources
cap.release()

cv2.destroyAllWindows()
