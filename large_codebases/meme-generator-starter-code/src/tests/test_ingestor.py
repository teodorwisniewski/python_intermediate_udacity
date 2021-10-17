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
import pathlib
import math
import unittest

from . import TXTIngestor

TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()
TEST_TXT_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesTXT.txt'
TEST_CAD_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'test-cad-2020.json'


class TestLoadNEOs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.txt_ingestor_output = TXTIngestor.parse(TEST_TXT_FILE)

    def test_approaches_contain_close_approaches(self):
        approach = self.get_first_approach_or_none()
        self.assertIsNotNone(approach)
        self.assertIsInstance(approach, CloseApproach)
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
