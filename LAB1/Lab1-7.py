import cv2
import numpy as np

# LUT (Look-Up Table) 생성
lut_inverse = np.zeros((256, 1), dtype=np.uint8)
lut_sqrt = np.zeros((256, 1), dtype=np.uint8)
lut_cube = np.zeros((256, 1), dtype=np.uint8)

for i in range(256):
    # 반전 LUT (Inverse)
    lut_inverse[i] = 255 - i
    # 제곱근 LUT (Square Root)
    lut_sqrt[i] = int((i / 255) ** (1/2) * 255)
    # 세제곱 LUT (Cube)
    lut_cube[i] = int((i / 255) ** 3 * 255)

# 이미지 불러오기
image = cv2.imread('stuff_color_1.png', cv2.IMREAD_GRAYSCALE)

# LUT 적용 (대비 & 밝기 조정)
image_inverse = cv2.LUT(image, lut_inverse)  # 반전
image_sqrt = cv2.LUT(image, lut_sqrt)        # 제곱근 (밝기 증가 효과)
image_cube = cv2.LUT(image, lut_cube)        # 세제곱 (어두운 영역 강조)

# 결과 출력
cv2.imshow('Original', image)
cv2.imshow('Inverse LUT', image_inverse)
cv2.imshow('Square Root LUT', image_sqrt)
cv2.imshow('Cube LUT', image_cube)

cv2.waitKey(0)
cv2.destroyAllWindows()
