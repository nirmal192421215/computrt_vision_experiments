import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_rectangle_image(width=500, height=500):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    pt1 = (int(width * 0.2), int(height * 0.2))
    pt2 = (int(width * 0.8), int(height * 0.8))
    cv2.rectangle(image, pt1, pt2, (0, 0, 255), 4)
    return image

try:
    user_input = input("Enter image width and height (e.g., 500 500): ").split()
    w, h = int(user_input[0]), int(user_input[1])
except:
    w, h = 500, 500

result = draw_rectangle_image(w, h)

plt.imshow(result)
plt.title("Rectangle on White Image")
plt.axis("off")
plt.show()
