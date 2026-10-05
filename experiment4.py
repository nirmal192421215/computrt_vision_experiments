import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.hist(gray_image.ravel(), 256, range=[0, 256])
plt.title("Original Histogram")

plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, range=[0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()
