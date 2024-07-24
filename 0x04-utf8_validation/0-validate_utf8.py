#!/usr/binpython3
"""UFT-8 Validation"""

from typing import List


def validUTF8(data:List[int]) -> bool:
    """
    This method takes in a list of integer values 'data'
    and validates if its a UFT8 encoded  or not returning a
    boolean
    """
    for enc in data:
        if enc > 255:
            return False

    return True
