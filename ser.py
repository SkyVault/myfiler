#!/usr/bin/env python3
import json


class Serial:
    """ NOTE(Dustin): This isn't recursive """
    def __str__(self):
        jobj = json.dumps(self.__dict__, indent=2)
        return jobj
