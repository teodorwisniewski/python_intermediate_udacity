from abc import ABC, abstractmethod
from typing import List
import pathlib

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    allowed_exts = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        format = pathlib.Path(path).suffix[1:]
        format in cls.allowed_exts


    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass



