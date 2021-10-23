from typing import List
import csv
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor allows to parse csv files"""

    allowed_exts = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        with open(path, "r") as f:
            quotes = []
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                body, author = row
                new_quote = QuoteModel(body.strip('"'), author)
                quotes.append(new_quote)

        return quotes
