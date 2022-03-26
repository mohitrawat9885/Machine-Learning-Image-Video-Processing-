import cv2
import numpy as np

img = cv2.imread("../img/Color2.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range=np.array([25,50,70]) # green
upper_range=np.array([102,255,255])
mask = cv2.inRange(hsv, lower_range, upper_range)
cv2.imshow('Original Image',img)
cv2.imshow('Mask Image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()