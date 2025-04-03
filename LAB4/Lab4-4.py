import cv2


def convert_rgb_to_hsv(image_path, hsv_output_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imwrite(hsv_output_path, hsv_img)
    print(f"HSV image saved as {hsv_output_path}")


try:
    convert_rgb_to_hsv('jenny.jpg', 'jenny_hsv.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")