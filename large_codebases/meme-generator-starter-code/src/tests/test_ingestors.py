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
from QuoteEngine import TXTIngestor
from QuoteEngine import CSVIngestor
from QuoteEngine import DOCXIngestor
from QuoteEngine import PDFIngestor


TESTS_ROOT = (Path(__file__).parent.parent).resolve()
TEST_TXT_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesTXT.txt'
TEST_CSV_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesCSV.csv'
TEST_DOCX_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesDOCX.docx'
TEST_PDF_FILE = TESTS_ROOT / '_data' / 'DogQuotes'  / 'DogQuotesPDF.pdf'


class TestLoadNEOs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.txt_ingestor_output = TXTIngestor.parse(TEST_TXT_FILE)
        cls.csv_ingestor_output = CSVIngestor.parse(TEST_CSV_FILE)
        cls.docx_ingestor_output = DOCXIngestor.parse(TEST_DOCX_FILE)
        cls.pdf_ingestor_output = PDFIngestor.parse(TEST_PDF_FILE)

    def test_txt_ingestor(self):
        self.assertIsNotNone(self.txt_ingestor_output)
        self.assertIsInstance(self.txt_ingestor_output, List)
        self.assertIsInstance(self.txt_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.txt_ingestor_output),2)
        self.assertEqual(self.txt_ingestor_output[0].author, "Bork")

    def test_csv_ingestor(self):
        self.assertIsNotNone(self.csv_ingestor_output)
        self.assertIsInstance(self.csv_ingestor_output, List)
        self.assertIsInstance(self.csv_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.csv_ingestor_output),2)
        self.assertEqual(self.csv_ingestor_output[0].author, "Skittle")

    def test_docx_ingestor(self):
        self.assertIsNotNone(self.docx_ingestor_output)
        self.assertIsInstance(self.docx_ingestor_output, List)
        self.assertIsInstance(self.docx_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.docx_ingestor_output),4)
        self.assertEqual(self.docx_ingestor_output[0].author, "Rex")

    def test_pdf_ingestor(self):
        self.assertIsNotNone(self.pdf_ingestor_output)
        self.assertIsInstance(self.pdf_ingestor_output, List)
        self.assertIsInstance(self.pdf_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.pdf_ingestor_output),3)
        self.assertEqual(self.pdf_ingestor_output[0].author, "Fluffles")


if __name__ == '__main__':
    unittest.main()
