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
    subtracted = cv2.absdiff(gray_img, dilated_img)
    subtracted = cv2.normalize(subtracted, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(f'{output_prefix}_subtracted.png', subtracted)
    return subtracted


# Step 1-(4): Otsu Binarization on the Subtraction output
def perform_otsu_binarization(subtracted_img, output_prefix):
    _, binary = cv2.threshold(subtracted_img, 120, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(f'{output_prefix}_binary.png', binary)
    return binary


# Step 1-(5): Labeling using cv2.findContours on the Binarized output
def perform_labeling(binary_img, output_prefix):
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    labeled = np.zeros_like(binary_img, dtype=np.uint16)
    for i, contour in enumerate(contours):
        cv2.drawContours(labeled, [contour], -1, (i + 1) * 10, -1)
    labeled = cv2.normalize(labeled, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(f'{output_prefix}_labeled.png', labeled)
    return labeled


# Step 2-(6): Find edges of step4 output using Canny (First method)
def find_edges_canny(binary_img, output_prefix):
    edges = cv2.Canny(binary_img, 100, 200)
    cv2.imwrite(f'{output_prefix}_edges1.png', edges)
    return edges


# Step 2-(7): Find edges of step4 output using Sobel (Second method, kernel size 5x5)
def find_edges_sobel(binary_img, output_prefix):
    sobelx = cv2.Sobel(binary_img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(binary_img, cv2.CV_64F, 0, 1, ksize=5)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(f'{output_prefix}_edges2_sobel.png', sobel_combined)
    return sobel_combined


# Step 2-(8): Closing on the Sobel output using MORPH_CLOSE
def perform_closing(sobel_img, output_prefix):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(sobel_img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(f'{output_prefix}_edges2_closed.png', closed)
    return closed


# Step 2-(9): Opening on the Closing output using MORPH_OPEN
def perform_opening(closed_img, output_prefix):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Using a 5x5 rectangular kernel
    opened = cv2.morphologyEx(closed_img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(f'{output_prefix}_edges2_opened.png', opened)
    return opened


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

    # Perform edge detection (first method - Canny)
    find_edges_canny(binary, output_prefix)

    # Perform edge detection (second method - Sobel)
    sobel_edges = find_edges_sobel(binary, output_prefix)

    # Perform closing (second method - Closing)
    closed = perform_closing(sobel_edges, output_prefix)

    # Perform opening (second method - Opening)
    perform_opening(closed, output_prefix)


# Main execution
if __name__ == "__main__":
    images = ["stuff_color_1.png", "rice.png"]
    for img_path in images:
        output_prefix = img_path.split('.')[0]
        process_image(img_path, output_prefix)