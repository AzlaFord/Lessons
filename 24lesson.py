import cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('model/trainer.yml')
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
target_id = 1
target_name = "Me"
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id_pred, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if id_pred == target_id and confidence < 50:
            cv2.putText(img, target_name, (x+5, y-5),
                        font, 1, (255, 255, 255), 2)
        else:
            cv2.putText(img, "Unknown", (x+5, y-5),
                        font, 1, (255, 255, 255), 2)

    cv2.imshow('camera', img)
    if cv2.waitKey(10) & 0xFF == 27:  # Esc pentru exit
        break
