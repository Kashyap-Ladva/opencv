import cv2

pathToImage = 'images\\math-1500720_640.jpg'
# Step 1: Load image
image = cv2.imread(pathToImage)

if image is None:
    print("Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Step 3: Apply Gaussian Blur
blur = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

# Step 4: Edge Detection
edges = cv2.Canny(
    blur,
    100,
    200
)

# Step 5: Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Step 6: Create output directory
import os

os.makedirs("cropped_objects", exist_ok=True)

count = 0

# Step 7: Crop detected objects
for contour in contours:

    area = cv2.contourArea(contour)

    # Ignore small contours
    if area < 100:
        continue

    # Get bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Crop object
    cropped = image[y:y+h, x:x+w]

    # Save cropped image
    filename = f"cropped_objects/object_{count}.jpg"

    cv2.imwrite(filename, cropped)

    print("Saved:", filename)

    count += 1

print("Total cropped objects:", count)