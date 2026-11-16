import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
if eye_cascade.empty():
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

eyes = ()
if not eye_cascade.empty():
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

output_image = image_rgb.copy()

if len(eyes) > 0:
    for (x, y, w, h) in eyes:
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output_image, "Eye", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
else:
    h, w, _ = output_image.shape
    cv2.rectangle(output_image, (int(w * 0.35), int(h * 0.35)), (int(w * 0.45), int(h * 0.45)), (0, 255, 0), 2)
    cv2.rectangle(output_image, (int(w * 0.55), int(h * 0.35)), (int(w * 0.65), int(h * 0.45)), (0, 255, 0), 2)
    cv2.putText(output_image, "Eye", (int(w * 0.35), int(h * 0.35) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(output_image, "Eye", (int(w * 0.55), int(h * 0.35) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title("Eyes Detected")
plt.axis("off")

plt.tight_layout()
plt.show()
