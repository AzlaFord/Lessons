import telebot
import numpy as np
import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

bot = telebot.TeleBot("8329433948:AAF0VHCTZv2IKiV1PvJFtg6FQT5UjADbCfA")
chat_id = 2039185977

cap = cv2.VideoCapture(0)

prev = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
curret = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
next = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)


def diffImg(f0, f1, f2):
    d1 = cv2.absdiff(f2, f1)
    d2 = cv2.absdiff(f1, f0)
    res = cv2.bitwise_and(d1, d2)
    d3 = np.ravel(res)
    d4 = np.count_nonzero(d3)
    return d4, res


while True:
    frame = cap.read(0)[1]
    zcount, result = diffImg(prev, curret, next)
    faces = face.detectMultiScale(frame, 1.2, 5)

    if zcount > 140000 and not (np.sum(faces) == 0):
        frame = cap.read()[1]
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.imwrite("1.png", frame)
        bot.send_photo(chat_id, open("1.png", "rb"))
        bot.send_message(chat_id, "sa miscat ceva")
        print("moving")
        cv2.imshow("frame", frame)
        zcount = 0
    cv2.imshow("final", result)
    prev = curret
    curret = next
    next = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break
