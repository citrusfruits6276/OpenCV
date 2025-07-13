import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (0, 255, 255) # 녹색
THIKNESS = 3

cv2.line(img, (100, 100), (200, 300), COLOR, THIKNESS, cv2.LINE_4) # 수직선
cv2.line(img, (200, 100), (300, 400), COLOR, THIKNESS, cv2.LINE_8) # 수직선
cv2.line(img, (300, 100), (500, 600), COLOR, THIKNESS, cv2.LINE_AA) # 수직선

cv2.imshow('img', img) # 창 이름 'img'로 이미지 표시
cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 자원 해제
