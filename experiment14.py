import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rows, cols, ch = image_rgb.shape

pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
pts2 = np.float32([[0, 0], [cols, 0], [100, rows], [cols - 100, rows]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_image = cv2.warpPerspective(image_rgb, matrix, (cols, rows))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(perspective_image)
plt.title("Perspective Transformed")
plt.axis("off")

plt.tight_layout()
plt.show()
