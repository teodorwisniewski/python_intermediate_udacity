from PIL import Image
from pathlib import Path
import os


def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    if not out_path:
        output_path = "./"
    if not os.path.exists(in_path):
        raise Exception("File not found")

    with Image.open(in_path) as img:
        width, height = img.size
        (left, upper, right, lower) = (3*width/9, 3*height/9, 6*width/9, 5*height/9)
        im_crop = img.crop((left, upper, right, lower))
        width, height = im_crop.size
        new_image = im_crop.resize((width*2, height*2))
        out_path = os.path.join(out_path, "outputimage.jpg")
        new_image.save(out_path)

    return out_path

if __name__=='__main__':
    print(generate_postcard('./imgs/img.jpg', './imgs/'))
