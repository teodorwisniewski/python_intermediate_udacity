"""Module that defines an abstract base class for ingestors."""
from abc import ABC, abstractmethod
from typing import List
import pathlib

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for ingestors helper classes."""

    allowed_exts = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
            Can_ingest method for checking whether a file can be parsed or not.
        """
        format = pathlib.Path(path).suffix[1:].lower()
        return format in cls.allowed_exts

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parsing a given type of file."""
        pass
