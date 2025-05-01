import cv2

webcam = cv2.VideoCapture(0)
mask = cv2.imread('mask.png')  # 마스크 이미지는 미리 준비되어 있어야 함

while webcam.isOpened():
    status, frame = webcam.read()
    if status:
        frame = cv2.resize(frame, (600, 400))
        mask = cv2.resize(mask, (600, 400))
        cv2.imshow("frame", frame)

        add1 = cv2.add(frame, mask)
        cv2.imshow("add1", add1)

        ycrcb = cv2.cvtColor(add1, cv2.COLOR_BGR2YCrCb)
        cv2.imshow("ycrcb", ycrcb)

        Skin_Area = cv2.inRange(ycrcb, (0, 140, 90), (255, 160, 120))
        cv2.imshow("Skin_Area", Skin_Area)

        gray_frame = cv2.cvtColor(add1, cv2.COLOR_BGR2GRAY)
        Skin = cv2.add(gray_frame, ~Skin_Area)
        cv2.imshow("Skin", Skin)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()

