import cv2
import numpy as np


def convert_rgb_to_hsv_split_and_equalize_v(image_path, hsv_output_path, h_output_path, s_output_path, v_output_path,
                                            v_eq_output_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imwrite(hsv_output_path, hsv_img)
    print(f"HSV image saved as {hsv_output_path}")

    h, s, v = cv2.split(hsv_img)

    h_img = np.zeros_like(img)
    h_img[:, :, 0] = h

    s_img = np.zeros_like(img)
    s_img[:, :, 1] = s

    v_img = np.zeros_like(img)
    v_img[:, :, 2] = v

    cv2.imwrite(h_output_path, h_img)
    print(f"H channel image saved as {h_output_path}")

    cv2.imwrite(s_output_path, s_img)
    print(f"S channel image saved as {s_output_path}")

    cv2.imwrite(v_output_path, v_img)
    print(f"V channel image saved as {v_output_path}")

    v_eq = cv2.equalizeHist(v)

    v_eq_img = np.zeros_like(img)
    v_eq_img[:, :, 2] = v_eq

    cv2.imwrite(v_eq_output_path, v_eq_img)
    print(f"Equalized V channel image saved as {v_eq_output_path}")


try:
    convert_rgb_to_hsv_split_and_equalize_v(
        'jenny.jpg',
        'jenny_hsv.png',
        'jenny_h.png',
        'jenny_s.png',
        'jenny_v.png',
        'jenny_v_eq.png'
    )
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")