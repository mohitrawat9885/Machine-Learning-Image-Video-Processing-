from PIL import Image
import numpy as np
from pylab import *
img=Image.open('./gra_img.jpg')
figure(0)
img.show()
print(img.width,img.height,img.mode,img.format)

pix = img.load()
print(pix[2,3])