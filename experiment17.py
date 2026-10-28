import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
overlay = image_rgb.copy()

h, w, c = image_rgb.shape
cv2.putText(overlay, "WATERMARK", (int(w * 0.1), int(h * 0.5)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 8, cv2.LINE_AA)

watermarked_image = cv2.addWeighted(overlay, 0.4, image_rgb, 0.6, 0)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(watermarked_image)
plt.title("Watermarked Image")
plt.axis("off")

plt.tight_layout()
plt.show()
