import cv2

cap = cv2.VideoCapture(0) # 0번째 카메라

if not cap.isOpened():
    exit()

while True :
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()