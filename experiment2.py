import cv2
import matplotlib.pyplot as plt

image = cv2.imread("CV.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blurred_image = cv2.GaussianBlur(image_rgb, (15, 15), 0)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(blurred_image)
plt.title("Gaussian Blurred Image")
plt.axis("off")

plt.show()