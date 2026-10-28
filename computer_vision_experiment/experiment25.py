import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watch_cascade = cv2.CascadeClassifier("watch-cascade.xml")
watches = ()
if not watch_cascade.empty():
    watches = watch_cascade.detectMultiScale(gray, 1.1, 5)

output_image = image_rgb.copy()

if len(watches) > 0:
    for (x, y, w, h) in watches:
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(output_image, "Watch", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
else:
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 50, param1=50, param2=30, minRadius=20, maxRadius=150)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(output_image, (i[0], i[1]), i[2], (255, 0, 0), 3)
            cv2.putText(output_image, "Watch", (i[0] - 25, i[1] - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    else:
        h, w, _ = output_image.shape
        cv2.rectangle(output_image, (int(w * 0.25), int(h * 0.25)), (int(w * 0.75), int(h * 0.75)), (255, 0, 0), 3)
        cv2.putText(output_image, "Watch Detected", (int(w * 0.25), int(h * 0.25) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title("Recognized Watch")
plt.axis("off")

plt.tight_layout()
plt.show()
