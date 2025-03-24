import cv2
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def process_image_with_thresholds(image_path, threshold_value=150, grayscale_output_path=None, binary_output_path=None,
                                  otsu_output_path=None):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(5, 5))
    plt.imshow(gray_img, cmap='gray')
    plt.title('Lenna (Grayscale)')
    plt.axis('off')
    plt.show()

    if grayscale_output_path:
        cv2.imwrite(grayscale_output_path, gray_img)
        print(f"Grayscale image saved as {grayscale_output_path}")

    _, binary_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(5, 5))
    plt.imshow(binary_img, cmap='gray')
    plt.title(f'Lenna (Binary Thresholded, Threshold={threshold_value})')
    plt.axis('off')
    plt.show()

    if binary_output_path:
        cv2.imwrite(binary_output_path, binary_img)
        print(f"Binary thresholded image saved as {binary_output_path}")

    otsu_threshold, otsu_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    plt.figure(figsize=(5, 5))
    plt.imshow(otsu_img, cmap='gray')
    plt.title(f'Lenna (Otsu Thresholded, Computed Threshold={otsu_threshold})')
    plt.axis('off')
    plt.show()

    if otsu_output_path:
        cv2.imwrite(otsu_output_path, otsu_img)
        print(f"Otsu thresholded image saved as {otsu_output_path}")


try:
    process_image_with_thresholds(
        'lenna.png',
        threshold_value=150,
        grayscale_output_path='lenna_grayscale.png',
        binary_output_path='lenna_binary.png',
        otsu_output_path='lenna_otsu.png'
    )
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")