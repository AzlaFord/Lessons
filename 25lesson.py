import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2)
imgFin = cv2.imread("4fingers.jpeg")
# Fingertip landmark IDs
FINGER_TIPS = [8, 12, 16, 20]   # Index, Middle, Ring, Pinky
THUMB_TIP = 4
dexter = cv2.imread("dexter.jpg")


def count_fingers(landmarks, handedness):
    count = 0
    lm = landmarks.landmark

    if handedness == "Right":
        if lm[THUMB_TIP].x < lm[THUMB_TIP - 1].x:
            count += 1
    else:
        if lm[THUMB_TIP].x > lm[THUMB_TIP - 1].x:
            count += 1

    # Other 4 fingers: tip higher (lower y) than the knuckle 2 below it
    for tip in FINGER_TIPS:
        if lm[tip].y < lm[tip - 2].y:
            count += 1

    return count


while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror for natural feel
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    h, w, _ = frame.shape
    total_fingers = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for handLms, handInfo in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            handedness = handInfo.classification[0].label  # "Left" or "Right"
            finger_count = count_fingers(handLms, handedness)
            total_fingers += finger_count

            # Get wrist position to place label near each hand
            wrist = handLms.landmark[0]
            h, w, _ = frame.shape
            wx, wy = int(wrist.x * w), int(wrist.y * h)
            cv2.putText(frame, f'{handedness}: {finger_count}',
                        (wx - 40, wy + 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Display total finger count top-left
    cv2.putText(frame, f'Total Fingers: {total_fingers}',
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1.2, (0, 255, 0), 3)
    if total_fingers == 4:
        # Resize imgFin to match frame height, keeping aspect ratio
        img_h, img_w, _ = imgFin.shape
        new_w = int(img_w * (h / img_h))           # Scale width proportionally
        imgFin_resized = cv2.resize(imgFin, (new_w, h))  # Match frame height

        combined = cv2.hconcat([frame, imgFin_resized])
        cv2.imshow("Finger Counter", combined)
    else:
        img_h, img_w, _ = dexter.shape
        new_w = int(img_w * (h / img_h))           # Scale width proportionally
        dexter_resized = cv2.resize(dexter, (new_w, h))  # Match frame height
        combined = cv2.hconcat([frame, dexter_resized])
        cv2.imshow("Finger Counter", combined)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
