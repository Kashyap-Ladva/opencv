
import cv2

# Step 1: Connect to webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("Cannot access webcam.")

# Step 2: Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise Exception("Error loading face cascade.")

# Step 3: Capture frames continuously
while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        break

    # Flip frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Initialize face counter
    i = 0

    # Process every detected face
    for (x, y, w, h) in faces:

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Increment counter
        i += 1

        # Display face number
        cv2.putText(
            frame,
            "Face " + str(i),
            (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    # Display total face count
    cv2.putText(
        frame,
        "Total Faces: " + str(i),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Display frame
    cv2.imshow("Face Detection", frame)

    # Press 'Esc' to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
