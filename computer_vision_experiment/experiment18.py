import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, c = image_rgb.shape

roi = image_rgb[int(h * 0.2):int(h * 0.6), int(w * 0.2):int(w * 0.6)].copy()

pasted_image = image_rgb.copy()
rh, rw, _ = roi.shape
pasted_image[0:rh, 0:rw] = roi

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(roi)
plt.title("Cropped ROI")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(pasted_image)
plt.title("ROI Pasted")
plt.axis("off")

plt.tight_layout()
plt.show()
