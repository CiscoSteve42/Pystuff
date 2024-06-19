#!/usr/bin/python3

from PIL import Image
import piexif

def remove_metadata(image_path, output_path):
    image = Image.open(image_path)
    exif_dict = {}
    exif_bytes = piexif.dump(exif_dict)
    image_info = image.info
    image_info['exif'] = exif_bytes
    image.save(output_path, **image_info)

if __name__ == "__main__":
    image_path = input('Enter the Filename of the Image that You Want to Wipe. ')
    output_path = input('Enter Your Desired New Filename. ')
    remove_metadata(image_path, output_path)
