import cv2

def convert_to_grayscale_and_blur(image_path, blur_output_path=None):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if blur_output_path:
        cv2.imwrite(blur_output_path.replace('blurred', 'grayscale'), gray_img)
        print(f"Grayscale image saved as {blur_output_path.replace('blurred', 'grayscale')}")

    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    if blur_output_path:
        cv2.imwrite(blur_output_path, blurred_img)
        print(f"Blurred image saved as {blur_output_path}")


try:
    convert_to_grayscale_and_blur('lenna.png', 'lenna_blurred.png')
    convert_to_grayscale_and_blur('jenny.jpg', 'jenny_blurred.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")