from PIL import Image
import numpy as np
from pylab import *

img=Image.open('./img/1.jpg')
figure(0)
img.show()

img1=img.convert('L')
figure(1)
img1.show()