import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_circle_image(width=500, height=500):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (int(width / 2), int(height / 2))
    radius = int(min(width, height) * 0.3)
    cv2.circle(image, center, radius, (255, 0, 0), 4)
    return image

try:
    user_input = input("Enter image width and height (e.g., 500 500): ").split()
    w, h = int(user_input[0]), int(user_input[1])
except:
    w, h = 500, 500

result = draw_circle_image(w, h)

plt.imshow(result)
plt.title("Circle on White Image")
plt.axis("off")
plt.show()
