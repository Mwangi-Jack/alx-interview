#!/usr/bin/env python3

"""Using Sieve Eratosthenes Algorithm"""

from typing import List


def get_prime_numbers(limit: int)-> List[int]:
    """
    This function takes int an integer 'limit'
    and returns a list of prime numbers from
    0 to the 'limit'
    """

    true_list = [True] * (limit + 1)

    p = 2

    while p * p <= limit:
        if true_list[p]:
            for i in range(p ** p, limit + 1, p):
                true_list[i] = False
        p += 1

    prime_numbers = [p for p in range(2, limit + 1) if true_list[p]]


    print(prime_numbers)
    print(true_list)

    return prime_numbers


get_prime_numbers(10)
