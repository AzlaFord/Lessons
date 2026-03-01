import numpy as np
from PIL import Image
import os
import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

path = "dataset/"
detector = cv2.face.LBPHFaceRecognizer_create()


def getImg(path):
    imgPaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples, ids = [], []
    for imgPath in imgPaths:
        img_numpy = np.array(Image.open(imgPath).convert('L'), "uint8")
        id = int(os.path.split(imgPath)[-1].split(".")[1])
        for x, y, h, w in face.detectMultiScale(img_numpy, 1.1, 4):
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples, ids


faces, ids = getImg(path)
detector.train(faces, np.array(ids))
detector.write("model/trainer.yml")
print("merge tot cred")
