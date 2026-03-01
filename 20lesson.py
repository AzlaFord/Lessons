import cv2
from datetime import datetime as dt
import serial

uno = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.2, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        center_x = int(x+w/2)
        center_y = int(y+h/2)
        cv2.circle(frame, (center_x, center_y), 3, (255, 0, 0), 3)
    cv2.imshow("eu", frame)
    cv2.waitKey(1)
