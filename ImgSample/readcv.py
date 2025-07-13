import cv2

# 컬러 이미지. 투명영역은 무시(기본값)
img_color = cv2.imread('imgCat.jpg', cv2.IMREAD_COLOR)
# 흑백 이미지.
img_gray = cv2.imread('imgCat.jpg', cv2.IMREAD_GRAYSCALE)
# 투명역역 포함
img_unchanged = cv2.imread('imgCat.jpg', cv2.IMREAD_UNCHANGED)

# 세로, 가로, Channel
img = img_color.shape
print (img)

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)

# 키 입력 기다리기
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()