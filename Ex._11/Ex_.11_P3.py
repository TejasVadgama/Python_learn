import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load image
img = Image.open(r'C:\Users\Admin\Downloads\Tej_44\MU.jpg')
img_array = np.array(img)

# Split channels
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Show each channel
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(G, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(B, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.tight_layout()
plt.show()
