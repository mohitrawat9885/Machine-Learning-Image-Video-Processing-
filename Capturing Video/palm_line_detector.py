import cv2
image=cv2.imread('../img/palm.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 60, 65, apertureSize=3)


cv2.imshow("palm",image)
cv2.imshow("edges", edges)
edges = cv2.bitwise_not(edges)
cv2.imshow("Black & white", edges)
cv2.waitKey(0)