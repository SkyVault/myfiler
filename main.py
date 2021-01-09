#!/usr/bin/env python3

from typing import Final
from os import path, walk
from pdf import PdfMeta

MEDIA_DIR: Final = "/home/dustin/Media/"
META_DATA: Final = path.join(MEDIA_DIR, "media-db.json")


def generateFreshDatabase():
    res = {}
    cur = META_DATA
    for (dpath, dnames, fnames) in walk(cur):
        print(dpath, dnames, fnames)


if __name__=="__main__":
    # with open(META_DATA, "rb") as f:
    #     lines = f.readlines()
    #     print(lines)

    generateFreshDatabase()
