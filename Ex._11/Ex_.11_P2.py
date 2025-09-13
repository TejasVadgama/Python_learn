from PIL import Image, ImageOps

img = Image.open(r'C:\Users\Admin\Downloads\Tej_44\MU.jpg')

# Add 50 pixel black border
padded_img = ImageOps.expand(img, border=50, fill='black')

padded_img.show()
