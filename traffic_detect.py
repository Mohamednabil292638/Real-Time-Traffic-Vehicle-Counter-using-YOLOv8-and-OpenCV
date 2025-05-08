import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or use 'yolov8s.pt' for better accuracy
cap = cv2.VideoCapture("Highway_traffic.mp4")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("Traffic Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
