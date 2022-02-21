import cv2
import numpy as np
from matplotlib import image, pyplot as plt

def displayImage (image, title):
   plt.imshow(image)
   plt.title(title)
   plt.show()

image = cv2.imread("../img/1.jpg")
displayImage(image, "Original")

P=np.ones(image.shape, dtype="uint8")*100
added = cv2.add(image, P)
displayImage(added, "increase pixel intensity by 100")

P=np.ones(image.shape, dtype="uint8")*100
subtracted=cv2.subtract(image, P)
displayImage(subtracted, "reduced pixel intensity by 100")