import cv2

pathToImage = 'images\\BigBangTheoryGettyImages-503820038.jpg'

image = cv2.imread(pathToImage)

# 1. Average Blur
average_blur = cv2.blur(image, (7, 7))

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

# 3. Median Blur
median_blur = cv2.medianBlur(image, 7)

# 4. Bilateral Filter
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

# Display all images
cv2.imshow("Original", image)
cv2.imshow("Average Blur", average_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Blur", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()