# image restoration
import numpy as np
import cv2 

from matplotlib import pyplot as plt

src = cv2.imread('../img/1.jpg')
src = cv2.resize(src, (712, 512))
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )

sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
blur = cv2.GaussianBlur(image, (3,3), 0)
Restoredimg = cv2.filter2D(blur, -1, sharpen_kernel)

cv2.imshow('orimg',image)
cv2.imshow('restoredimg.png',Restoredimg)
#cv2.imwrite('restoredimg.png',Restoredimg)
cv2.imshow('blur',blur)
cv2.waitKey(0)
