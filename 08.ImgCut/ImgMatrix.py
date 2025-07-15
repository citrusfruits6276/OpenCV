import cv2
import numpy as np
import os

script_path = os.path.join(os.path.dirname(__file__), '../08.ImgCut/NewsPaper.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path)

width, height = 640, 240

scr = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(scr, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('original', img)
cv2.imshow('transformed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()