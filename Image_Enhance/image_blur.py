import cv2
import numpy
from matplotlib import pyplot as plt
image=cv2.imread('../img/1.jpg')
img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
plt.subplot(231),plt.imshow(img)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.subplot(232),plt.imshow(gray,cmap='gray')

image_MedianBlur=cv2.medianBlur(gray,7)
plt.subplot(233),plt.imshow(image_MedianBlur,cmap='gray')

image_MedianBlur=cv2.medianBlur(gray,11)
plt.subplot(234),plt.imshow(image_MedianBlur,cmap='gray')

image_MedianBlur=cv2.medianBlur(gray,13)
plt.subplot(235),plt.imshow(image_MedianBlur,cmap='gray')

image_MedianBlur=cv2.medianBlur(gray,17)
plt.subplot(236),plt.imshow(image_MedianBlur,cmap='gray')

plt.show()