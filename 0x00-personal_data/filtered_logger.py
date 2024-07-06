#!/usr/bin/env python3
""" Use of regex in replacing occurrences of certain field values """

from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ Returns regex obfuscated log messages """
    for field in fields:
        message = re.sub(rf'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
