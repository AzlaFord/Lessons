import telebot
import numpy as np
import cv2
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')


bot = telebot.TeleBot("8329433948:AAF0VHCTZv2IKiV1PvJFtg6FQT5UjADbCfA")
chat_id = 2039185977
cam = cv2.VideoCapture(0)
winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
prev_frame = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
current_frame = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
next_frame = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


def diffImg(f0, f1, f2):
    d1 = cv2.absdiff(f2, f1)
    d2 = cv2.absdiff(f1, f0)
    res = cv2.bitwise_and(d1, d2)
    d3 = np.ravel(res)
    d4 = np.count_nonzero(d3)
    return d4, res


while True:
    frame = cam.read()[1]
    nzero, result = diffImg(prev_frame, current_frame, next_frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face.detectMultiScale(gray)
    print(faces)
    if nzero > 160000 and not (np.sum(faces) == 0):
        _ret, frame = cam.read()
        for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('cam', frame)
        cv2.imwrite('1.png', frame)
        print("moving")
        bot.send_photo(648624553, open('1.png', 'rb'))
        bot.send_message(648624553, "Face detected")
        nzero = 0
    cv2.imshow(winName, result)
    prev_frame = current_frame
    current_frame = next_frame
    next_frame = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    key = cv2.waitKey(1)
    if key == 27:
    cv2.destroyWindow(winName)
break
