import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage import io

original_img = io.imread("../img/parrot.jpg", 1)

original_image = img_as_float(original_img)

sigma = 0.155
noise_image = random_noise(original_img, var=sigma**2)
restored_img  = estimate_sigma(noise_image, average_sigmas=True)


# plt.figure(figsize=(15,8))
plt.subplot(231)
plt.title('Mohit Original Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(original_img) # First image
plt.subplot(232)
plt.title('Mohit Noise Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(noise_image)# second image
plt.subplot(233)
plt.title('Mohit Restored Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(restored_img)# third image
plt.show()