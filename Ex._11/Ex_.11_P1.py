###### Auther: Tejas Vadgama K. ########

from PIL import Image
import numpy as np

# Load the image
img = Image.open(r'C:\Users\Admin\Downloads\Tej_44\MU.jpg')
img_array = np.array(img)

# Show image details
print("Image Size (Width x Height):", img.size)
print("Image Shape (Height, Width, Channels):", img_array.shape)
print("Min pixel value in Blue channel:", img_array[:, :, 2].min())
