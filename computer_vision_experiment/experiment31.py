import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 127
_, thresh_binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
_, thresh_binary_inv = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)
_, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(thresh_binary, cmap="gray")
plt.title("Binary Threshold (127)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(thresh_binary_inv, cmap="gray")
plt.title("Inverse Binary Threshold")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(thresh_otsu, cmap="gray")
plt.title("Otsu Thresholding")
plt.axis("off")

plt.tight_layout()
plt.show()
