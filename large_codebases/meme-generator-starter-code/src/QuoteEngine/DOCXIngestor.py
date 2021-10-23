"""Module that define an ingestor for docx files."""
from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """DOCXIngestor allows to parse docx files."""

    allowed_exts = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method that allows to parse docx files.

        @param path: path to a docx file.
        @return: list of QuoteModel objects
        """
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
