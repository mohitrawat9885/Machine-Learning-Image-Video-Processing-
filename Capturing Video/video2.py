import numpy as np
import cv2
cap = cv2.VideoCapture('peoplewalking.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG()
while(1):
   ret, frame = cap.read()
   fgmask = fgbg.apply(frame)
   cv2.imshow('fgmask',frame) # original frame
   cv2.imshow('frame',fgmask) # result frame
   if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
      break
cap.release()
cv2.destroyAllWindows()