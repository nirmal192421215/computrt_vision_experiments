import cv2

cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    cap = cv2.VideoCapture(0)

car_cascade = cv2.CascadeClassifier("cars.xml")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = ()
    if not car_cascade.empty():
        cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    if len(cars) > 0:
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        h, w, _ = frame.shape
        cv2.rectangle(frame, (int(w * 0.2), int(h * 0.4)), (int(w * 0.8), int(h * 0.8)), (0, 255, 0), 2)
        cv2.putText(frame, "Vehicle", (int(w * 0.2), int(h * 0.4) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
