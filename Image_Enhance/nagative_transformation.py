from PIL import Image
import numpy as np
from pylab import *
img=Image.open('../img/1.jpg')
figure(1)
img.show()
img1=img.convert('L')       # RGB to Gray-scale conversion
figure(2)
img1.show()
img_neg=img1.point(lambda x:255-x)    # Negative Transformation
img_neg.show()

