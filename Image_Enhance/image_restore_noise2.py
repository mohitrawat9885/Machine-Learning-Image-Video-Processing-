import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage import io

original_img = io.imread("../img/parrot.jpg", 1)


original = img_as_float(original_img)

sigma = 0.155
noisy = random_noise(original, var=sigma**2)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 11),
                       sharex=True, sharey=True)

plt.gray()

sigma_est = estimate_sigma(noisy, average_sigmas=True)

ax[0].imshow(noisy)
ax[0].set_title('Mohit Noise Image')
ax[0].set_xlabel([1,1,9,0])
ax[0].set_ylabel([4,4,6,3])

ax[1].imshow(denoise_tv_chambolle(noisy, weight=0.1))
ax[1].set_title('Mohit Restored Image')
ax[1].set_xlabel([1,1,9,0])
ax[1].set_ylabel([4,4,6,3])

fig.tight_layout()

plt.show()