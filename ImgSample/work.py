import cv2

# 이미지 읽기
img = cv2.imread('imgCat.jpg')

# 이미지 출력
cv2.imshow('imgCat', img)

# 키 입력을 기다리고, 키 코드 값 저장
key = cv2.waitKey(0)

# 키 코드 값 출력
print(key)

# 창 닫기
cv2.destroyAllWindows()