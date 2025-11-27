import cv2

def noth(x):
    pass

img = cv2.imread("pacman.png")
cv2.namedWindow("track",cv2.WINDOW_NORMAL)
cv2.resizeWindow("track",400,400)
cv2.createTrackbar("sigma","track",1,100,noth)

while True:
    sigma = cv2.getTrackbarPos('sigma','track')
    blur = cv2.GaussianBlur(img,(9,9),sigma)
    canny = cv2.Canny(blur,10,200)
    cv2.imshow("track",canny)
    cv2.waitKey(1)

cv2.destroyAllWindows(0)
