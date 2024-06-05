"""
This script tries to extract information from images using the exif library
"""

from exif import Image


with open("image", "rb") as image_file:
    image = Image(image_file)

for key in image.list_all():
    try:
        print(key, image[key])
    except Exception as e:
        pass
