import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
kernel = np.ones((9, 9), np.uint8)

tophat_image = cv2.morphologyEx(image_rgb, cv2.MORPH_TOPHAT, kernel)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(tophat_image)
plt.title("Top Hat")
plt.axis("off")

plt.tight_layout()
plt.show()
