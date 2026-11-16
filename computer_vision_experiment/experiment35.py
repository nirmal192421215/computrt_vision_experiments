import cv2
import matplotlib.pyplot as plt

def put_text_on_image(image_path="sample_image.png", text="Computer Vision"):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return None
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image_rgb.shape
    position = (int(w * 0.1), int(h * 0.5))
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 2
    color = (255, 0, 0)
    thickness = 5
    cv2.putText(image_rgb, text, position, font, scale, color, thickness, cv2.LINE_AA)
    return image_rgb

try:
    user_text = input("Enter text string: ")
    if not user_text.strip():
        user_text = "Computer Vision"
except:
    user_text = "Computer Vision"

result = put_text_on_image("sample_image.png", user_text)

if result is not None:
    plt.imshow(result)
    plt.title("Text on Image")
    plt.axis("off")
    plt.show()
