import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))

while True:
    rat,frame = cap.read()
    out.write(frame)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()























