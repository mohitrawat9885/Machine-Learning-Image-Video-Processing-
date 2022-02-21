import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread('../img/parrot.jpg')
plt.imshow(img)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')


sobel_y = np.array([[ -1, -2, -1], 
                           [ 0, 0, 0], 
                          [ 1, 2, 1]])
sobel_x = np.array([[-1, 0, 1],
                        [-2,0,2],
                        [-1, 0, 1]])
filtered_image = cv2.filter2D(gray, -1, sobel_y)  
plt.imshow(filtered_image, cmap='gray')
plt.show()

filtered_image = cv2.filter2D(gray, -1, sobel_x)
plt.imshow(filtered_image, cmap='gray')

plt.show()
