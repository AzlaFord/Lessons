import cv2

def noth(x):
    pass


img = cv2.imread('python.png')

cv2.namedWindow('ceva',cv2.WINDOW_NORMAL)
cv2.resizeWindow("ceva",400,400)
cv2.createTrackbar('sigma','ceva',1,100,noth)

while True:
    sigma = cv2.getTrackbarPos('sigma','ceva')
    blur = cv2.GaussianBlur(img,(21,21),sigma)
    canny = cv2.Canny(blur,100,200)
    cv2.imshow('ceva',canny)
    cv2.waitKey(1)

cv2.destroyAllWindows(1)
