import cv2
import numpy as np


def rotate_image_center(img, angle=30):
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
    return rotated_img


def repeat_rotation(img, angle=30, num_rotations=11):
    for i in range(num_rotations):
        img = rotate_image_center(img, angle)
        print(f"Rotation {i + 1}/{num_rotations} completed")
    return img


def subtract_images(original_img, processed_img, output_path):
    subtracted_img = cv2.subtract(original_img, processed_img)
    cv2.imwrite(output_path, subtracted_img)
    print(f"Subtracted image saved as {output_path}")

    if np.all(subtracted_img == 0):
        print("The two images are identical (result is a black image).")
    else:
        print("The two images are different (result is not a black image).")


try:
    original_img = cv2.imread('briefcase.jpg')
    if original_img is None:
        raise FileNotFoundError("briefcase.jpg not found")

    # 1st cycle
    current_img = rotate_image_center(original_img, angle=30)
    current_img = repeat_rotation(current_img, angle=30, num_rotations=11)

    # Remaining cycles
    num_cycles = 6
    for cycle in range(2, num_cycles + 1):
        current_img = rotate_image_center(current_img, angle=30)
        current_img = repeat_rotation(current_img, angle=30, num_rotations=11)
        print(f"Cycle {cycle}/{num_cycles} completed")

    # Save final result
    final_output_path = 'briefcase_final_rotated.png'
    cv2.imwrite(final_output_path, current_img)
    print(f"Final rotated image saved as {final_output_path}")

    # Subtract and compare
    subtract_images(original_img, current_img, 'briefcase_subtracted_2-1-(3).png')

except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")
