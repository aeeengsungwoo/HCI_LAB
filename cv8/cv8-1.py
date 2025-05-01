import cv2
import os

# 결과 이미지 저장 폴더 생성
save_dir = 'output_images'
os.makedirs(save_dir, exist_ok=True)

# 1. 웹캠 프레임 읽기 및 마스크 합성
webcam = cv2.VideoCapture(0)
mask = cv2.imread('mask.png')  # 미리 준비된 마스크 이미지 사용

while webcam.isOpened():
    status, frame = webcam.read()
    if not status:
        break

    # 1-1. 프레임과 마스크 크기 맞추기
    frame = cv2.resize(frame, (600, 400))
    mask_resized = cv2.resize(mask, (600, 400))
    cv2.imshow("frame", frame)
    cv2.imwrite(f"{save_dir}/01_frame.jpg", frame)

    # 1-2. 프레임과 마스크 합성
    add1 = cv2.add(frame, mask_resized)
    cv2.imshow("add1", add1)
    cv2.imwrite(f"{save_dir}/02_add1.jpg", add1)

    # 2. YCrCb 컬러 모델로 변환
    ycrcb = cv2.cvtColor(add1, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("ycrcb", ycrcb)
    cv2.imwrite(f"{save_dir}/03_ycrcb.jpg", ycrcb)

    # 3. 피부 영역 추출 (inRange)
    Skin_Area = cv2.inRange(ycrcb, (0, 140, 90), (255, 160, 120))
    cv2.imshow("Skin_Area", Skin_Area)
    cv2.imwrite(f"{save_dir}/04_Skin_Area.jpg", Skin_Area)

    # 4. 그레이스케일 변환 및 피부영역 적용
    gray_frame = cv2.cvtColor(add1, cv2.COLOR_BGR2GRAY)
    Skin = cv2.add(gray_frame, ~Skin_Area)
    cv2.imshow("Skin", Skin)
    cv2.imwrite(f"{save_dir}/05_Skin.jpg", Skin)

    # 5. 이진화 및 노이즈 제거
    ret, Skin_bi = cv2.threshold(Skin, 250, 255, cv2.THRESH_BINARY)
    cv2.imshow("Skin_bi", Skin_bi)
    cv2.imwrite(f"{save_dir}/06_Skin_bi.jpg", Skin_bi)

    # 노이즈가 심할 경우 침식(erode) 적용
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    Skin_bi_erode = cv2.erode(Skin_bi, kernel, iterations=1)
    cv2.imshow("Skin_bi_erode", Skin_bi_erode)
    cv2.imwrite(f"{save_dir}/07_Skin_bi_erode.jpg", Skin_bi_erode)

    # 6. Center of Mass(질량 중심) 계산 함수
    def Center_of_mass(img):
        cnt = 0
        mx = 0
        my = 0
        h, w = img.shape
        for i in range(h):
            for j in range(w):
                if img[i][j] < 125:  # 검은색(손바닥) 픽셀
                    cnt += 1
                    mx += j
                    my += i
        if cnt == 0:
            return w//2, h//2  # 예외처리: 중앙 리턴
        px = mx // cnt
        py = my // cnt
        return px, py

    # 7. 손바닥 중심 좌표 찾기 및 표시
    cx, cy = Center_of_mass(Skin_bi_erode)
    cx, cy = int(cx), int(cy)
    radius = 45
    frame_center = frame.copy()
    cv2.circle(frame_center, (cx, cy), radius, (255, 0, 0), 2)
    cv2.imshow("center_frame", frame_center)
    cv2.imwrite(f"{save_dir}/08_center_frame.jpg", frame_center)

    # 8. 손바닥 영역 추출
    Skin_Copy = Skin.copy()
    cv2.circle(Skin_Copy, (cx, cy), radius, (0, 0, 0), -1)  # 손바닥 부분을 검게 마스킹
    cv2.imshow("palm_Skin", Skin_Copy)
    cv2.imwrite(f"{save_dir}/09_palm_Skin.jpg", Skin_Copy)

    palm = cv2.subtract(Skin, Skin_Copy)
    cv2.imshow("palm", palm)
    cv2.imwrite(f"{save_dir}/10_palm.jpg", palm)

    # 9. 손금 추출 (Canny Edge)
    CannyEdge = cv2.Canny(palm, 50, 150)
    cv2.circle(CannyEdge, (cx, cy), radius, (0, 0, 0), 3)  # 원형 노이즈 제거
    cv2.imshow("CannyEdge", CannyEdge)
    cv2.imwrite(f"{save_dir}/11_CannyEdge.jpg", CannyEdge)

    # 10. 결과 이미지(노이즈 제거 후)
    Result = CannyEdge.copy()
    cv2.circle(Result, (cx, cy), radius, (0, 0, 0), 3)
    cv2.imshow("Result", Result)
    cv2.imwrite(f"{save_dir}/12_Result.jpg", Result)

    # 종료 조건
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
