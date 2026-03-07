import cv2
from ultralytics import YOLO
model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]

    results = model(frame, conf=0.8)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Inference", annotated_frame)
    cv2.waitKey(1)
