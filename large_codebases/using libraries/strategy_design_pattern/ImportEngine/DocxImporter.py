from .ImportInterface import ImporterInterface
from typing import List
from .Cat import Cat
import docx


class DocxImporter(ImporterInterface):
    allowed_exts = "docs"

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if cls.can_ingest(path):
            raise Exception(f"Extension is not allowed")

        cats = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(',')
                new_cat = Cat(parsed[0],
                              int(parsed[1]),
                              bool(parsed[2])
                              )
                cats.append(new_cat)

        return cats