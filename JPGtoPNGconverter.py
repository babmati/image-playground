import os  # to use to grab the path
import sys## how to use sys to grap first and second argument
from PIL import Image, ImageFilter

# we had to install Pillow Libray

# grab first and second argument
image_folder= sys.argv[1]
output_folder= sys.argv[2]
# check if new exit and if not create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

## loop through Pokedex

for filename in os.listdir(image_folder):
    img= Image.open(f'{image_folder}{filename}')
    clean_name= os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done')
# Convert images to png
#save to the new
# folder


# total arguments


