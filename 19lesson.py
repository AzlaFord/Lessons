import cv2
import serial
import numpy as np
low_green = (35, 80, 50)
high_green = (85, 255, 255)

low_blue = (90, 80, 50)
high_blue = (130, 255, 255)

low_red1 = (0, 80, 50)
high_red1 = (10, 255, 255)
low_red2 = (170, 80, 50)
high_red2 = (179, 255, 255)

comPort = "/dev/ttyUSB0"
baudrate = 9600
uno = serial.Serial(comPort, baudrate)

cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green = cv2.inRange(hsv, low_green, high_green)
    blue = cv2.inRange(hsv, low_blue, high_blue)
    red = cv2.inRange(hsv, low_red1, high_red1) | cv2.inRange(
        hsv, low_red2, high_red2)
    color_green = np.count_nonzero(green)
    color_red = np.count_nonzero(red)
    color_blue = np.count_nonzero(blue)
    if color_red > 1000:
        uno.write(b'1')
    elif color_green > 1000:
        uno.write(b'2')
    elif color_blue > 1000:
        uno.write(b'3')
    cv2.imshow('frame', frame)
    cv2.imshow("blue", blue)
    cv2.imshow('green', green)
    cv2.imshow("red", red)
    cv2.waitKey(1)
