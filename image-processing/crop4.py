import cv2

pathToImage = 'images/sample_image.jpg'

image = cv2.imread(pathToImage)

height, width = image.shape[:2]

mid_height = height // 2
mid_width = width // 2

top_left = image[0:mid_height, 0:mid_width]

top_right = image[0:mid_height, mid_width:width]

bottom_left = image[mid_height:height, 0:mid_width]

bottom_right = image[mid_height:height, mid_width:width]

cv2.imshow("Top Left", top_left)
cv2.imshow("Top Right", top_right)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Bottom Right", bottom_right)

cv2.waitKey(0)
cv2.destroyAllWindows()