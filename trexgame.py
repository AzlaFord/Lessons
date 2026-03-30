import mss
import numpy as np
import cv2
import pyautogui

jumped = False  # Flag to track if we already jumped

with mss.mss() as sct:
    monitor = sct.monitors[1]
    while True:
        screen = sct.grab(monitor)
        img = np.array(screen)
        img = img[:, :, :3]
        roi = img[300:500, 500:800]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

        non_zeros = cv2.countNonZero(thresh)
        ceva = 300  # Tune this value — number of non-zero pixels that signals an obstacle

        if non_zeros > ceva and not jumped:
            pyautogui.press("up")
            jumped = True  # Lock further presses
        elif non_zeros <= ceva:
            jumped = False  # Reset once obstacle is gone

        cv2.imshow("screen", roi)
        cv2.waitKey(1)
