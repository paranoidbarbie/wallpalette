from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os
from random import shuffle

def generate_palette(image_path=os.path.join(f"{os.getcwd()}/tests/", "testimage.png"), num_colors=18):
    image = Image.open(image_path)
    image = image.resize((150, 150))
    image_array = np.array(image)
    reshaped_image_array = image_array.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(reshaped_image_array)
    colors = kmeans.cluster_centers_
    colors = colors.astype(int)
    return colors

if __name__ == "__main__":
    generate_palette()
