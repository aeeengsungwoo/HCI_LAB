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


# Step 1-(3): Subtract the Dilation output from the original grayscale image
def perform_subtraction(gray_img, dilated_img, output_prefix):
    # Use absdiff to avoid negative clipping
    subtracted = cv2.absdiff(gray_img, dilated_img)
    # Normalize the result for better visualization
    subtracted = cv2.normalize(subtracted, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(f'{output_prefix}_subtracted.png', subtracted)
    return subtracted


# Step 1-(4): Otsu Binarization on the Subtraction output
def perform_otsu_binarization(subtracted_img, output_prefix):
    # Apply Otsu binarization with threshold=120 (though Otsu will override it)
    _, binary = cv2.threshold(subtracted_img, 120, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(f'{output_prefix}_binary.png', binary)
    return binary


# Step 1-(5): Labeling using cv2.findContours on the Binarized output
def perform_labeling(binary_img, output_prefix):
    # Find contours
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank image for labeling
    labeled = np.zeros_like(binary_img, dtype=np.uint16)

    # Label each contour with a unique value
    for i, contour in enumerate(contours):
        cv2.drawContours(labeled, [contour], -1, (i + 1) * 10, -1)

    # Normalize labeled image for visualization (optional)
    labeled = cv2.normalize(labeled, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(f'{output_prefix}_labeled.png', labeled)
    return labeled


# Process each image
def process_image(image_path, output_prefix):
    # Load and convert to grayscale
    gray = load_and_convert_to_grayscale(image_path)
    cv2.imwrite(f'{output_prefix}_gray.png', gray)

    # Perform erosion
    eroded, kernel = perform_erosion(gray, output_prefix)

    # Perform dilation
    dilated = perform_dilation(eroded, kernel, output_prefix)

    # Perform subtraction
    subtracted = perform_subtraction(gray, dilated, output_prefix)

    # Perform Otsu binarization
    binary = perform_otsu_binarization(subtracted, output_prefix)

    # Perform labeling
    perform_labeling(binary, output_prefix)


# Main execution
if __name__ == "__main__":
    images = ["stuff_color_1.png", "rice.png"]
    for img_path in images:
        output_prefix = img_path.split('.')[0]
        process_image(img_path, output_prefix)