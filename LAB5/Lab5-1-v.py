import cv2
import numpy as np


def convert_to_grayscale(image_path, output_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_eq = cv2.equalizeHist(gray_img)

    cv2.imwrite(output_path, gray_eq)
    print(f"Grayscale image saved as {output_path}")
    return gray_eq


def extract_sobel_edge(gray_img, output_path):
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(output_path, sobel_combined)
    print(f"Sobel edge image saved as {output_path}")
    return sobel_combined


def extract_laplacian_edge(gray_img, output_path):
    laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)

    laplacian = cv2.convertScaleAbs(laplacian)

    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(output_path, laplacian)
    print(f"Laplacian edge image saved as {output_path}")
    return laplacian


def extract_canny_edge(gray_img, output_path):
    canny = cv2.Canny(gray_img, 30, 150)

    cv2.imwrite(output_path, canny)
    print(f"Canny edge image saved as {output_path}")
    return canny


def extract_log_edge(gray_img, output_path, sigma=2):
    blurred = cv2.GaussianBlur(gray_img, (0, 0), sigma)

    log = cv2.Laplacian(blurred, cv2.CV_64F)

    log = cv2.convertScaleAbs(log)

    log = cv2.normalize(log, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(output_path, log)
    print(f"Laplacian of Gaussian (LoG) edge image saved as {output_path}")


try:
    jenny_gray = convert_to_grayscale('jenny.jpg', 'jenny_grayscale.png')
    rice_gray = convert_to_grayscale('rice.png', 'rice_grayscale.png')

    extract_sobel_edge(jenny_gray, 'jenny_sobel.png')
    extract_sobel_edge(rice_gray, 'rice_sobel.png')

    extract_laplacian_edge(jenny_gray, 'jenny_laplacian.png')
    extract_laplacian_edge(rice_gray, 'rice_laplacian.png')

    extract_canny_edge(jenny_gray, 'jenny_canny.png')
    extract_canny_edge(rice_gray, 'rice_canny.png')

    extract_log_edge(jenny_gray, 'jenny_log.png', sigma=2)
    extract_log_edge(rice_gray, 'rice_log.png', sigma=2)
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")