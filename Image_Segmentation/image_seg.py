import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
src = cv2.imread("../img/1.jpg")
src = cv2.resize(src, (900, 600))
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )   
ret, thresh = cv2.threshold(image, 0, 255, 
                            cv2.THRESH_BINARY_INV +
                            cv2.THRESH_OTSU) 
cv2.imshow('Segmented image', thresh) 
cv2.imshow('Original image', src)
cv2.waitKey(0)
