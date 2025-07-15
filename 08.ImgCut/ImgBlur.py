import cv2
import os

script_path = os.path.join(os.path.dirname(__file__), '../01.ImgSample/imgCat.jpg')
img_path = os.path.normpath(script_path)

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
kernel_3 = cv2.GaussianBlur(img, (3, 3), 0)  # 3x3 가우시안 블러
kernel_5 = cv2.GaussianBlur(img, (5, 5), 0)  # 5x5 가우시안 블러
kernel_7 = cv2.GaussianBlur(img, (7, 7), 0)  # 7x7 가우시안 블러

sigma_3 = cv2.GaussianBlur(img, (0, 0), 1)  # 3x3 가우시안 블러, 시그마 1
sigma_5 = cv2.GaussianBlur(img, (0, 0), 2)  # 5x5 가우시안 블러, 시그마 2
sigma_7 = cv2.GaussianBlur(img, (0, 0), 3)  # 7x7 가우시안 블러, 시그마 3

cv2.imshow('original', img)
cv2.imshow('Gaussian Blur 3x3', kernel_3)
cv2.imshow('Gaussian Blur 5x5', kernel_5)
cv2.imshow('Gaussian Blur 7x7', kernel_7)
cv2.imshow('Gaussian Blur Sigma 1', sigma_3)
cv2.imshow('Gaussian Blur Sigma 2', sigma_5)
cv2.imshow('Gaussian Blur Sigma 3', sigma_7)
cv2.waitKey(0)
cv2.destroyAllWindows()