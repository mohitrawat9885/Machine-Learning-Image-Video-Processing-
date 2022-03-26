import numpy as np
import cv2

cap = cv2.VideoCapture('peoplewalking.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
   ret, frame = cap.read()
   fgmask = fgbg.apply(frame)
   fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN,kernel)
   cv2.imshow('frame', fgmask)

   if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
      break

cap.release()
cv2.destroyAllWindows()

