import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = [
    'angel1.jpeg', 'angel2.jpeg', 'angel3.jpeg', 
    'angel4.jpeg', 'angel5.jpeg', 'angel6.jpeg', 'angel7.jpeg'
]

images = []

print("Resizing images to match...")

# 1. Load the first image to get the "target size"
first_image = Image.open(filenames[0])
target_size = first_image.size  # This gets the (width, height)

for filename in filenames:
    # 2. Open each image with Pillow
    img = Image.open(filename)
    
    # 3. Force it to be the same size as the first one
    img_resized = img.resize(target_size)
    
    # 4. Convert it to a format imageio understands
    images.append(np.array(img_resized))

print("Creating GIF...")
iio.imwrite('angel_animation.gif', images, duration=150, loop=0)

print("Success! Your GIF is ready.")