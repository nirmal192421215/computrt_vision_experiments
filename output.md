# Computer Vision Experiments - Output

This document outlines the computer vision experiments implemented using Python and OpenCV, along with their input operations and output results.

---

## Experiment 1: Basic Image Reading & Grayscale Conversion
- **Source File**: `experiment1.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- **Output**: 

![Experiment 1 Output](outputs/output_exp1.png)

---

## Experiment 2: Gaussian Blurring
- **Source File**: `experiment2.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.GaussianBlur(image_rgb, (15, 15), 0)`
- **Output**: 

![Experiment 2 Output](outputs/output_exp2.png)

---

## Experiment 3: Canny Edge Detection (Outline)
- **Source File**: `experiment3.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.Canny(gray_image, 100, 200)`
- **Output**: 

![Experiment 3 Output](outputs/output_exp3.png)

---

## Experiment 4: Histogram Equalization & Comparison
- **Source File**: `experiment4.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.equalizeHist(gray_image)` and `plt.hist()`
- **Output**: 

![Experiment 4 Output](outputs/output_exp4.png)

---

## Experiment 5: Color Histogram Analysis
- **Source File**: `experiment5.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.calcHist([image], [i], None, [256], [0, 256])` for Blue, Green, and Red channels
- **Output**: 

![Experiment 5 Output](outputs/output_exp5.png)

---

## Experiment 6: Image Erosion
- **Source File**: `experiment6.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.erode(image_rgb, kernel, iterations=1)` using a 5x5 rectangular kernel
- **Output**: 

![Experiment 6 Output](outputs/output_exp6.png)

---

## Experiment 7: Video Processing (Slow & Fast Motion)
- **Source File**: `experiment7.py`
- **Input**: `video.mp4` / Camera feed
- **Operation**: Frame playback speed manipulation via `cv2.waitKey(delay)`
- **Output**: 

![Experiment 7 Output](outputs/output_exp7.png)

---

## Experiment 8: Image Dilation
- **Source File**: `experiment8.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.dilate(image_rgb, kernel, iterations=1)` using a 5x5 rectangular kernel
- **Output**: 

![Experiment 8 Output](outputs/output_exp8.png)

---

## Experiment 9: Image Scaling (Bigger and Smaller)
- **Source File**: `experiment9.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.resize()` with interpolation techniques
- **Output**: 

![Experiment 9 Output](outputs/output_exp9.png)

---

## Experiment 10: 90-Degree Clockwise Rotation
- **Source File**: `experiment10.py`
- **Input**: `sample_image.png`
- **Operation**: `cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)`
- **Output**: 

![Experiment 10 Output](outputs/output_exp10.png)
