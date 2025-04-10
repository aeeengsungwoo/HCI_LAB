import cv2
import numpy as np


def rotate_image_center(image_path, output_path, angle=30):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)

    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    cv2.imwrite(output_path, rotated_img)
    print(f"Rotated image saved as {output_path}")
    return rotated_img


def repeat_rotation(image_path, output_path, angle=30, num_rotations=11):
    img = cv2.imread(image_path)

    for i in range(num_rotations):
        height, width = img.shape[:2]
        center = (width // 2, height // 2)

        rotation_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)

        img = cv2.warpAffine(img, rotation_matrix, (width, height))
        print(f"Rotation {i + 1}/{num_rotations} completed")

    cv2.imwrite(output_path, img)
    print(f"Final rotated image (A image) saved as {output_path}")


try:
    rotated_img = rotate_image_center('briefcase.jpg', 'briefcase_rotated_1i.png', angle=30)

    repeat_rotation('briefcase_rotated_1i.png', 'briefcase_A_1ii.png', angle=30, num_rotations=11)
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")