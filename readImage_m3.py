from skimage import io
from matplotlib import image, pyplot as plt

imgage = io.imread('./img/leo.jpg')
io.imshow(image)

print(image.shape)
print("image width : %d" % image.shape [0])
print("image height : %d" % image.shape [1])
print("image columns : %d" % image.shape [2])

plt.imshow(image)
plt.title('RGB Color Image')
plt.show()