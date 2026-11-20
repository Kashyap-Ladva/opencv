import cv2

pathToImage = 'images\\math-1500720_640.jpg'
# Load image
image = cv2.imread(pathToImage)

if image is None:
    print("Image not found!")
    exit()

# Add black border
black_border = cv2.copyMakeBorder(
    image,
    50,  # Top
    50,  # Bottom
    50,  # Left
    50,  # Right
    cv2.BORDER_CONSTANT,
    value=(0, 0, 0)
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Black Border", black_border)

cv2.waitKey(0)
cv2.destroyAllWindows()