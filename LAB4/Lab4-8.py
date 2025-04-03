import cv2
import numpy as np


def convert_rgb_to_hsv_and_split(image_path, hsv_output_path, h_output_path, s_output_path, v_output_path):
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


def equalize_v_channel(v_input_path, v_eq_output_path):
    v_img = cv2.imread(v_input_path)
    v_channel = v_img[:, :, 2]

    v_eq = cv2.equalizeHist(v_channel)

    v_eq_img = np.zeros_like(v_img)
    v_eq_img[:, :, 2] = v_eq

    cv2.imwrite(v_eq_output_path, v_eq_img)
    print(f"Equalized V channel image saved as {v_eq_output_path}")
    return v_eq


def composite_hsv_and_convert_to_rgb(h_input_path, s_input_path, v_eq_input_path, hsv_eq_output_path):
    h_img = cv2.imread(h_input_path)
    s_img = cv2.imread(s_input_path)
    v_eq_img = cv2.imread(v_eq_input_path)

    h = h_img[:, :, 0]
    s = s_img[:, :, 1]
    v_eq = v_eq_img[:, :, 2]

    hsv_eq_img = cv2.merge((h, s, v_eq))

    cv2.imwrite(hsv_eq_output_path, hsv_eq_img)
    print(f"Composite HSV' image saved as {hsv_eq_output_path}")
    return hsv_eq_img


def convert_hsv_to_rgb(hsv_eq_input_path, rgb_output_path):
    hsv_eq_img = cv2.imread(hsv_eq_input_path)

    rgb_eq_img = cv2.cvtColor(hsv_eq_img, cv2.COLOR_HSV2BGR)

    cv2.imwrite(rgb_output_path, rgb_eq_img)
    print(f"Converted RGB image from HSV' saved as {rgb_output_path}")


try:
    convert_rgb_to_hsv_and_split(
        'jenny.jpg',
        'jenny_hsv.png',
        'jenny_h.png',
        'jenny_s.png',
        'jenny_v.png'
    )

    equalize_v_channel('jenny_v.png', 'jenny_v_eq.png')

    composite_hsv_and_convert_to_rgb(
        'jenny_h.png',
        'jenny_s.png',
        'jenny_v_eq.png',
        'jenny_hsv_eq.png'
    )

    convert_hsv_to_rgb('jenny_hsv_eq.png', 'jenny_hsv2rgb.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")