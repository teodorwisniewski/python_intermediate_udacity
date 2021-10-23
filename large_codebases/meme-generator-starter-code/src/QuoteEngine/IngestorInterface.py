from abc import ABC, abstractmethod
from typing import List
import pathlib

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    "Abstract base class for ingestors classes"
    allowed_exts = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        "this method will check whether a file can be parsed or not"
        format = pathlib.Path(path).suffix[1:].lower()
        return format in cls.allowed_exts

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        "abstract method for parsing a given type of file"
        pass
