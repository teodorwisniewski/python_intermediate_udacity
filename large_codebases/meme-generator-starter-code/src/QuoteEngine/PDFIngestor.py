import subprocess
from typing import List
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from tempfile import TemporaryDirectory
from QuoteEngine import TXTIngestor


class PDFIngestor(IngestorInterface):

    allowed_exts = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        with TemporaryDirectory() as tmpdir:
            tmp = os.path.join(tmpdir, "file.txt")
            call = subprocess.call(["pdftotext", "-layout", path, tmp])
            quotes = TXTIngestor.parse(tmp)

        return quotes
