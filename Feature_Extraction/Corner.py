import cv2
import numpy as np

img=cv2.imread("../img/obj2.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[255,0,0]
cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
