from PIL import Image, ImageFilter 
import numpy as np
from pylab import *

image = Image.open("../img/obj.jpg")
image.show()
figure(0)
img = image.convert("L")
img.show()
figure(1)
final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, 
                                          -1, -1, -1, -1), 1, 0)) 
  
final.save("4.jpeg")
final.show()
figure(2)
