"""Check that data can be ingested from different types of files.
To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_ingestors
"""
from pathlib import Path
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
from QuoteEngine import Ingestor


TESTS_ROOT = (Path(__file__).parent.parent).resolve()
TEST_TXT_FILE = TESTS_ROOT / "_data" / "DogQuotes" / "DogQuotesTXT.txt"
TEST_CSV_FILE = TESTS_ROOT / "_data" / "DogQuotes" / "DogQuotesCSV.csv"
TEST_DOCX_FILE = TESTS_ROOT / "_data" / "DogQuotes" / "DogQuotesDOCX.docx"
TEST_PDF_FILE = TESTS_ROOT / "_data" / "DogQuotes" / "DogQuotesPDF.pdf"
TEST_GENERAL_FILE = TESTS_ROOT / "_data" / "DogQuotes" / "DogQuotesPDF.pdf"


class TestQuoteEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.txt_ingestor_output = TXTIngestor.parse(TEST_TXT_FILE)
        cls.csv_ingestor_output = CSVIngestor.parse(TEST_CSV_FILE)
        cls.docx_ingestor_output = DOCXIngestor.parse(TEST_DOCX_FILE)
        cls.pdf_ingestor_output = PDFIngestor.parse(TEST_PDF_FILE)
        cls.general_ingestor_output = Ingestor.parse(TEST_PDF_FILE)

    def test_txt_ingestor(self):
        self.assertIsNotNone(self.txt_ingestor_output)
        self.assertIsInstance(self.txt_ingestor_output, List)
        self.assertIsInstance(self.txt_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.txt_ingestor_output), 2)
        self.assertEqual(self.txt_ingestor_output[0].author, "Bork")
        self.assertRaises(Exception, CSVIngestor.parse, TEST_TXT_FILE)

    def test_csv_ingestor(self):
        self.assertIsNotNone(self.csv_ingestor_output)
        self.assertIsInstance(self.csv_ingestor_output, List)
        self.assertIsInstance(self.csv_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.csv_ingestor_output), 2)
        self.assertEqual(self.csv_ingestor_output[0].author, "Skittle")
        self.assertRaises(Exception, CSVIngestor.parse, TEST_PDF_FILE)

    def test_docx_ingestor(self):
        self.assertIsNotNone(self.docx_ingestor_output)
        self.assertIsInstance(self.docx_ingestor_output, List)
        self.assertIsInstance(self.docx_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.docx_ingestor_output), 4)
        self.assertEqual(self.docx_ingestor_output[0].author, "Rex")
        self.assertRaises(Exception, DOCXIngestor.parse, TEST_PDF_FILE)

    def test_pdf_ingestor(self):
        self.assertIsNotNone(self.pdf_ingestor_output)
        self.assertIsInstance(self.pdf_ingestor_output, List)
        self.assertIsInstance(self.pdf_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.pdf_ingestor_output), 3)
        self.assertEqual(self.pdf_ingestor_output[0].author, "Fluffles")
        self.assertRaises(Exception, PDFIngestor.parse, TEST_DOCX_FILE)

    def test_ingestor(self):
        self.assertIsNotNone(self.general_ingestor_output)
        self.assertIsInstance(self.general_ingestor_output, List)
        self.assertIsInstance(self.general_ingestor_output[0], QuoteModel)
        self.assertEqual(len(self.general_ingestor_output), 3)
        self.assertEqual(self.general_ingestor_output[0].author, "Fluffles")
        self.assertEqual(Ingestor.parse("file.jpg"), [])


if __name__ == "__main__":
    unittest.main()
