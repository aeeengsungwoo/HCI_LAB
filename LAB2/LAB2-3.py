import cv2
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def process_image(image_path, title):

    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized_img = cv2.equalizeHist(gray_img)

    orig_histogram = cv2.calcHist([gray_img], [0], None, [256], [0, 256])  # i
    equalized_histogram = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])  # iii

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title(f'{title} (Grayscale)')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.plot(orig_histogram)
    plt.title('Original Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True)

    plt.subplot(2, 3, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title(f'{title} (Equalized)')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.plot(equalized_histogram)
    plt.title(f'Equalized Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True)

    plt.tight_layout()
    plt.show()


try:
    process_image('lenna.png', 'Lenna')
    process_image('stuff_color_1.png', 'Stuff Color 1')

except FileNotFoundError as e:
    print(f"404 Error")
except Exception as e:
    print(f"error : {str(e)}")