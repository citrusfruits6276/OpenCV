import cv2
import numpy as np
import os

script_path = os.path.join(os.path.dirname(__file__), '../08.ImgCut/Poker.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path)

width, height = 530, 710

scr = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(scr, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('original', img)
cv2.imshow('transformed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()