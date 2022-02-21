from skimage import io
from skimage import color
from skimage import data
from pylab import *
from matplotlib import pyplot as plt

img = io.imread("../img/aarav.jpg")
figure(0)

io.imshow(img)
plt.title('Original Image')

img_hsv = color.rgb2hsv(img)

img_rgb = color.hsv2rgb(img_hsv)

figure(1)

io.imshow(img_hsv)

plt.title("HSV Image")

figure(2)
io.imshow(img_rgb)
plt.title('RGB Image')

plt.show()