import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread("../img/obj.jpg")

noise_img = random_noise(img, mode='s&p',amount=0.4)
gnoise_img = np.array(255*noise_img, dtype = 'uint8')


cv2.imshow('blur',noise_img)
cv2.waitKey(0)
