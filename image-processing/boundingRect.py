import cv2

pathToImage = 'images\\math-1500720_640.jpg'

# Load image
image = cv2.imread(pathToImage)

if image is None:
    print("Image not found!")
    exit()

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 100, 200)

# Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Copy original image
output = image.copy()

# Loop through detected contours
for contour in contours:

    # Calculate contour area
    area = cv2.contourArea(contour)

    # Ignore very small contours
    if area < 100:
        continue

    # Calculate bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Draw rectangle
    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    # Display coordinates
    print("X:", x, "Y:", y, "Width:", w, "Height:", h)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Detected Objects", output)

cv2.waitKey(0)
cv2.destroyAllWindows()