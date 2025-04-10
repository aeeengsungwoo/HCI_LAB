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
    return enlarged_img


def rotate_image_center(image_path, output_path, angle=45):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    cv2.imwrite(output_path, rotated_img)
    print(f"Rotated image saved as {output_path}")
    return rotated_img, width, height


def subtract_images(a_img, b_img, a_width, a_height, output_path):
    b_img_resized = cv2.resize(b_img, (a_width, a_height), interpolation=cv2.INTER_LINEAR)

    subtracted_img = cv2.subtract(a_img, b_img_resized)

    cv2.imwrite(output_path, subtracted_img)
    print(f"Subtracted image saved as {output_path}")

    if np.all(subtracted_img == 0):
        print("The two images are identical (result is a black image).")
    else:
        print("The two images are different (result is not a black image).")


try:
    a_img = enlarge_image_center('briefcase.jpg', 'briefcase_enlarged_2i.png', scale=1.5)

    b_img, original_width, original_height = rotate_image_center('briefcase.jpg', 'briefcase_rotated_2ii.png', angle=45)

    a_height, a_width = a_img.shape[:2]
    subtract_images(a_img, b_img, a_width, a_height, 'briefcase_subtracted_3.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")