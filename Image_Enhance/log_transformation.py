from PIL import Image
import numpy as np
from pylab import *
img=Image.open('../img/1.jpg')
figure(1)
img.show()
img1=img.convert('L')       
figure(2)
img1.show()
img_log=img1.point(lambda x: 255*np.log10(1+x/255))
figure(3)
img_log.show()
