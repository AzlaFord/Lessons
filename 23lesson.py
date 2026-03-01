import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)
while True:
    frame = cap.read()[1]
    result = model(frame, conf=0.0)
    alnotated_frame = result[0].plot()
    cv2.imshow("ceva", frame)
    cv2.waitKey(1)
