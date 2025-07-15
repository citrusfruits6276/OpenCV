import cv2
import os

script_path = os.path.join(os.path.dirname(__file__), '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
# flip_img = cv2.flip(img, 1)  # 수평으로 뒤집기
# flip_img = cv2.flip(img, 0) # 수직으로 뒤집기
flip_img = cv2.flip(img, -1)  # 수평 및 수직으로 뒤집기

cv2.imshow('flipped', flip_img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()