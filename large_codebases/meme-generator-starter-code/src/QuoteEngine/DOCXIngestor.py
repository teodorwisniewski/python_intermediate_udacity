from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):

    allowed_exts = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(" - ")
                new_quote = QuoteModel(body.strip('"'), author.strip())
                quotes.append(new_quote)

        return quotes
