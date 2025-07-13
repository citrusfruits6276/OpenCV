import cv2
import os

# 현재 스크립트의 디렉토리 경로를 가져옴
scripts_dir = os.path.dirname(os.path.abspath(__file__))
# 이미지 파일 경로 설정
img_path = os.path.join(scripts_dir, '../01.ImgSample/imgCat.jpg')
# 경로를 정규화하여 운영체제에 맞게 변환
img_path = os.path.normpath(img_path)

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_save_path = os.path.join(scripts_dir, '../05.ImgSave/saved_image.jpg')
img_save_path = os.path.normpath(img_save_path)
result = cv2.imwrite(img_save_path, img)  # 이미지 저장
print(result)  # 저장 성공 여부 출력w
