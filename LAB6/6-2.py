import cv2

# USB 카메라 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라; 필요 시 다른 인덱스로 변경

# 카메라가 제대로 열렸는지 확인
if not cap.isOpened():
    print("에러: 카메라를 열 수 없습니다.")
    exit()

# 템플릿 이미지 로드 (컬러 이미지로 로드)
template = cv2.imread('img.png')
if template is None:
    print("에러: 템플릿 이미지를 로드할 수 없습니다.")
    cap.release()
    exit()

# 템플릿 이미지의 크기(너비, 높이) 가져오기
h, w, _ = template.shape  # 컬러 이미지이므로 채널 정보 포함

# 프레임 캡처
ret, frame = cap.read()
if not ret:
    print("에러: 프레임을 읽을 수 없습니다.")
    cap.release()
    exit()

# 템플릿 매칭 수행 (컬러 이미지 그대로 사용)
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

# 매칭 결과에서 최적의 위치 찾기
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 좋은 매칭을 위한 임계값 설정 (필요에 따라 조정)
threshold = 0.4
if max_val >= threshold:
    # 매칭된 영역의 좌상단과 우하단 좌표 계산
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 매칭된 영역에 초록색 사각형 그리기
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    print("템플릿이 캡처된 이미지에서 감지되었습니다!")
else:
    print("템플릿을 찾을 수 없습니다. 매칭 점수:", max_val)

# 결과 이미지 저장
cv2.imwrite('result_image.jpg', frame)
print("결과 이미지가 'result_image.jpg'로 저장되었습니다.")

# 카메라 해제
cap.release()