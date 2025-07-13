import cv2
import numpy as np
# 한글 우회
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype("fonts/gulim.ttc", font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)


img = np.zeros((480, 640, 3), dtype=np.uint8)


FONT_SIZE = 32
COLOR = (255, 255, 255)  # 흰색
THICKNESS = 1
#보통 크기 산 세레프
img = myPutText(img, "한글", (20, 50), FONT_SIZE, COLOR)

cv2.imshow('text_kr', img)
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 자원 해제