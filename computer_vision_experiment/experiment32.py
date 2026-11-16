import numpy as np
import matplotlib.pyplot as plt

def create_corner_boxes_image(width=500, height=500):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    bw = width // 10
    bh = height // 10
    
    image[0:bh, 0:bw] = [0, 0, 0]
    image[0:bh, width - bw:width] = [0, 0, 255]
    image[height - bh:height, 0:bw] = [0, 255, 0]
    image[height - bh:height, width - bw:width] = [255, 0, 0]
    
    return image

try:
    user_input = input("Enter image width and height (e.g., 500 500): ").split()
    w, h = int(user_input[0]), int(user_input[1])
except:
    w, h = 500, 500

result = create_corner_boxes_image(w, h)

plt.imshow(result)
plt.title("White Image with 4 Corner Boxes")
plt.axis("off")
plt.show()
