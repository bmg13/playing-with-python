"""
Change images - Crop, Resize and alter Transparency

Important note:
 - There is a dependency of external library. To get it, the following command was used:
    a) pip install pillow

The image used is the same created in the script "3_Webscrape_image_and_save_it_locally" of this repository

"""

from PIL import Image

value =Image.open("gustavo_santaolalla_image.jpg")
value.size


# crop image using picture coordinates
value_cropped = value.crop((250,50,650,550))
value_cropped


# resize image
value_resized = value.resize((2000,500))
value_resized


# rotate 90 degrees
value_rotated = value.rotate(90)
value_rotated


#change image transparency
value.putalpha(120) # this value can be between 0 (not been seen) and 256 (original picture)
value

# return picture to original value
value.putalpha(256)
value