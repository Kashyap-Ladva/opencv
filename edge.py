import cv2
import numpy as np

pathToImage = 'images\\math-1500720_640.jpg'

# Load image
image = cv2.imread(pathToImage)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Sobel X: Vertical edges
sobel_x = cv2.Sobel(
    blur,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

# Sobel Y: Horizontal edges
sobel_y = cv2.Sobel(
    blur,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

# Convert to displayable 8-bit images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y
sobel_combined = cv2.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)
# Laplacian Edge Detection

laplacian = cv2.Laplacian(
    blur,
    cv2.CV_64F
)

laplacian = cv2.convertScaleAbs(laplacian)
# Canny Edge Detection

canny = cv2.Canny(
    blur,
    150,
    200
)
# Display
cv2.imshow("Original", image)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.imshow("Laplacian Edges", laplacian)
cv2.imshow("Canny Edges", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()