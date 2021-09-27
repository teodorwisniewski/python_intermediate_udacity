from abc import ABC, abstractmethod
from .Cat import Cat
from typing import List


class ImporterInterface(ABC):
    allowed_exts = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split(".")[-1]
        return ext in cls.allowed_exts

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Cat]:
        pass
