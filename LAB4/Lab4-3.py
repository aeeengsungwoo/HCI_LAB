import cv2
import numpy as np


def split_equalize_and_composite_rgb_channels(image_path, r_output_path, g_output_path, b_output_path, r_eq_output_path,
                                              g_eq_output_path, b_eq_output_path, composite_output_path):
    img = cv2.imread(image_path)
    b, g, r = cv2.split(img)

    r_img = np.zeros_like(img)
    r_img[:, :, 2] = r

    g_img = np.zeros_like(img)
    g_img[:, :, 1] = g

    b_img = np.zeros_like(img)
    b_img[:, :, 0] = b

    cv2.imwrite(r_output_path, r_img)
    print(f"R channel image saved as {r_output_path}")

    cv2.imwrite(g_output_path, g_img)
    print(f"G channel image saved as {g_output_path}")

    cv2.imwrite(b_output_path, b_img)
    print(f"B channel image saved as {b_output_path}")

    r_eq = cv2.equalizeHist(r)
    g_eq = cv2.equalizeHist(g)
    b_eq = cv2.equalizeHist(b)

    r_eq_img = np.zeros_like(img)
    r_eq_img[:, :, 2] = r_eq

    g_eq_img = np.zeros_like(img)
    g_eq_img[:, :, 1] = g_eq

    b_eq_img = np.zeros_like(img)
    b_eq_img[:, :, 0] = b_eq

    cv2.imwrite(r_eq_output_path, r_eq_img)
    print(f"Equalized R channel image saved as {r_eq_output_path}")

    cv2.imwrite(g_eq_output_path, g_eq_img)
    print(f"Equalized G channel image saved as {g_eq_output_path}")

    cv2.imwrite(b_eq_output_path, b_eq_img)
    print(f"Equalized B channel image saved as {b_eq_output_path}")

    composite_img = cv2.merge((b_eq, g_eq, r_eq))

    cv2.imwrite(composite_output_path, composite_img)
    print(f"Composite R'G'B' image saved as {composite_output_path}")


try:
    split_equalize_and_composite_rgb_channels(
        'jenny.jpg',
        'jenny_r.png', 'jenny_g.png', 'jenny_b.png',
        'jenny_r_eq.png', 'jenny_g_eq.png', 'jenny_b_eq.png',
        'jenny_rgb_eq.png'
    )
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")