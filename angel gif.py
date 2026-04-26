import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = [
    'angel1.jpeg', 'angel2.jpeg', 'angel3.jpeg', 
    'angel4.jpeg', 'angel5.jpeg', 'angel6.jpeg', 'angel7.jpeg'
]

images = []

print("Resizing images to match...")

first_image = Image.open(filenames[0])
target_size = first_image.size  

for filename in filenames:

    img = Image.open(filename)
    
    img_resized = img.resize(target_size)
    
    images.append(np.array(img_resized))

print("Creating GIF...")
iio.imwrite('angel_animation.gif', images, duration=150, loop=0)

print("Success! Your GIF is ready.")