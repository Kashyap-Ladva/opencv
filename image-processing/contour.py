import cv2

pathToImage = 'images\\math-1500720_640.jpg'

# Step 1: Load image
image = cv2.imread(pathToImage)

if image is None:
    print("Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Detect edges
edges = cv2.Canny(blur, 100, 200)

# Step 5: Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours:", len(contours))

# Step 6: Draw contours
contour_image = image.copy()

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Detected Edges", edges)
cv2.imshow("Detected Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()