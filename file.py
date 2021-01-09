#!/usr/bin/env python3
from ser import Serial
from dataclasses import dataclass
from enum import Enum, auto


class FileType(Enum):
    TEXT = auto()
    PDF = auto()
    MUSIC = auto()


@dataclass
class MediaFile(Serial):
    mediaType: FileType
    name: str
    meta: MetaData
