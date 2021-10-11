import subprocess
from typing import List
import pathlib
import random
import os
from .ingestor import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):

    allowed_exts = ["pdf"]


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        cats = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)

        file_ref.close()
        os.remove(tmp)
        return cats
