import cv2
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def convert_to_grayscale(image_path, output_path=None):
    # 이미지 읽기
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image file {image_path} not found.")

    # 그레이스케일로 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 그레이스케일 이미지 표시
    plt.figure(figsize=(5, 5))
    plt.imshow(gray_img, cmap='gray')
    plt.title('Lenna (Grayscale)')
    plt.axis('off')
    plt.show()

    # 필요 시 파일로 저장
    if output_path:
        cv2.imwrite(output_path, gray_img)
        print(f"Grayscale image saved as {output_path}")


# 이미지 변환 실행
try:
    convert_to_grayscale('lenna.jpg', 'img/lenna_grayscale.jpg')
except FileNotFoundError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")