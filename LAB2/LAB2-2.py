import cv2
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def create_histogram_and_equalized(image_path, title):

    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    equalized_img = cv2.equalizeHist(gray_img)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title(f'{title} (Grayscale)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(equalized_img, cmap='gray')
    plt.title(f'{title} (Equalized)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


try:
    create_histogram_and_equalized('lenna.png', 'Lenna')
    create_histogram_and_equalized('stuff_color_1.png', 'Stuff Color 1')

except FileNotFoundError as e:
    print(f"404 Error")
except Exception as e:
    print(f"error : {str(e)}")