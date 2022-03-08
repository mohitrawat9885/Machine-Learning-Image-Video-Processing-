import cv2
kernelSize = 15

parameter1 = 20
parameter2=60
intApertureSize=1

cap=cv2.VideoCapture(0)

while(True):
   ret, frame = cap.read()

   frame = cv2.GaussianBlur(frame, (kernelSize, kernelSize), 0, 0)

   # frame = cv2.Canny(frame, parameter1, parameter2, intApertureSize)

   # frame = cv2.Laplacian(frame, cv2.CV_64F)

   frame = cv2.Sobel(frame, cv2.CV_64F,1, 0, ksize=kernelSize) #X direction edge detection
   frame = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=kernelSize) #Y direction edge detection

   cv2.imshow('Edge Detection', frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()