import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray_image)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

corner_image = image_rgb.copy()
corner_image[dst > 0.01 * dst.max()] = [255, 0, 0]

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(corner_image)
plt.title("Harris Corners Detected")
plt.axis("off")

plt.tight_layout()
plt.show()
