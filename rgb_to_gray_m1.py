import cv2
image = cv2.imread('./img/4.jpg')
image = cv2.resize(image, (612, 512))
cv2.imshow('Original', image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.resize(gray_image, (612, 512))
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()