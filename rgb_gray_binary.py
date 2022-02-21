import cv2
im_gray = cv2.imread('./img/2.jpg', cv2.IMREAD_GRAYSCALE)
im_gray = cv2.resize(im_gray, (600, 600))
cv2.imshow('Gray-scale', im_gray)

(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = cv2.resize(im_bw, (600, 600))
cv2.imshow('Binary', im_bw)
cv2.waitKey()