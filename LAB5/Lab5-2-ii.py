import cv2


def enlarge_image(image_path, output_path, scale_factor=1.5):
    img = cv2.imread(image_path)

    height, width = img.shape[:2]
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)

    enlarged_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    cv2.imwrite(output_path, enlarged_img)
    print(f"Enlarged image saved as {output_path}")


try:
    enlarge_image('briefcase.jpg', 'briefcase_enlarged.png', scale_factor=1.5)
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")