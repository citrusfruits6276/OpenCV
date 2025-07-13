import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 0, 0) # 파란색
THICKNESS = 3
cv2.rectangle(img, (200, 100), (300, 200), COLOR, THICKNESS, cv2.LINE_AA) 
cv2.rectangle(img, (400, 100), (300, 200), COLOR, cv2.FILLED, cv2.LINE_AA) 

cv2.imshow('img', img) # 창 이름 'img'로 이미지 표시
cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 자원 해제