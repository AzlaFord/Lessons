import cv2
import mediapipe as mp
import numpy as np
import math

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
frame_init = camera.read()[1]
height, width, channels = frame_init.shape
mask = np.ones((height, width), dtype="uint8")

tool = "Pen"
paintText = ""
circle = False
paint = False
prevx = 0
prevy = 0
thick = 4
dist = 0.00
size_mode = False


def find_xy(index):
    coordinates = str(landmarks[index]).splitlines()
    xy = [float(coordinates[i].split(":")[1]) for i in range(2)]
    return xy


def float_to_coord(coords):
    scaled_x = int(coords[0] * width)
    scaled_y = int(coords[1] * height)
    return scaled_x, scaled_y


def length(index_a, index_b):
    sx = abs(find_xy(index_a)[0] - find_xy(index_b)[0])
    sy = abs(find_xy(index_a)[1] - find_xy(index_b)[1])
    c = math.sqrt(sx**2 + sy**2)
    c = round(c, 2)
    return c


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
            middle_tip = float_to_coord(middle_tip_float)
            middle_pip_float = find_xy(10)

            ring_tip_float = find_xy(16)
            ring_tip = float_to_coord(ring_tip_float)
            ring_pip_float = find_xy(14)

            little_tip_float = find_xy(20)
            little_tip = float_to_coord(little_tip_float)
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

            if length(4, 8) < 0.06 and middle_up:
                size_mode = True
            if size_mode:
                dist = length(4, 8)
                paint = False
                if not middle_up:
                    size_mode = False

            if index_up and middle_up and ring_up and little_up and tool != "Circle":
                tool = "Eraser"
                paint = False
            elif index_up and middle_up and ring_up and tool != "Circle":
                tool = "Pen"
                paint = False
            elif index_up and middle_up and not size_mode:
                paint = True
            else:
                paint = False

            x, y = index_tip[:2]

            old = 0.28 - 0.01
            new = 7
            thick = int(((dist - 0.01) * 12 / old) + 2)

            if paint and tool == "Pen":
                paintText = "ON"
                cv2.line(mask, (prevx, prevy), (x, y), 0, thick)
                prevx, prevy = x, y
            elif paint and tool == "Eraser":
                paintText = "ON"
                cv2.line(mask, (prevx, prevy), (x, y), 255, thick)
                prevx, prevy = x, y
            else:
                paintText = "OFF"
                prevx, prevy = x, y

            if cv2.waitKey(1) == ord("c"):
                tool = "Circle"

            if tool == "Circle" and paint:
                init_x, init_y = x, y
                circle = True
                tool = "Center"

            if circle:
                if not paint:
                    last_x, last_y = x, y
                    cv2.circle(mask, (init_x, init_y), int(
                        math.sqrt(abs(init_x - last_x) ** 2 + abs(init_y - last_y) ** 2)), 0, thick)
                    tool = "Eraser"
                    circle = False

    cv2.putText(frame, "Tool: " + tool, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.putText(frame, "Draw: " + str(paint), (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.putText(frame, "Size: " + str(thick), (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    op = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Video", op)

    if cv2.waitKey(1) == ord("q"):
        mask = np.ones((height, width), dtype="uint8")

    if cv2.waitKey(1) == 27:
        break
