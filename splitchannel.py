
from PIL import Image
import cv2
import numpy as np

pathToImage = 'images\\BigBangTheoryGettyImages-503820038.jpg'

# Load image using PIL
image = Image.open(pathToImage)

# Convert image into NumPy array (RGB)
rgb_image = np.array(image.convert("RGB"))

# Extract individual channels
red_channel = rgb_image[:, :, 0]
green_channel = rgb_image[:, :, 1]
blue_channel = rgb_image[:, :, 2]

# Create empty RGB images
red_image = np.zeros_like(rgb_image)
green_image = np.zeros_like(rgb_image)
blue_image = np.zeros_like(rgb_image)

# Assign individual channels
red_image[:, :, 0] = red_channel
green_image[:, :, 1] = green_channel
blue_image[:, :, 2] = blue_channel

# Convert RGB to BGR for OpenCV display
original_bgr = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
red_bgr = cv2.cvtColor(red_image, cv2.COLOR_RGB2BGR)
green_bgr = cv2.cvtColor(green_image, cv2.COLOR_RGB2BGR)
blue_bgr = cv2.cvtColor(blue_image, cv2.COLOR_RGB2BGR)

# Display images
cv2.imshow("Original Image", original_bgr)
cv2.imshow("Red Channel", red_bgr)
cv2.imshow("Green Channel", green_bgr)
cv2.imshow("Blue Channel", blue_bgr)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
