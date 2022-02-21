from __future__ import print_function
from builtins import input
from skimage.io import imread, imshow
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

image=cv2.imread("../img/5.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
new_image = np.zeros(image.shape, image.dtype)
alpha = 1.0 # Simple contrast control
beta = 0    # Simple brightness control

print(' Basic Linear Transforms ')
print('-------------------------')
try:
   alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
   beta = int(input('* Enter the beta value [0-100]: '))
except ValueError:
   print('Error, not a number')



for y in range(image.shape[0]):
   for x in range(image.shape[1]):
      for c in range(image.shape[2]):
         new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)



plt.subplot(211),imshow(image)
plt.title('Original Image')
plt.subplot(212),imshow(new_image)
plt.title('new Image')
plt.show()
