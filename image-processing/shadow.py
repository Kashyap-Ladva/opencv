import cv2
import numpy as np

pathToImage = 'images\\BigBangTheoryGettyImages-503820038.jpg'
# Load image
image = cv2.imread(pathToImage)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split HSV channels
h, s, v = cv2.split(hsv)

# Define brightness threshold
threshold = 50

# Identify dark pixels
shadow_mask = cv2.inRange(
    v,
    0,
    threshold
)

# Remove small noise
kernel = np.ones((3, 3), np.uint8)

shadow_mask = cv2.morphologyEx(
    shadow_mask,
    cv2.MORPH_OPEN,
    kernel
)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("HSV Value Channel", v)
cv2.imshow("Dark Region Mask", shadow_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()