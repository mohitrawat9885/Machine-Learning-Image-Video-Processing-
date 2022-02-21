import cv2
import numpy
from matplotlib import pyplot as plt

def displayImage (image,title):
   plt.imshow(image)
   plt.title(title)
   plt.show()


image=cv2.imread("./img/aarav.jpg")


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
displayImage(image, "original")
flippedImage=cv2.flip(image,1)
displayImage(flippedImage, "flipped horizontally")
flippedImage=cv2.flip(image,0)
displayImage(flippedImage, "flipped vertically")
flippedImage=cv2.flip(image,-1)
displayImage(flippedImage, "flipped horizontally")
