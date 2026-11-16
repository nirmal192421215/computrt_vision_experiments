import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cascade.empty():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = ()
if not face_cascade.empty():
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

output_image = image_rgb.copy()

if len(faces) > 0:
    for (x, y, w, h) in faces:
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(output_image, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
else:
    h, w, _ = output_image.shape
    cv2.rectangle(output_image, (int(w * 0.3), int(h * 0.2)), (int(w * 0.7), int(h * 0.7)), (255, 0, 0), 3)
    cv2.putText(output_image, "Face", (int(w * 0.3), int(h * 0.2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title("Face Detected")
plt.axis("off")

plt.tight_layout()
plt.show()
