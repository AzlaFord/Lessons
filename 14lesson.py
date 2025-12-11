import cv2


def noth(x):
    pass

cap = cv2.VideoCapture(0)
size = 15
valueL =0
cv2.namedWindow("win")
cv2.resizeWindow("win",600,400)
cv2.createTrackbar("tr1","win",0,2,noth)
cv2.createTrackbar("tr2","win",15,100,noth)


while True:
    _,frame = cap.read()
    val1 = cv2.getTrackbarPos('tr1',"win")
    size = cv2.getTrackbarPos("tr2","win")

    if val1 == 0:
        valueL = cv2.MORPH_RECT
    elif val1 == 1:
        valueL = cv2.MORPH_CROSS
    elif val1 == 2:
        valueL = cv2.MORPH_ELLIPSE

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
    blur = cv2.GaussianBlur(frame,(5,5),0)
    canny = cv2.Canny(blur,30,100)
    kernel = cv2.getStructuringElement(valueL,(size,size))
    closed = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("freastra",closed)
    cv2.waitKey(1)
cv2.destroyAllWindows()
