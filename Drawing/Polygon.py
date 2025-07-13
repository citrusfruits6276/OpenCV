import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 0)  # 녹색
THICKNESS = 3

pts1 = np.array([[100, 100], [200, 50], [300, 100], [350, 200], [250, 300], [150, 200]])
pts2 = np.array([[300, 200], [400, 200], [400, 300], [300, 300]])
#cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
pts3 = np.array([[[100, 200],[400, 300],[300, 400]], [[200, 300],[400, 400],[300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

