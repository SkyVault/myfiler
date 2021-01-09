#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List
from meta import MetaData


@dataclass()
class PdfMeta(MetaData):
    title: str
    description: str
    authors: List[str]
    tags: List[str]
