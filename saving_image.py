import cv2
img = cv2.imread('./img/3.jpg',0)
cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.imwrite("this_is_new_saved_image.jpg", img)