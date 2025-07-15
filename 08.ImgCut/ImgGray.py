import cv2
import os

script_path = os.path.join(os.path.dirname(__file__), '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
cv2.imshow('grayscale', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


