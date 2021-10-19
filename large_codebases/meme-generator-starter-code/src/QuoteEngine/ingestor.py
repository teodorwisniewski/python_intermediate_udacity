from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor
from .DOCXIngestor import DOCXIngestor


class Ingestor(IngestorInterface):
    allowed_ingestors = [CSVIngestor, TXTIngestor, PDFIngestor, DOCXIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        for ingestor in cls.allowed_ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)

        return quotes
