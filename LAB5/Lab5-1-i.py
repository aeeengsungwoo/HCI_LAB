import cv2
def convert_to_grayscale(image_path, output_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_path, gray_img)
    print(f"Grayscale image saved as {output_path}")


try:
    convert_to_grayscale('jenny.jpg', 'jenny_grayscale.png')
    convert_to_grayscale('rice.png', 'rice_grayscale.png')
except FileNotFoundError as e:
    print(f"404 Error: {str(e)}")
except Exception as e:
    print(f"error: {str(e)}")