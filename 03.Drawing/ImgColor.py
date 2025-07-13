import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
img[100:200, 200:300] = (255, 255, 255)  # 흰색 배경
cv2.imshow('img', img) # 창 이름 'img'로 이미지 표시
cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows()# 자원 해제

