import cv2

# 이미지 불러오기
image1 = cv2.imread('lenna.png')
image2 = cv2.imread('orange.jpg')

# 두 이미지 크기를 동일하게 맞추기
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# 이미지 addWeighted
added_image = cv2.addWeighted(image1, 0.3, image2, 0.7, 0)
# 결과 출력
cv2.imshow('Result Image', added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()