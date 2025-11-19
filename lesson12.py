import cv2
image_file = "shapes.png"
img = cv2.imread(image_file)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray,115,255,cv2.THRESH_BINARY)
contour,hierarcy = cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.imshow("salut",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
