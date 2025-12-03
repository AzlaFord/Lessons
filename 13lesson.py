import cv2

def nimic(x):
    pass


img = cv2.VideoCapture(0)

cv2.namedWindow('track',cv2.WINDOW_NORMAL)
cv2.resizeWindow('track',400,400)
cv2.createTrackbar('sigma','track',1,100,nimic)

while True:
    ret,frame=img.read()
    sigma = cv2.getTrackbarPos('sigma','track')
    blur = cv2.GaussianBlur(frame,(21,21),sigma)
    canny = cv2.Canny(blur,100,200)
    cv2.imshow('track',canny)
    cv2.waitKey(1)

cv2.destroyAllWindows()



