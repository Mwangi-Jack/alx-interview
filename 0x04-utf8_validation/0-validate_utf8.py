#!/usr/bin/python3
"""UFT-8 Validation"""

from typing import List


# def validUTF8(data: List[int]) -> bool:
#     """
#     This method takes in a list of integer values 'data'
#     and validates if its a UFT8 encoded  or not returning a
#     boolean
#     """
#     for enc in data:
#         if enc >= 255:
#             return False

#     return True


def validUTF8(data):
    """
    This method takes in a list of integer values 'data'
    and validates if its a UFT8 encoded  or not returning a
    boolean
    """
    def check_following_bytes(data, start, num_bytes):
        for i in range(start + 1, start + num_bytes):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        byte = data[i]
        if byte >> 7 == 0:
            num_bytes = 1
        elif byte >> 5 == 0b110:
            num_bytes = 2
        elif byte >> 4 == 0b1110:
            num_bytes = 3
        elif byte >> 3 == 0b11110:
            num_bytes = 4
        else:
            return False

        if not check_following_bytes(data, i, num_bytes):
            return False

        i += num_bytes

    return True
