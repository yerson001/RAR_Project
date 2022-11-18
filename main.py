import cv2
import numpy as np
import cv2.aruco

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if ret == False: break

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cap.destroyAllWindows()
