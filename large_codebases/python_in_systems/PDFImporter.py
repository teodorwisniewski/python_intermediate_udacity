from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from .Cat import Cat

class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        cats = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(',')
                new_cat = Cat(parsed[0],
                              int(parsed[1]),
                              bool(parsed[2]))
                cats.append(new_cat)

        file_ref.close()
        os.remove(tmp)
        return cats