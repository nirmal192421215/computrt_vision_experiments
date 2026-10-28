import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.uint8)

opening_image = cv2.morphologyEx(image_rgb, cv2.MORPH_OPEN, kernel)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(opening_image)
plt.title("Opening")
plt.axis("off")

plt.tight_layout()
plt.show()
