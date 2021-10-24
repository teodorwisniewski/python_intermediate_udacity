"""Module that defines an MemeEngine class."""
import os
import sys
from typing import Union
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """This class allows to load an image and add a text to it in order to create a meme."""

    def __init__(self, output_path: Union[str, bytes, os.PathLike]):
        """Init method for MemeEngine class."""
        self.output_path = output_path

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
        try:
            self.img = Image.open(img_path)
            # resizing the image
            ratio = width / float(self.img.size[0])
            height = int(ratio * float(self.img.size[1]))
            self.img = self.img.resize((width, height), Image.NEAREST)
            # adding a quote to the image
            new_height = self.img.height
            font_size = int(new_height / 15)
            draw = ImageDraw.Draw(self.img)
            font = ImageFont.truetype("../fonts/LilitaOne-Regular.ttf", size=font_size)
            x_loc, y_loc = 30, 50
            draw.text((x_loc, y_loc), text, font=font, fill="red")
            draw.text((int(x_loc * 1.25), y_loc + font_size), " - " + author, font=font, fill="red")
            # saving output image file
            filename_basename = os.path.basename(img_path)
            new_filename = (
                filename_basename.split(".")[0]
                + f"_{random.randint(0,1000000)}_with_quote.jpg"
            )
            output_path = os.path.join(self.output_path, new_filename)
            self.img.save(output_path)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print("The image cannot be opened")
            output_path = None

        return output_path
