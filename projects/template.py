import cv2

# Load images
img = cv2.imread(r"D:\opencv\cropped_objects\object_13.jpg")
template = cv2.imread(r"D:\opencv\images\math-1500720_640.jpg")

# Match template
result = cv2.matchTemplate(
    img,
    template,
    cv2.TM_CCOEFF_NORMED
)

# Find best match
_, max_val, _, max_loc = cv2.minMaxLoc(result)

# Set threshold
threshold = 0.8

if max_val >= threshold:

    h, w = template.shape[:2]

    # Draw rectangle
    cv2.rectangle(
        img,
        max_loc,
        (max_loc[0] + w, max_loc[1] + h),
        (0, 255, 0),
        2
    )

    print("Template Found:", max_val)

else:
    print("Template Not Found")

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()