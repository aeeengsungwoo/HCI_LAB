import cv2
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def convert_to_grayscale(image_path, output_path=None):

    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image file {image_path} not found.")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(5, 5))
    plt.imshow(gray_img, cmap='gray')
    plt.title('Lenna (Grayscale)')
    plt.axis('off')
    plt.show()

try:
    convert_to_grayscale('lenna.png', 'lenna_grayscale.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error : {str(e)}")