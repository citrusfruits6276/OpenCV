import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)
RADIUS = 50
THICKNESS = 3
cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) # 테두리만 있는 원
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) # 채워진 원

cv2.imshow('img', img) # 창 이름 'img'로 이미지 표시
cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 자원 해제