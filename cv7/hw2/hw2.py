import cv2
import numpy as np


# Function to load and convert image to grayscale
def load_and_convert_to_grayscale(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image {image_path} not found")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


# Step 1-(1): Erosion with 11x11 MORPH_ELLIPSE kernel
def perform_erosion(gray_img, output_prefix):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    eroded = cv2.erode(gray_img, kernel)
    cv2.imwrite(f'{output_prefix}_eroded.png', eroded)
    return eroded, kernel


# Step 1-(2): Dilation on the output of Erosion
def perform_dilation(eroded_img, kernel, output_prefix):
    dilated = cv2.dilate(eroded_img, kernel)
    cv2.imwrite(f'{output_prefix}_dilated.png', dilated)
    return dilated


# Process each image
def process_image(image_path, output_prefix):
    # Load and convert to grayscale
    gray = load_and_convert_to_grayscale(image_path)
    cv2.imwrite(f'{output_prefix}_gray.png', gray)

    # Perform erosion
    eroded, kernel = perform_erosion(gray, output_prefix)

    # Perform dilation
    perform_dilation(eroded, kernel, output_prefix)


# Main execution
if __name__ == "__main__":
    images = ["stuff_color_1.png", "rice.png"]
    for img_path in images:
        output_prefix = img_path.split('.')[0]
        process_image(img_path, output_prefix)