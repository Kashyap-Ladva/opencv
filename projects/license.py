
import cv2
import time
from statistics import mean
from fast_alpr import ALPR

# =====================================
# 1. INITIALIZE ALPR
# =====================================

alpr = ALPR(
    detector_model="yolo-v9-s-608-license-plate-end2end",
    ocr_model="cct-xs-v2-global-model",
    detector_conf_thresh=0.25,
    ocr_device="cpu"
)

# =====================================
# 2. LOAD VIDEO
# =====================================

VIDEO_PATH = r"D:\opencv\videos\license.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    raise Exception("Cannot open video!")

fps = cap.get(cv2.CAP_PROP_FPS)
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 24

out = cv2.VideoWriter(
    "output_yolo.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (W, H)
)

# =====================================
# 3. OPTIMIZATION SETTINGS
# =====================================

FRAME_SKIP = 5
SCALE = 1.5

frame_count = 0
cached_detections = []
recognized_plates = set()

start_time = time.time()

print("Starting License Plate Recognition...")

# =====================================
# 4. PROCESS VIDEO
# =====================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    # Run YOLO + OCR every 5 frames
    if frame_count % FRAME_SKIP == 0:

        # Upscale frame for small plates
        resized = cv2.resize(
            frame,
            None,
            fx=SCALE,
            fy=SCALE,
            interpolation=cv2.INTER_CUBIC
        )

        # Detect and recognize plates
        results = alpr.predict(resized)

        cached_detections = []

        for result in results:

            detection = result.detection
            bbox = detection.bounding_box

            # Convert coordinates to original frame size
            x1 = int(bbox.x1 / SCALE)
            y1 = int(bbox.y1 / SCALE)
            x2 = int(bbox.x2 / SCALE)
            y2 = int(bbox.y2 / SCALE)

            # Keep coordinates inside frame
            x1 = max(0, min(x1, W - 1))
            y1 = max(0, min(y1, H - 1))
            x2 = max(0, min(x2, W - 1))
            y2 = max(0, min(y2, H - 1))

            plate_text = "Plate detected"
            confidence = 0.0

            if result.ocr is not None:

                plate_text = result.ocr.text.strip()

                ocr_conf = result.ocr.confidence

                if isinstance(ocr_conf, list):
                    confidence = mean(ocr_conf) if ocr_conf else 0.0
                else:
                    confidence = ocr_conf or 0.0

                if plate_text:
                    print(
                        f"Plate: {plate_text} | "
                        f"Confidence: {confidence:.2f}"
                    )

                    recognized_plates.add(plate_text)

            cached_detections.append(
                (x1, y1, x2, y2, plate_text, confidence)
            )

    # =================================
    # 5. DRAW DETECTIONS
    # =================================

    for x1, y1, x2, y2, text, confidence in cached_detections:

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        label = text

        if confidence > 0:
            label += f" ({confidence:.2f})"

        label_y = max(y1 - 10, 25)

        cv2.putText(
            frame,
            label,
            (x1, label_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 255, 0),
            2
        )

    # Frame counter
    cv2.putText(
        frame,
        f"Frame: {frame_count}",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # Display
    cv2.imshow("YOLO License Plate Recognition", frame)

    # Save output
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =====================================
# 6. RELEASE RESOURCES
# =====================================

cap.release()
out.release()
cv2.destroyAllWindows()

elapsed = time.time() - start_time

print("\n========== RESULTS ==========")

print("Total frames:", frame_count)
print("Processing time:", round(elapsed, 2), "seconds")

print("\nRecognized plates:")

for plate in sorted(recognized_plates):
    print(plate)

print("\nOutput saved as output_yolo.mp4")
