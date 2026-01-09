import cv2

eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

while True:
    frame = cap.read()[1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.35, 4, 0, (30, 30))
    eyes = eye.detectMultiScale(gray, 1.2, 10, 0, (10, 10))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)
    for (x, y, w, h) in eyes:
        radius = int(round((w+h)*0.25))
        center = ((2*x+w)//2, ((2*y+h)//2))
        cv2.circle(frame, center, radius, (255, 0, 0), 2)

    cv2.imshow("frame", frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
