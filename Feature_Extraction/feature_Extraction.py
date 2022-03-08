import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread, imshow
from skimage import io

image1 = io.imread("../img/1.jpg")
plt.subplot(121)
imshow(image1);
image2 = io.imread("../img/1.jpg",as_gray=True)
plt.subplot(122)
imshow(image2);

print(image1.shape)
print(image1.size)
print(image2.shape)
print(image2.size)


