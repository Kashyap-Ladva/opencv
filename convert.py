import cv2

pathToImage = 'images\\BigBangTheoryGettyImages-503820038.jpg'

image = cv2.imread(pathToImage)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, binary_image = cv2.threshold(
    gray_image,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original BGR", image)
cv2.imshow("RGB", cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR))
cv2.imshow("Grayscale", gray_image)
cv2.imshow("Binary", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()