import cv2
import matplotlib.pyplot as plt

image = cv2.imread("CV.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

bigger_image = cv2.resize(image_rgb, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(image_rgb, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bigger_image)
plt.title("Scaled Bigger (1.5x)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(smaller_image)
plt.title("Scaled Smaller (0.5x)")
plt.axis("off")

plt.tight_layout()
plt.show()
