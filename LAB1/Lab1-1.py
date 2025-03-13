import cv2

# 이미지 불러오기
image1 = cv2.imread('stuff_color_1.png')
image2 = cv2.imread('stuff_color_2.png')

# 두 이미지 크기를 동일하게 맞추기
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# 이미지 합성 (덧셈)
added_image = cv2.add(image1, image2)

# 결과 출력
cv2.imshow('Result Image', added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
