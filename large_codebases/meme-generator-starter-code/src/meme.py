"""Module that defines how to create a new meme."""
import os
import random
import argparse
import pathlib
import sys
from typing import Union
from pathlib import Path

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine

root_directory = Path(__file__).parent.resolve()


def generate_meme(path=None, body=None, author=None) -> Union[str, bytes, os.PathLike]:
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        imgage_path = random.choice(imgs)
    else:
        imgage_path = path

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine(root_directory / "tmp")
    path = meme.make_meme(imgage_path, quote.body, quote.author)
    return path


def is_valid_file(path: Union[str, bytes, os.PathLike]) -> bool:
    """Check if a path represents an existing file."""
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError(path)


def parse_args(args):
    """Parse argument function. This function is created for testing purposes."""
    parser = argparse.ArgumentParser(
        description="Create a meme with a quote and cute dog."
    )

    # Add arguments for custom data files.
    parser.add_argument(
        "--path",
        default=None,
        type=is_valid_file,
        help="path to the image file",
    )
    parser.add_argument(
        "--body",
        default=None,
        type=str,
        help="quote's body to add to the image",
    )
    parser.add_argument(
        "--author",
        default=None,
        type=str,
        help="quote's author to add to the image",
    )
    return parser.parse_args(args)


if __name__ == "__main__":

    PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
    DATA_ROOT = PROJECT_ROOT / "data"

    args = parse_args(sys.argv[1:])
    print(generate_meme(args.path, args.body, args.author))
