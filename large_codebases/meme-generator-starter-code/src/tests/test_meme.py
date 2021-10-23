"""Check that meme parser works.
To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_meme
"""
from pathlib import Path
import unittest
import sys
import os
from tempfile import TemporaryDirectory


project_path = Path(os.getcwd()) / "src"
sys.path.append(str(project_path))

from meme import parse_args, generate_meme


TESTS_ROOT = (Path(__file__).parent.parent).resolve()
PHOTO1_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_1.jpg"
PHOTO2_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_2.jpg"
PHOTO3_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /   "xander_3.jpg"
PHOTO4_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_4.jpg"


class TestMemeParser(unittest.TestCase):

    def test_make_meme(self):
        quote = "if you can't dazzle them with your brilliance, blind them with bullshit"
        author = "W.C. Fields"
        args = ["--path",str(PHOTO1_FILE), "--body", quote, "--author", author]
        parser = parse_args(args)
        output_path = generate_meme(path=parser.path, body=parser.body, author=parser.author)
        self.assertEqual(os.path.isfile(output_path), True)


if __name__ == "__main__":
    unittest.main()
