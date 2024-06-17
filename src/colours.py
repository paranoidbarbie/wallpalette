from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

def generate_palette(image_path, num_colors=5):
    # Load image
    image = Image.open(image_path)
    
    # Resize image to speed up processing
    image = image.resize((150, 150))
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Reshape the image array to a 2D array of pixels (3 color channels)
    reshaped_image_array = image_array.reshape(-1, 3)
    
    # Use KMeans to find the main colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(reshaped_image_array)
    
    # Get the main colors
    colors = kmeans.cluster_centers_
    
    # Convert the colors to int
    colors = colors.astype(int)
    
    # Display or save the color palette
    plt.figure(figsize=(8, 6))
    for idx, color in enumerate(colors):
        color_patch = np.zeros((100, 100, 3), dtype=np.uint8)
        color_patch[:, :, :] = color
        plt.subplot(1, num_colors, idx + 1)
        plt.imshow(color_patch)
        plt.axis('off')
        plt.title(f'RGB: {color}')
    
    plt.show()

# Example usage:
image_path = os.path.join("/home/yoru/Projects/python/colourApp/tests", "testimage.png")  # Replace with your image file path
generate_palette(image_path)
