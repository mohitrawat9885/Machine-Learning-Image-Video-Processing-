from skimage import io
from pylab import *

img = io.imread('./img/1.jpg')
plt.subplot(121)
io.imshow(img)
plt.title('original image')

im_c=img[0:100,0:100]
plt.subplot(122)
io.imshow(im_c)
plt.title('cropped image')