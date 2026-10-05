import cv2
import matplotlib.pyplot as plt

image = cv2.imread("CV.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated_image = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("90 Degree Clockwise Rotated")
plt.axis("off")

plt.tight_layout()
plt.show()
