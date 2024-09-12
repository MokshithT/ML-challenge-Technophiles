import os
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

# Create a directory to save the downloaded images
image_dir = 'images'
os.makedirs(image_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv('/Users/moksheethpatelthota/Desktop/MLhack/student_resource 3/dataset/train.csv')  # Assuming you have a train.csv with image_link

# Function to download images
def download_images(image_url, image_id, save_dir):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        
        # If the request is successful (status code 200)
        if response.status_code == 200:
            # Convert the image content to a PIL Image
            image = Image.open(BytesIO(response.content))
            
            # Create the path to save the image
            image_path = os.path.join(save_dir, f'{image_id}.jpg')
            
            # Save the image
            image.save(image_path)
            print(f"Image {image_id} downloaded successfully!")
        else:
            print(f"Failed to download image {image_id}: {response.status_code}")
    
    except Exception as e:
        print(f"Error downloading image {image_id}: {e}")

# Download all images
for index, row in df.iterrows():
    image_url = row['image_link']
    image_id = index  # Use the built-in index as the image identifier
  # Assuming 'index' is a unique identifier in your CSV
    download_images(image_url, image_id, image_dir)

# Function to visualize downloaded images
def visualize_images(image_dir, num_images=5):
    # Get a list of all image file names in the directory
    image_files = os.listdir(image_dir)[:num_images]
    
    plt.figure(figsize=(10, 10))
    
    # Display the first 'num_images' images
    for i, image_file in enumerate(image_files):
        img_path = os.path.join(image_dir, image_file)
        img = Image.open(img_path)
        
        plt.subplot(1, num_images, i + 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title(image_file)
    
    plt.show()

# Visualize a few of the downloaded images
visualize_images(image_dir, num_images=5)
