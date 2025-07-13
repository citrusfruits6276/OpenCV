import cv2

cap = cv2.VideoCapture('VideoSample/VideoCat.mp4')

# 동영상 파일이 올바로 열려있는지
while cap.isOpened():
    # ret 성공여부 frame 받아온 이미지
    ret, frame = cap.read()
    if not ret:
        print('더이상 가져올 프레임이 없음')
        break
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow('video', frame)

    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break

cap.release() # 자원 해제
cv2.destroyAllWindows()