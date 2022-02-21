import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("../img/4.jpg", 0)
img = cv2.resize(img, (600, 600))
# cv2.imshow("Image", img)
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.hist(img.ravel(), 256, [0, 256]);
# plt.show()

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()