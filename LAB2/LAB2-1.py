import cv2
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def create_histogram(image_path, title):

    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    histogram = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    # 그레이스케일 이미지 표시
    plt.figure(figsize=(5, 5))
    plt.imshow(gray_img, cmap='gray')
    plt.title(f'{title} (Grayscale)')
    plt.axis('off')
    plt.show()

    plt.figure()
    plt.title(f'Histogram of {title}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()


try:
    create_histogram('lenna.png', 'Lenna')

    create_histogram('stuff_color_1.png', 'Stuff Color 1')

except FileNotFoundError as e:
    print(f"404 Error")
except Exception as e:
    print(f"error : {str(e)}")