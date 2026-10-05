import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    colors = ('b', 'g', 'r')
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
        
    plt.title("Color Histogram Analysis")
    plt.xlabel("Color Levels")
    plt.ylabel("Pixel Count")
    
    plt.tight_layout()
    plt.show()

image = cv2.imread("CV.png")

if image is None:
    print("Error: Image not found!")
    exit()

analyze_color_histogram(image)
