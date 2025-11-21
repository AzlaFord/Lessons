import cv2

img = cv2.imread("shapes.png")
font = cv2.FONT_HERSHEY_COMPLEX
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
contour, _  = cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contour:
    errore = 0.01 *  cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,errore,True)
    x = approx.ravel()[0]
    y = approx.ravel()[1] -10
    
    cv2.drawContours(img,[approx],0,(0,0,0),3)
    
    if len(approx) == 3:
       cv2.putText(img, "Triangle", (x, y), font, 1, (0,0,0))
    elif len(approx) == 4:
       cv2.putText(img, "Rectangle", (x, y), font, 1,(0,0,0))
    elif len(approx) == 5:
       cv2.putText(img, "Pentagon", (x, y), font, 1, (0,0,0))
    elif 6 < len(approx) < 15:
       cv2.putText(img, "Ellipse", (x, y), font, 1, (0,0,0))
    else:
       cv2.putText(img,"Circle",(x, y), font,1, (0,0,0))        
    
cv2.imshow('contour',img)
cv2.waitKey(0)
