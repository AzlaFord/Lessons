import cv2

cap = cv2.VideoCapture(0)

def noth(x):
    pass

size = 15
valT = 0

cv2.namedWindow("win")
cv2.resizeWindow("win",400,200)
cv2.createTrackbar("tr1","win",0,2,noth)
cv2.createTrackbar("tr2","win",15,100,noth)

while True:
    val1 = cv2.getTrackbarPos("tr1","win")
    size =cv2.getTrackbarPos("tr2","win")
    if val1 == 0:
        valT = cv2.MORPH_ELLIPSE
    elif val1 == 1:
        valT = cv2.MORPH_CROSS
    elif val1 == 2:
        valT = cv2.MORPH_RECT
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,200)
    kernel = cv2.getStructuringElement(valT,(size,size))
    closed = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("win",closed)
    cv2.waitKey(1)
cv2.destroyAllWindows()
