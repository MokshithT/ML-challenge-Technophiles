import pytesseract
from PIL import Image
import cv2
import os
import re
import numpy as np
# Path to the folder where images are stored
image_dir = 'images'

# Function to preprocess the image for better OCR results
def preprocess_image(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Convert to a numpy array for OpenCV processing
    img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Apply thresholding (optional)
    _, img_thresh = cv2.threshold(img_np, 150, 255, cv2.THRESH_BINARY)
    
    # Convert back to PIL Image for OCR
    processed_img = Image.fromarray(img_thresh)
    
    return processed_img

# Function to extract text from images using pytesseract
def extract_text_from_image(image_path):
    try:
        # Preprocess the image
        img = preprocess_image(image_path)
        
        # Use pytesseract to extract text
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

# Apply OCR to all images and save results
ocr_results = {}

for image_file in os.listdir(image_dir):
    if image_file.endswith(".jpg"):
        image_path = os.path.join(image_dir, image_file)
        
        # Extract text from image
        text = extract_text_from_image(image_path)
        ocr_results[image_file] = text
        
        print(f"OCR Result for {image_file}:\n{text}\n{'='*50}\n")

# Saving the OCR results to a file (optional)
with open('ocr_results.txt', 'w') as f:
    for image_file, text in ocr_results.items():
        f.write(f"{image_file}:\n{text}\n{'='*50}\n")
