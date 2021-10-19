"""Check that data can be extracted from structured data files.

The `load_neos` function should load a collection of `NearEarthObject`s from a
CSV file, and the `load_approaches` function should load a collection of
`CloseApproach` objects from a JSON file.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_extract

These tests should pass when Task 2 is complete.
"""
import collections.abc
import datetime
from pathlib import Path
import math
from typing import List
import unittest
import sys
import os


project_path = Path(os.getcwd()) / "src"
sys.path.append(str(project_path))

from QuoteEngine import QuoteModel
from QuoteEngine.TXTIngestor import TXTIngestor

TESTS_ROOT = (Path(__file__).parent.parent).resolve()
TEST_TXT_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesTXT.txt'
TEST_CAD_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesCSV.csv'


class TestLoadNEOs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.txt_ingestor_output = TXTIngestor.parse(TEST_TXT_FILE)

    def test_approaches_contain_close_approaches(self):
        self.assertIsNotNone(self.txt_ingestor_output)
        self.assertIsInstance(self.txt_ingestor_output, List)
        self.assertIsInstance(self.txt_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.txt_ingestor_output),2)


if __name__ == '__main__':
    unittest.main()
