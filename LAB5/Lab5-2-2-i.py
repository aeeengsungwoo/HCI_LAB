import cv2
import numpy as np


def enlarge_image_center(image_path, output_path, scale=1.5):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    scale_matrix = cv2.getRotationMatrix2D(center, 0, scale)

    new_width, new_height = int(width * scale), int(height * scale)

    enlarged_img = cv2.warpAffine(img, scale_matrix, (new_width, new_height))

    cv2.imwrite(output_path, enlarged_img)
    print(f"Enlarged image saved as {output_path}")


try:
    enlarge_image_center('briefcase.jpg', 'briefcase_center_enlarged.png', scale=1.5)
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")