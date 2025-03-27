import cv2

def process_image_with_all_steps(image_path, grayscale_output_path, blur_output_path, subtract_output_path,
                                 add_output_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(grayscale_output_path, gray_img)
    print(f"Grayscale image saved as {grayscale_output_path}")

    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    cv2.imwrite(blur_output_path, blurred_img)
    print(f"Blurred image saved as {blur_output_path}")

    subtracted_img = cv2.absdiff(gray_img, blurred_img)
    subtracted_img = cv2.normalize(subtracted_img, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(subtract_output_path, subtracted_img)
    print(f"Subtracted image saved as {subtract_output_path}")

    added_img = cv2.add(gray_img, subtracted_img)
    added_img = cv2.normalize(added_img, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(add_output_path, added_img)
    print(f"Added image saved as {add_output_path}")


try:
    process_image_with_all_steps('lenna.png', 'lenna_grayscale.png', 'lenna_blurred.png', 'lenna_subtracted.png',
                                 'lenna_added.png')
    process_image_with_all_steps('jenny.jpg', 'jenny_grayscale.png', 'jenny_blurred.png', 'jenny_subtracted.png',
                                 'jenny_added.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")