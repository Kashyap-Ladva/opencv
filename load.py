import cv2

pathToImage = 'images/math-1500720_640.jpg'

img = cv2.imread(pathToImage)

cv2.imshow('Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()