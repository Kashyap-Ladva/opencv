
import numpy as np
import cv2
import time

# Step 1: Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not available!")
    exit()

time.sleep(2)

# Step 2: Capture background
background = None

for i in range(30):
    ret, background = cap.read()

    if not ret:
        print("Background capture failed!")
        cap.release()
        exit()

# Step 3: Initialize VideoWriter
height, width = background.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(
    'output.avi',
    fourcc,
    30.0,
    (width, height)
)

if not out.isOpened():
    print("VideoWriter initialization failed!")
    cap.release()
    exit()

# Step 4: Process webcam frames
while cap.isOpened():

    ret, img = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Detect red color - Range 1
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Detect red color - Range 2
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([179, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combine masks
    mask1 = cv2.bitwise_or(mask1, mask2)

    # Remove noise
    kernel = np.ones((3, 3), np.uint8)

    mask1 = cv2.morphologyEx(
        mask1,
        cv2.MORPH_OPEN,
        kernel,
        iterations=3
    )

    # Expand detected region
    mask1 = cv2.dilate(
        mask1,
        kernel,
        iterations=2
    )

    # Invert mask
    mask2 = cv2.bitwise_not(mask1)

    # Extract background pixels
    res1 = cv2.bitwise_and(
        background,
        background,
        mask=mask1
    )

    # Extract current frame pixels
    res2 = cv2.bitwise_and(
        img,
        img,
        mask=mask2
    )

    # Combine both results
    final_output = cv2.add(res1, res2)

    # Save output
    out.write(final_output)

    # Display output
    cv2.imshow("Final Output", final_output)

    k = cv2.waitKey(10)

    if k == 27:
        break

# Step 5: Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
