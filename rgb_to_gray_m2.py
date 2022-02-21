import cv2
img = cv2.imread('./img/2.jpg', 1)
img = cv2.resize(img, (800, 600))
cv2.imshow('Grayscale', img)
cv2.waitKey()