"""Check that meme can be generated.
To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_MemeEngine
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFile
import unittest
import sys
import os
from tempfile import TemporaryDirectory


project_path = Path(os.getcwd()) / "src"
sys.path.append(str(project_path))

from MemeEngine import MemeEngine


TESTS_ROOT = (Path(__file__).parent.parent).resolve()
PHOTO1_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_1.jpg"
PHOTO2_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_2.jpg"
PHOTO3_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /   "xander_3.jpg"
PHOTO4_FILE = TESTS_ROOT / "_data" / "photos" / "dog" /  "xander_4.jpg"


class TestMemeEngine(unittest.TestCase):

    def test_make_meme(self):
        with TemporaryDirectory() as tmpdir:
            meme_gen = MemeEngine(tmpdir)
            output_path = meme_gen.make_meme(PHOTO1_FILE, "tested quote", "random author")
            self.assertEqual(os.path.isfile(output_path), True)
        self.assertIsInstance(meme_gen.img, Image.Image)

if __name__ == "__main__":
    unittest.main()



