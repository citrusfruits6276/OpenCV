import cv2
import os

script_path = os.path.join(os.path.dirname(__file__), '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #  90도 회전
rotate_180 = cv2.rotate(img, cv2.ROTATE_180) # 180도 회전
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 270도 회전

cv2.imshow('original', img)
cv2.imshow('rotated', rotate_270)

cv2.waitKey(0)
cv2.destroyAllWindows()