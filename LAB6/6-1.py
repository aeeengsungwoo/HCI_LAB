import cv2

# USB 카메라 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라; 필요 시 다른 인덱스로 변경

# 카메라가 제대로 열렸는지 확인
if not cap.isOpened():
    print("에러: 카메라를 열 수 없습니다.")
    exit()

# 프레임 캡처
ret, frame = cap.read()
if not ret:
    print("에러: 프레임을 읽을 수 없습니다.")
    cap.release()
    exit()

# 캡처한 이미지를 파일로 저장
cv2.imwrite('captured_image.jpg', frame)
print("이미지가 'captured_image.jpg'로 저장되었습니다.")

# 카메라 해제
cap.release()