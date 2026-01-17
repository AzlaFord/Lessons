import cv2

cap = cv2.VideoCapture(0)
bg = cv2.imread("space.png")
while True:
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    bg = cv2.resize(bg, (frame.shape[1], frame.shape[0]))
    mask = cv2.inRange(hsv, (48, 121, 64), (84, 255, 255))
    green_color = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    result = cv2.bitwise_and(bg, bg, mask=mask)
    final = green_color + result
    cv2.imshow("frame ceva", final)
    cv2.waitKey(1)
cv2.destroyAllWindows()
