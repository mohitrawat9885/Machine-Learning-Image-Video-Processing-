import numpy as np
import cv2

scaling_factorx=1
scaling_factory=0.5

cap = cv2.VideoCapture(0)
while(True):
   ret, frame = cap.read() # ret = 1 if the video is captured; frame is the image
   frame=cv2.resize(frame,None,fx=scaling_factorx,fy=scaling_factory,interpolation=cv2.INTER_AREA)
   cv2.imshow("Smaller Window", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()