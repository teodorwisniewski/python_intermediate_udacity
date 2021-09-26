from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os


def find_font_size(text, font, image, target_width_ratio):
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = tested_font_size / (observed_width / image.width) * target_width_ratio
    return round(estimated_font_size)

def get_text_size(text, image, font):
    im = Image.new('RGB', (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)

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

        draw = ImageDraw.Draw(new_image)
        text = 'woof!!!'
        width_ratio = 0.5  # Portion of the image the text width should be (between 0 and 1)
        font_family = "arial.ttf"
        font_size = find_font_size(text, font_family, new_image, width_ratio)
        font = ImageFont.truetype(font_family, int(font_size*1.3))
        draw.text((width/5, height/5), text, font=font, fill ="red")
        new_image.show()
        out_path = os.path.join(out_path, "outputimage.jpg")
        new_image.save(out_path)

    return out_path

if __name__=='__main__':
    print(generate_postcard('./imgs/img.jpg', './imgs/'))
