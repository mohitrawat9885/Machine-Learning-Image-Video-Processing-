from skimage import io
from skimage import color
from pylab import *

img = io.imread('./img/2.jpg')
io.imsave("new_image.jpg", img)