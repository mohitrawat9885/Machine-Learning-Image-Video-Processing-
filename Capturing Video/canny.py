import numpy as np
import cv2

kernelSize=21 # Kernel Bluring size

# Edge Detection Parameter
parameter1=20
parameter2=60
intApertureSize=1

cap = cv2.VideoCapture(0)

while(True):
   # Capture frame-by-frame
   ret, frame = cap.read()

# Our operations on the frame come here
   frame = cv2.GaussianBlur(frame, (kernelSize,kernelSize), 0, 0)

   frame = cv2.Canny(frame,parameter1,parameter2,intApertureSize) # Canny edge detection
   cv2.imshow('Canny',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
      break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
