"""Module that defines an MemeEngine class."""
import os
from typing import Union
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """This class allows to load an image and add a text to it in order to create a meme."""

    def __init__(self, path: Union[str, bytes, os.PathLike]):
        """Init method for MemeEngine class."""
        self.path = path
        self.img = Image.open(self.path)

    def make_meme(
        self,
        img_path: Union[str, bytes, os.PathLike],
        text: str,
        author: str,
        width: int = 500,
    ) -> str:
        """Manipulate a given image:  resize, add a quote and save.

        @param img_path: output path of a generated meme
        @param text: content of a meme
        @param author: meme's author
        @param width: width of a the meme
        @return: path to the output image file
        """
        self.img.show()
        # resizing the image
        ratio = width / float(self.img.size[0])
        height = int(ratio * float(self.img.size[1]))
        img = self.img.resize((width, height), Image.NEAREST)
        img.show()
        # adding a quote to the image
        new_height = img.height
        font_size = int(new_height/15)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("../fonts/LilitaOne-Regular.ttf", size=font_size)
        draw.text((30, 50), text, font=font, fill="red")
        img.show()
        # saving output image file
        filename_basename = os.path.basename(self.path)
        new_filename = filename_basename.split(".")[0] + f"_{random.randint(0,1000000)}_with_quote.jpg"
        output_path = os.path.join(img_path, new_filename)
        img.save(output_path)

        return output_path
