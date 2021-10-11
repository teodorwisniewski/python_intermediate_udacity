from abc import ABC, abstractmethod
from typing import List
import pathlib

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    allowed_exts = ["csv"]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        format = pathlib.Path(path).suffix[1:]
        if format in cls.allowed_exts:
            return True
        else:
            return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass



