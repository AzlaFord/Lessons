import cv2
import serial
import time

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=0.1)
time.sleep(2)

cap = cv2.VideoCapture(0)

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        x, y, w, h = max(faces, key=lambda f: f[2]*f[3])
        cx = x + w // 2
        cy = y + h // 2

        ser.write(f"{cx},{cy}\n".encode())

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    cv2.imshow("Face tracking", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
ser.close()
cv2.destroyAllWindows()
