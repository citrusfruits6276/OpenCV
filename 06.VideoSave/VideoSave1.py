import cv2
import os

scripts_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(scripts_dir, '../02.VideoSample/VideoCat.mp4')
video_path = os.path.normpath(video_path)

cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 설정

fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임 수
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 프레임 너비
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 프레임 높이

vidoo_save_path = os.path.join(scripts_dir, '../06.VideoSave/saved_video.avi')
vidoo_save_path = os.path.normpath(vidoo_save_path)

out = cv2.VideoWriter(vidoo_save_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('더이상 가져올 프레임이 없음')
        break

    out.write(frame) # 프레임을 비디오 파일에 저장(소리 없음)
    cv2.namedWindow('video', cv2.WINDOW_NORMAL) # 창 크기 조정 가능
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break

out.release()
cap.release()
cv2.destroyAllWindows()

