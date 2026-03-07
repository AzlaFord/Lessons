import cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
recognizer.read('model/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX
names = "me"
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print(confidence)
        if (confidence < 50):
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(confidence), (x + 5, y + h - 5),
                        font, 1, (255, 255, 0), 1)
        else:
            cv2.putText(img, str(id), (x + 5, y - 5),
                        font, 1, (255, 255, 255), 2)
    cv2.imshow('camera', img)
    cv2.waitKey(10)
