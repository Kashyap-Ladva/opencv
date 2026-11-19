import cv2

pathToImage = 'images\\math-1500720_640.jpg'

image = cv2.imread(pathToImage)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blur, 100, 200)

# Create kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3, 3)
)

# Apply dilation
dilated = cv2.dilate(
    edges,
    kernel,
    iterations=1
)
#Apply erosion
eroded = cv2.erode(
    dilated,
    kernel,
    iterations=1
)
# Display
cv2.imshow("Original Edges", edges)
cv2.imshow("Dilated Image", dilated)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()