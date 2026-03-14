import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
monkey = cv2.imread("monkey.jpeg")
dexter = cv2.imread("dexter.jpg")
fingGuy = cv2.imread("4fingers.jpeg")
likeMeme = cv2.imread("like.webp")
abs = cv2.imread("absolute_cinema.jpeg")


def getSize(img):
    frame = cap.read()[1]
    img_resized = cv2.resize(img, (frame.shape[1], frame.shape[0]))
    return img_resized


interactie = False
abs = getSize(abs)
likeMeme = getSize(likeMeme)
monkey = getSize(monkey)
dexter = getSize(dexter)
fingGuy = getSize(fingGuy)
mp_hands = mp.solutions.hands
# modul de recunoastere a mani
mp_draw = mp.solutions.drawing_utils
# modul responsabil de desenare
hands = mp_hands.Hands(max_num_hands=2)
# modul responsabil de creare a obiectului de tip hands
p = [0 for i in range(21)]
finger = [0 for i in range(5)]
while True:
    frame = cap.read()[1]
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks) == 2:
            interactie = True
            combined = cv2.hconcat([frame, abs])
            cv2.imshow("Video", combined)
        else:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, handLms, mp_hands.HAND_CONNECTIONS)
                for id, point in enumerate(handLms.landmark):
                    width, height, color = frame.shape
                    width, height = int(point.x * height), int(point.y * width)
                    p[id] = height
                    if p[2] > p[4] and p[2] < p[5]:
                        interactie = True
                        combined = cv2.hconcat([frame, likeMeme])
                        cv2.imshow("Video", combined)
                    elif (p[10] > p[12] and p[14] > p[16] and p[18] > p[20]
                          and len(results.multi_hand_landmarks) == 1):
                        interactie = True
                        combined = cv2.hconcat([frame, fingGuy])
                        cv2.imshow("Video", combined)
                    elif p[8] < p[6] and p[12] > p[8]:
                        interactie = True
                        combined = cv2.hconcat([frame, monkey])
                        cv2.imshow("Video", combined)
                    else:
                        interactie = False
    else:
        interactie = False
    if not interactie:
        combined = cv2.hconcat([frame, dexter])
        cv2.imshow("Video", combined)
    cv2.waitKey(2)
