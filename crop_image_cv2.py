import cv2
import numpy
from matplotlib import pyplot as plt

image=cv2.imread("./img/leo.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

w=image.shape[0]
h=image.shape[1]
(cx,cy)=(w//2,h//2)
print(cx)
print(cy)


top_right=image[0:cy,cx:w]
top_left=image[0:cy,0:cx]
bottom_left=image[cy:h,0:cx]
bottom_right=image[cy:h,cx:w]


plt.figure(figsize=(15,8))

plt.subplot(221)
plt.title('Mohit Top left')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(top_left);

plt.subplot(222)
plt.title('Mohit Top Right')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(top_right);

plt.subplot(223)
plt.title('Mohit Bottom left')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(bottom_left);

plt.subplot(224)
plt.title('Mohit Bottom Right')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(bottom_right);

plt.show()