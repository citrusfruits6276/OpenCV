import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)


SCALE = 0.5
COLOR = (255, 255, 255)  # 흰색
THICKNESS = 1
#보통 크기 산 세레프
cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
#작은 크기 세레프
cv2.putText(img, "FONT_HERSHEY_PLAIN", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
#필기체 스타일 세레프
cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
#보통 크기 세레프
cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
#보통 크기 산 세레프, 기울임꼴
cv2.putText(img, "FONT_ITALIC", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)


cv2.imshow('text', img)
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 자원 해제