"""The main ingestor module."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor
from .DOCXIngestor import DOCXIngestor


class Ingestor(IngestorInterface):
    """
        Ingestor class that encapsulates helper classes.
        It is defined for different file formats.
    """

    allowed_ingestors = [CSVIngestor, TXTIngestor, PDFIngestor, DOCXIngestor]
    allowed_exts = ["docx", "csv", "pdf", "txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse method to parse files and return a list of quote model objects.

        @param path: path to a file.
        @return: list of QuoteModel objects
        """
        quotes = []
        for ingestor in cls.allowed_ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)

        return quotes
