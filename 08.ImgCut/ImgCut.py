import cv2
import os

script_path = os.path.join(os.path.dirname(__file__), '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
crop = img[100:400, 200:400] #세로 가로 
img[100:400, 400:600] = crop

cv2.imshow('original', img)
cv2.imshow('cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()