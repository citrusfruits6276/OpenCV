import cv2
import os

video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../02.VideoSample/VideoCat.mp4')
video_path = os.path.normpath(video_path)

cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('더이상 가져올 프레임이 없음')
        break

    frame_resize = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('video', frame_resize)
    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break

cap.release()
cv2.destroyAllWindows()