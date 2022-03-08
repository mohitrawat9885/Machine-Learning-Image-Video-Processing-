import cv2

cap = cv2.VideoCapture(0)

while(True):
   # Capture frame-by-frame
   ret, frame = cap.read()
   img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

   cv2.imshow("My Image", img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()