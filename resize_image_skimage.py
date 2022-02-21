from skimage import io 
from pylab import *
from skimage.transform import resize 

img =io.imread('./img/1.jpg') 
io.imsave('abc.jpg',img)
img_res = resize(img, (10,10))
figure(0)
io.imshow(img_res) 
io.imsave('md.jpg',img_res)

img_res1 = resize(img, (600,600))
figure(1)
io.imshow(img_res1) 
io.imsave('ss.jpg', img_res1)

img_res2 = resize(img, (1000,1000))
figure(2)
io.imshow(img_res2) 
io.imsave('rj.jpg', img_res2)
img.shape
