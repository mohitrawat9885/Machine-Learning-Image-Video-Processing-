import cv2
import numpy
from matplotlib import pyplot as plt

image = cv2.imread('./img/leo.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('RGB Color Image')
plt.show()

print(image.shape)
print('image width: %d' % image.shape[0])
print('image height: %d' % image.shape[1])
print('image columns: %d' % image.shape[2])
