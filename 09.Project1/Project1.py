import cv2
import os
import numpy as np

script_path = os.path.join(os.path.dirname(__file__), '../08.ImgCut/Poker.jpg')
img_path = os.path.normpath(script_path)
img = cv2.imread(img_path)

drawing = False

point_list = []
def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))

    if drawing:
        prev_point = None
        for point in point_list:
            cv2.circle(dst_img, point, 15, (0, 255, 0), cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, (0, 255, 0), 3, cv2.LINE_AA)
            prev_point = point

        next_point = (x, y)
        if len(point_list) == 4:
               show_result()
               next_point = point_list[0]

        cv2.line(dst_img, prev_point, next_point, (0, 255, 0), 3, cv2.LINE_AA)

        
    cv2.imshow('img', dst_img)

def show_result():
    width, height = 530, 710
    scr = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(scr, dst)
    result = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow('original', result)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', img)  
cv2.waitKey(0)
cv2.destroyAllWindows()