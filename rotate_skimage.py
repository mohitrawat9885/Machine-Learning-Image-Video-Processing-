from skimage import io 
from pylab import *
from skimage.transform import rotate

img = io.imread('./img/1.jpg') 
plt.subplot(121)
io.imshow(img)
plt.title('original image') 

img_rot = rotate(img, -45)
plt.subplot(122)
io.imshow(img_rot)
plt.title('Rotated image')