"""Module that defines an MemeEngine class."""
import os
import sys
from typing import Union
import random
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap

root_directory = Path(__file__).parent.parent.resolve()


class MemeEngine:
    """
        This class allows to load an image.
        Then it adds a text to it in order to create a meme.
    """

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
        self.img = Image.open(img_path)
        # resizing the image
        ratio = width / float(self.img.size[0])
        height = int(ratio * float(self.img.size[1]))
        self.img = self.img.resize((width, height), Image.NEAREST)
        # adding a quote to the image
        new_height = self.img.height
        font_size = int(new_height / 12)
        draw = ImageDraw.Draw(self.img)
        font_path = root_directory / "fonts/CollegiateFLF.ttf"
        font = ImageFont.truetype(str(font_path), size=font_size)
        y_loc = random.randint(0, 100)  # random location of the quote
        lines = textwrap.wrap(f'"{text}" - {author}', width=18)
        for line in lines:
            line_width, line_height = font.getsize(line)
            x_loc = (width - line_width) / 2
            draw.text((x_loc, y_loc), line, font=font, fill="white")
            y_loc += line_height
        # saving output image file
        filename_basename = os.path.basename(img_path)
        new_filename = (
            filename_basename.split(".")[0]
            + f"_{random.randint(0,1000000)}_with_quote.jpg"
        )
        output_path = os.path.join(self.output_path, new_filename)
        self.img.save(output_path)

        return output_path
