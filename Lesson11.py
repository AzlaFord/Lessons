import cv2

# img = cv2.imread('apple.jpg')
# galben = (0,255,255)
# rectagle = cv2.rectangle(img,(200,200),(10,10),galben)
# cv2.imshow("poza",rectagle)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import numpy as np

# img = cv2.imread("apple.jpg")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# min, thresh = cv2.threshold(img,120, 255, cv2.THRESH_BINARY)

# lower_green = np.array([30, 90, 120])
# upper_green = np.array([210, 255, 255])
# v = hsv[lower_green, upper_green, 2]
# _, th = cv2.threshold(v, 120, 255, cv2.THRESH_TOZERO)
# th_bgr = cv2.merge([th, th, th])
# mask = cv2.inRange(hsv, lower_green, upper_green)
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# for contur in contours:
#     area = cv2.contourArea(contur)
#     if area >= 600:  
#         cv2.drawContours(img, [contur], -1, (0, 0, 255), 2)

# cv2.imshow("Mar detectat",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image_file = "text.png"
img = cv2.imread(image_file)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (70, 0, 0), 1)

cv2.imshow("Mask", thresh)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image_file = "donut.jpg"
# img = cv2.imread(image_file)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hsv_min = (2, 28, 65)
# hsv_max = (26, 238, 255)
# thresh = cv2.inRange(hsv, hsv_min, hsv_max)
# contour, hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contour, -1, (220, 0, 255), 2,cv2.LINE_8,hierarchy,10)
# print(hierarchy)
# cv2.imshow("ceva",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
