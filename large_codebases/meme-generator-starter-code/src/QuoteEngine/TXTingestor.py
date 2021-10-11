import subprocess
from typing import List
import pathlib
import random
import os

from .ingestor import IngestorInterface
from .quote_model import QuoteModel


class TXTIngestor(IngestorInterface):

    allowed_exts = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(',')
                new_cat = QuoteModel(parsed[0],
                              int(parsed[1]),
                              bool(parsed[2])
                              )
                quotes.append(new_cat)

        return quotes
