import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math

cap = cv2.VideoCapture(0)
mpFace = mp.solutions.face_mesh
face = mpFace.FaceMesh()
mpDraw = mp.solutions.drawing_utils

frame_init = cap.read()[1]
height, width, channels = frame_init.shape

thresh_low = 0.1
thresh_high = 0.2


def find_xy(index):
    coordinates = str(landmarks[index]).splitlines()
    xy = [float(coordinates[i].split(":")[1]) for i in range(2)]
    scaled_x = int(xy[0] * width)
    scaled_y = int(xy[1] * height)
    return [scaled_x, scaled_y]


def length(index_a, index_b):
    sx = abs(find_xy(index_a)[0] - find_xy(index_b)[0])
    sy = abs(find_xy(index_a)[1] - find_xy(index_b)[1])
    c = math.sqrt(sx * sx + sy * sy)
    c = round(c, 2)
    return c


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLandmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame, faceLandmarks,
                                  mpFace.FACEMESH_CONTOURS)
            landmarks = faceLandmarks.landmark
            xynouse = find_xy(1)
            scaled_xy = find_xy(151)
            dst = length(xynouse, scaled_xy)
            if dst < thresh_low:
                print("Face up")
                pyautogui.keyDown("up")
            elif dst < thresh_high:
                print("Neutral")
            else:
                print("Face down")
                pyautogui.keyDown("down")

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == 27:
        break
