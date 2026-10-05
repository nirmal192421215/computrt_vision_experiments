import cv2

cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    cap = cv2.VideoCapture(0)

delay = 25

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("Video Player (s: Slow, f: Fast, n: Normal, q: Quit)", frame)

    key = cv2.waitKey(delay) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        delay = 100
    elif key == ord('f'):
        delay = 5
    elif key == ord('n'):
        delay = 25

cap.release()
cv2.destroyAllWindows()
