import cv2
import numpy as np

# 검은색 화면 생성
black_screen = np.zeros((480, 640, 3), dtype=np.uint8)
# 하얀색 화면 생성
white_screen = np.ones((480, 640, 3), dtype=np.uint8) * 255
# 검은색 화면에 글씨 추가
cv2.putText(black_screen, '2020112029', (50, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# 하얀색 화면에 글씨 추가
cv2.putText(white_screen, 'An Sung Woo', (50, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
# 검은색 화면 아래에 하얀색 화면 붙이기
combined_screen = np.vstack((black_screen, white_screen))
# 화면 표시
cv2.imshow('Combined Screen', combined_screen)
cv2.waitKey(0)
cv2.destroyAllWindows()
