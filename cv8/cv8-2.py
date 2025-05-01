import cv2
import os

# 결과 이미지 저장 폴더 생성
save_dir = 'output_images'
os.makedirs(save_dir, exist_ok=True)

# 마스크 이미지 로드
mask = cv2.imread('mask.png')

# 웹캠 켜기
webcam = cv2.VideoCapture(0)

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
        return w//2, h//2  # 예외처리
    px = mx // cnt
    py = my // cnt
    return px, py

print("웹캠 실행 중... 'c' 키를 누르면 촬영하고 이미지 저장, 'q' 키를 누르면 종료합니다.")

while True:
    status, frame = webcam.read()
    if not status:
        print("웹캠에서 프레임을 읽을 수 없습니다.")
        break

    # 라이브 화면 보여주기
    cv2.imshow("Live Feed", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        print("촬영 시작")

        frame = cv2.resize(frame, (600, 400))
        mask_resized = cv2.resize(mask, (600, 400))
        cv2.imwrite(f"{save_dir}/01_frame.jpg", frame)

        add1 = cv2.add(frame, mask_resized)
        cv2.imwrite(f"{save_dir}/02_add1.jpg", add1)

        ycrcb = cv2.cvtColor(add1, cv2.COLOR_BGR2YCrCb)
        cv2.imwrite(f"{save_dir}/03_ycrcb.jpg", ycrcb)

        Skin_Area = cv2.inRange(ycrcb, (0, 140, 90), (255, 160, 120))
        cv2.imwrite(f"{save_dir}/04_Skin_Area.jpg", Skin_Area)

        gray_frame = cv2.cvtColor(add1, cv2.COLOR_BGR2GRAY)
        Skin = cv2.add(gray_frame, ~Skin_Area)
        cv2.imwrite(f"{save_dir}/05_Skin.jpg", Skin)

        ret, Skin_bi = cv2.threshold(Skin, 250, 255, cv2.THRESH_BINARY)
        cv2.imwrite(f"{save_dir}/06_Skin_bi.jpg", Skin_bi)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        Skin_bi_erode = cv2.erode(Skin_bi, kernel, iterations=1)
        cv2.imwrite(f"{save_dir}/07_Skin_bi_erode.jpg", Skin_bi_erode)

        cx, cy = Center_of_mass(Skin_bi_erode)
        cx, cy = int(cx), int(cy)
        radius = 45
        frame_center = frame.copy()
        cv2.circle(frame_center, (cx, cy), radius, (255, 0, 0), 2)
        cv2.imwrite(f"{save_dir}/08_center_frame.jpg", frame_center)

        Skin_Copy = Skin.copy()
        cv2.circle(Skin_Copy, (cx, cy), radius, (0, 0, 0), -1)
        cv2.imwrite(f"{save_dir}/09_palm_Skin.jpg", Skin_Copy)

        palm = cv2.subtract(Skin, Skin_Copy)
        cv2.imwrite(f"{save_dir}/10_palm.jpg", palm)

        CannyEdge = cv2.Canny(palm, 50, 150)
        cv2.circle(CannyEdge, (cx, cy), radius, (0, 0, 0), 3)
        cv2.imwrite(f"{save_dir}/11_CannyEdge.jpg", CannyEdge)

        Result = CannyEdge.copy()
        cv2.circle(Result, (cx, cy), radius, (0, 0, 0), 3)
        cv2.imwrite(f"{save_dir}/12_Result.jpg", Result)

        print("촬영 및 이미지 저장 완료!")

    elif key == ord('q'):
        print("프로그램 종료")
        break

webcam.release()
cv2.destroyAllWindows()
