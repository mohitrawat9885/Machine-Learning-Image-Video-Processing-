import cv2
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt 
src = cv2.imread("D:/Programing/Python/ECE356/img/multi_object.jpg")
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )   
ret, thresh = cv2.threshold(image, 0, 255, 
                            cv2.THRESH_BINARY_INV +
                            cv2.THRESH_OTSU) 
plt.figure(figsize=(15,8))
plt.subplot(231)
plt.title('Mohit Original Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(src) # First image
plt.subplot(232)
plt.title('Mohit Gray Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(image)# second image
plt.subplot(233)
plt.title('Mohit Segmented Image')
plt.xlabel([1,1,9,0])
plt.ylabel([4,4,6,3])
plt.imshow(thresh)# third image
plt.show()
