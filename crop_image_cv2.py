import cv2
import numpy
from matplotlib import pyplot as plt

def displayImage (image,title):
    plt.imshow(image)
    plt.title(title)
    plt.show()

image=cv2.imread("./img/4.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
displayImage(image, "original")

w=image.shape[0]
h=image.shape[1]
(cx,cy)=(w//2,h//2)
print(cx)
print(cy)


top_right=image[0:cy,cx:w]
top_left=image[0:cy,0:cx]
bottom_left=image[cy:h,0:cx]
bottom_right=image[cy:h,cx:w]
displayImage(top_left, "top_left")
displayImage(top_right, "top_right")
displayImage(bottom_left, "bottom_left")
displayImage(bottom_right, "bottom_right")
