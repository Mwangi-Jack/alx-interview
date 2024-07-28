#!/usr/bin/python3
"""Get prime numbers using sieve algorithim"""

from typing import List


def get_prime_nums(n: int) -> List[int]:
    """
    This function takes in an integer 'n' and returns
    a list of prime numbers from 0 to 'n'
    """
    tt = [True]* (n + 1)

    a = 2

    while a * a <= n:
        if tt[a]:
            for i in range(a *  a, n + 1, a):
                tt[i] = False
        a += 1

    print([i for i in range(2, n) if tt[i]])
    print(tt)
    return [i for i in range(2, n + 1) if tt[i]]


get_prime_nums(10)
