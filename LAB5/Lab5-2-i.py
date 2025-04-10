import cv2
import numpy as np


def rotate_and_scale_image(image_path, output_path, angle=45, scale=0.5):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    transformed_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    cv2.imwrite(output_path, transformed_img)
    print(f"Rotated and scaled image saved as {output_path}")


try:
    rotate_and_scale_image('briefcase.jpg', 'briefcase_rotated_scaled.png', angle=45, scale=0.5)
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")