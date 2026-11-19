
import cv2
import os

# Step 1: Load image
pathToImage = 'images\\seeds.jpg'

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
    50,
    150
)

# Step 5: Create Mask
mask = edges.copy()

masked_image = cv2.bitwise_and(
    image,
    image,
    mask=mask
)

# Step 6: Find contours
contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Step 7: Create output image
output = image.copy()

count = 0

# Step 8: Process contours
for contour in contours:

    area = cv2.contourArea(contour)

    # Ignore small contours
    if area < 20:
        continue

    # Get bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Draw contour
    cv2.drawContours(
        output,
        [contour],
        -1,
        (0, 255, 0),
        1
    )

    # Draw dynamic numbering
    cv2.putText(
        output,
        str(count + 1),
        (x, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.4,
        (0, 0, 255),
        1
    )

    count += 1

# Step 9: Display results
print("Total detected contours:", count)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edges", edges)
cv2.imshow("Detected Contours", output)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
