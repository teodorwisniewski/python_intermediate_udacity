from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):

    allowed_exts = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        quotes = []

        with open(path, "r") as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    body, author = line.split('-')
                    new_quote = QuoteModel(body.strip().strip('"'), author.strip())
                    quotes.append(new_quote)

        return quotes
