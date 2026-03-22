import cv2
import mediapipe as mp
import numpy as np

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

frame_init = camera.read()[1]
height, width, channels = frame_init.shape
thick = 4

mask = np.ones((height, width), dtype="uint8")
prevx = 0
prevy = 0


def find_xy(index):
    coordinates = str(landmarks[index]).splitlines()
    xy = [float(coordinates[i].split(":")[1]) for i in range(2)]
    return xy


def float_to_coord(coords):
    scaled_x = int(coords[0] * width)
    scaled_y = int(coords[1] * height)
    return scaled_x, scaled_y


while True:
    frame = camera.read()[1]
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLandmarks,
                                  mpHands.HAND_CONNECTIONS)
            landmarks = handLandmarks.landmark

            index_tip_float = find_xy(8)
            index_tip = float_to_coord(index_tip_float)
            index_pip_float = find_xy(6)

            middle_tip_float = find_xy(12)
            middle_pip_float = find_xy(10)

            ring_tip_float = find_xy(16)
            ring_pip_float = find_xy(14)

            little_tip_float = find_xy(20)
            little_pip_float = find_xy(18)

            thumb_tip_float = find_xy(4)
            thumb_tip = float_to_coord(thumb_tip_float)

            if index_tip_float[1] < index_pip_float[1]:
                index_up = True
                cv2.circle(
                    frame, (index_tip[0], index_tip[1]), thick, (255, 0, 255), 2)
            else:
                index_up = False

            if middle_tip_float[1] < middle_pip_float[1]:
                middle_up = True
            else:
                middle_up = False

            if ring_tip_float[1] < ring_pip_float[1]:
                ring_up = True
            else:
                ring_up = False

            if little_tip_float[1] < little_pip_float[1]:
                little_up = True
            else:
                little_up = False

            x, y = index_tip
            cv2.line(mask, (prevx, prevy), (x, y), 0, thick)
            prevx, prevy = x, y

    final = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Video", final)

    if cv2.waitKey(1) == 27:
        break
