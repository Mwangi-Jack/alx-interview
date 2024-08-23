#!/usr/bin/python3
"""Make Change Problem"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    this method takes two arguments 'coins'-
    integer array and 'total'- integer and determines
    the fewest number of coins needed to meet a given
    amount 'total'
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        if total == 0:
            break

        count += total // coin
        total %= coin

    return count if total == 0 else -1
