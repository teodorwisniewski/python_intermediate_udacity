"""Module that define an ingestor for pdf files."""
import subprocess
from typing import List
from tempfile import TemporaryDirectory
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class PDFIngestor(IngestorInterface):
    """PDFIngestor allows to parse pdf files."""

    allowed_exts = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method that allows to parse pdf files.

        @param path: path to a pdf file.
        @return: list of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        with TemporaryDirectory() as tmpdir:
            tmp = os.path.join(tmpdir, "file.txt")
            call = subprocess.call(["pdftotext", "-layout", path, tmp])
            quotes = TXTIngestor.parse(tmp)

        return quotes
