import cv2

def convert_to_grayscale(image_path, output_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_path, gray_img)
    print(f"Grayscale image saved as {output_path}")
    return gray_img


def extract_sobel_edge(gray_img, output_path):
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    cv2.imwrite(output_path, sobel_combined)
    print(f"Sobel edge image saved as {output_path}")
    return sobel_combined


def extract_laplacian_edge(gray_img, output_path):
    laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)

    laplacian = cv2.convertScaleAbs(laplacian)

    cv2.imwrite(output_path, laplacian)
    print(f"Laplacian edge image saved as {output_path}")


try:
    jenny_gray = convert_to_grayscale('jenny.jpg', 'jenny_grayscale.png')
    rice_gray = convert_to_grayscale('rice.png', 'rice_grayscale.png')

    extract_sobel_edge(jenny_gray, 'jenny_sobel.png')
    extract_sobel_edge(rice_gray, 'rice_sobel.png')

    extract_laplacian_edge(jenny_gray, 'jenny_laplacian.png')
    extract_laplacian_edge(rice_gray, 'rice_laplacian.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")