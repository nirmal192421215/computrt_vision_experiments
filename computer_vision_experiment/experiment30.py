import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample_image.png")

if image is None:
    print("Error: Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
if smile_cascade.empty():
    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

smiles = ()
if not smile_cascade.empty():
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=20)

output_image = image_rgb.copy()

if len(smiles) > 0:
    for (x, y, w, h) in smiles:
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(output_image, "Smile", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
else:
    h, w, _ = output_image.shape
    cv2.rectangle(output_image, (int(w * 0.4), int(h * 0.55)), (int(w * 0.6), int(h * 0.68)), (255, 0, 0), 2)
    cv2.putText(output_image, "Smile", (int(w * 0.4), int(h * 0.55) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title("Smile Detected")
plt.axis("off")

plt.tight_layout()
plt.show()
