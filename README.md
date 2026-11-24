# OpenCV Python Practice Projects

A collection of beginner-friendly OpenCV examples covering image processing, video processing, computer-vision effects, and object or face detection. The repository also includes sample images, videos, detected outputs, cropped objects, and a few project experiments.

## Features

### Image processing

- Loading and converting images
- Grayscale conversion, blur, edge, contour, and mask operations
- Morphological dilation and erosion
- Image padding and channel splitting
- Bounding-box detection and object cropping
- Shadow removal and seed image processing

### Video processing

- Loading video files and reading frame properties
- Extracting individual frames
- Resizing and converting video frames to grayscale
- Recording from a webcam
- Resolution and FPS experiments

### Computer vision projects

- Face detection with a webcam
- Face clustering with DeepFace and DBSCAN
- Vehicle detection with a Haar cascade
- License plate recognition with `fast_alpr` and YOLO models
- Invisibility-cloak effect using color masks
- Virtual drawing with colored objects
- Cartoon-style image filtering

## Project structure

```text
opencv/
├── image-processing/      Image transformation and contour examples
├── video-processing/      Video loading, resizing, recording, and webcam examples
├── projects/              Face, vehicle, license plate, and visual effect demos
├── images/                Input images
├── videos/                Input videos and the vehicle Haar cascade
├── output/                Generated images
├── cropped_objects/       Images produced by object-cropping scripts
├── recordings/            Webcam recordings created by recording.py
└── Face_Clustering/       Face-cluster output folders
```

## Requirements

- Python 3.10 or newer (Python 3.12 environment files are included in this repository)
- OpenCV
- NumPy
- Optional packages for the specialized projects:
  - Pillow
  - pandas
  - scikit-learn
  - DeepFace
  - TensorFlow or another backend supported by DeepFace
  - fast-alpr

## Setup

Open a terminal in the repository root.

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-contrib-python numpy pillow pandas scikit-learn deepface fast-alpr
```

If PowerShell blocks script activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

You can install only the packages needed by the scripts you plan to run. The repository also contains virtual-environment requirement lists under `projects/venv312/`.

> The repository includes virtual-environment folders, but they should not be committed or used as portable environments. Create a fresh environment for your own machine.

## Running the examples

Run scripts from the project directory or repository root. Many scripts use `cv2.imshow`, so a desktop session is required.

```powershell
python image-processing\contour.py
python video-processing\load.py
python projects\face.py
python projects\cartoon.py
```

For scripts that use the webcam, make sure the camera is available and close the OpenCV window with `Esc`, or use the script-specific key shown in its output.

### Common examples

| Script | Description | Exit key |
|---|---|---|
| `image-processing/contour.py` | Detect and draw contours | Window close / Esc |
| `image-processing/cropdetect.py` | Crop connected objects from an image | Window close |
| `image-processing/edge.py` | Apply edge detection | Window close |
| `video-processing/load.py` | Read and display a video | `q` |
| `video-processing/webcam.py` | Display a webcam feed | `Esc` |
| `video-processing/recording.py` | Record the webcam feed | `q` |
| `projects/face.py` | Detect faces from the webcam | `Esc` |
| `projects/cartoon.py` | Create a cartoon-style image | `Esc` |
| `projects/cloak.py` | Run the red-cloak effect | `Esc` |
| `projects/drawing.py` | Draw with detected colored objects | `Esc` |
| `projects/vehicle.py` | Detect cars in a video | `Esc` |
| `projects/license.py` | Recognize license plates in a video | `q` |
| `projects/face_cluster.py` | Cluster faces extracted from a video | Completion only |

## Important paths

Several scripts contain Windows absolute paths such as `D:\opencv\...`. Update these constants to match the location of your clone:

- `projects/vehicle.py` uses `videos/cars.xml` and `videos/car-video.mp4`
- `projects/license.py` uses `videos/license.mp4`
- `projects/face_cluster.py` uses `videos/Footage.mp4` and writes to `projects/Face_Clustering`
- `projects/cartoon.py` uses an image under `images/`

Using paths derived from `__file__` is recommended so scripts work even when the repository is cloned elsewhere.

## Troubleshooting

- **Camera cannot be opened:** Check that another application is not using the webcam and verify that the camera is enabled in Windows privacy settings.
- **Image or video not found:** Run the script from the repository root and verify the path in the script.
- **Haar cascade cannot be loaded:** Ensure `opencv-contrib-python` is installed and the full cascade path is valid.
- **DeepFace or fast-alpr dependencies fail:** Create a fresh virtual environment and install only the optional package needed for that project. Model downloads may require internet access on the first run.
- **Video codec or writer error:** Try the bundled `.mp4` or `.avi` codec alternatives supported by your OpenCV build.

## Notes

- Some scripts are educational examples and may require model files or package-specific downloads.
- Add new example inputs to `images/` or `videos/` and keep generated results in `output/`, `cropped_objects/`, or `recordings/`.
- Video and environment directories are excluded through `.gitignore`.
