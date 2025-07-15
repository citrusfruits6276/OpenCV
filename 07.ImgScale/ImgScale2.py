import cv2
import os

script_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_path, '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(img_path)

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
#dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # 이미지 크기 조정 (비율로 줄일 때)
dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # 이미지 크기 조정 (비율로 키울 때)

cv2.imshow('original', img)
cv2.imshow('resized', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()