# import cv2 library
import cv2
import matplotlib.pyplot as plt
from skimage import exposure
from skimage.io import imread, imshow

# read the images
img1 = cv2.imread("../img/leo.jpg")
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)



plt.subplot(131), imshow(img1)
plt.title('Original Image')

# vertically concatenates images
# of same width
im_v = cv2.vconcat([img1, img1])
plt.subplot(132), imshow(im_v)
plt.title('Vertically Concatenated Image')

im_h = cv2.hconcat([img1, img1])
plt.subplot(133), imshow(im_h)
plt.title('Horizontally Concatenated Image')


plt.show()