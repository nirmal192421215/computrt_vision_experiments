# Computer Vision Experiments - Output

This document outlines the computer vision experiments implemented using Python and OpenCV, along with their input operations and output results.

---

## Experiment 1: Basic Image Reading & Grayscale Conversion
- **Source File**: `experiment1.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- **Output**: 
  - Displays original color image in the "Original Image" window.
  - Displays single-channel grayscale image in the "Grayscale Image" window.

---

## Experiment 2: Gaussian Blurring
- **Source File**: `experiment2.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.GaussianBlur(image_rgb, (15, 15), 0)`
- **Output**: 
  - Displays a side-by-side subplot comparing the sharp Original Image with the smoothed Gaussian Blurred Image.

---

## Experiment 3: Canny Edge Detection (Outline)
- **Source File**: `experiment3.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.Canny(gray_image, 100, 200)`
- **Output**: 
  - Displays a side-by-side subplot of the original RGB image and the black-and-white edge outline.

---

## Experiment 4: Histogram Equalization & Comparison
- **Source File**: `experiment4.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.equalizeHist(gray_image)` and `plt.hist()`
- **Output**: 
  - A 2x2 grid displaying the Original Image, Equalized Image, Original Intensity Histogram, and Equalized Histogram showing enhanced contrast.

---

## Experiment 5: Color Histogram Analysis
- **Source File**: `experiment5.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.calcHist([image], [i], None, [256], [0, 256])` for Blue, Green, and Red channels
- **Output**: 
  - Displays the original image alongside the plotted distribution curves for all three color channels (B, G, R).

---

## Experiment 6: Image Erosion
- **Source File**: `experiment6.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.erode(image_rgb, kernel, iterations=1)` using a 5x5 rectangular kernel
- **Output**: 
  - Side-by-side comparison showing the original image and the eroded image where object boundaries are thinned.

---

## Experiment 7: Video Processing (Slow & Fast Motion)
- **Source File**: `experiment7.py`
- **Input**: `video.mp4` / Camera feed
- **Operation**: Frame playback speed manipulation via `cv2.waitKey(delay)`
- **Output**: 
  - Interactive playback window supporting normal speed (25ms), slow motion (100ms on key 's'), and fast motion (5ms on key 'f').

---

## Experiment 8: Image Dilation
- **Source File**: `experiment8.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.dilate(image_rgb, kernel, iterations=1)` using a 5x5 rectangular kernel
- **Output**: 
  - Side-by-side comparison showing the original image and the dilated image where object boundaries are expanded.

---

## Experiment 9: Image Scaling (Bigger and Smaller)
- **Source File**: `experiment9.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.resize()` with interpolation techniques
- **Output**: 
  - 3-panel figure showing the Original Image, Scaled Bigger image (1.5x scaling), and Scaled Smaller image (0.5x scaling).

---

## Experiment 10: 90-Degree Clockwise Rotation
- **Source File**: `experiment10.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)`
- **Output**: 
  - Side-by-side subplot displaying the original image and the rotated image oriented 90 degrees clockwise.
