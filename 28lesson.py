import mediapipe as mp
import cv2
import numpy as np
import math
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

mpFace = mp.solutions.face_mesh
face = mpFace.FaceMesh()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
_, frame = cap.read()
height, width, _ = frame.shape

prev_x, prev_y = 0, 0
last_press = 0
cooldown = 0.3


def find_xy(index):
    c_list = str(landmarks[index]).splitlines()
    xy = [float(c_list[i].split(":")[1]) for i in range(2)]
    return xy


def float_to_coords(f_coords):
    abs_x = int(f_coords[0] * width)
    abs_y = int(f_coords[1] * height)
    return abs_x, abs_y


def pyth(x1, y1, x2, y2):
    cateta1 = x1 - x2
    cateta2 = y1 - y2
    dist = math.sqrt((cateta1 ** 2) + (cateta2 ** 2))
    return dist


def press_key(key):
    global last_press
    now = time.time()
    if now - last_press > cooldown:
        keyboard.press(key)
        keyboard.release(key)
        last_press = now


thresh_low = 0.1
thresh_high = 0.2

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face.process(frameRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame, faceLms, mpFace.FACEMESH_CONTOURS)
            landmarks = faceLms.landmark

            nose_tip = find_xy(1)
            forehead = find_xy(151)
            dst = pyth(nose_tip[0], nose_tip[1], forehead[0], forehead[1])

            if dst < thresh_low:
                print("Face UP")
                press_key(Key.up)
            elif dst < thresh_high:
                print("Neutral Position")
            else:
                print("Face DOWN")
                press_key(Key.down)

    cv2.imshow("WINDOW", frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
