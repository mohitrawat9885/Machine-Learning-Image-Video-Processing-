from skimage.io import imread, imshow

import matplotlib.pyplot as plt

image_gray = imread("./img/2.jpg", as_gray=True)

imshow(image_gray)