import cv2
import numpy as np

cap = cv2.VideoCapture(0)


dictionar = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
params = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionar, params)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cords, ids, _ = detector.detectMarkers(gray)
    frame = cv2.aruco.drawDetectedMarkers(frame, cords, ids)
    cv2.imshow("img", frame)
    cv2.waitKey(1)
