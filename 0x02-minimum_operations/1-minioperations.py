#!/usr/bin/env python3

"""Minimum Operations"""
import time
from typing import List
import timeit
import cProfile


def get_prime_numbers(limit: int) -> List[int]:
    """
    This function takes in an intager value 'n'
    and retuns an array of prime numbers between 2 and 'n'
    """
    is_prime = [True] * (limit + 1)
    p = 2

    while p ** 2 <= limit:
        if is_prime[p]:
            for i in range(p ** 2, limit + 1, p):
                is_prime[i] = False
        p += 1

    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]

    return prime_numbers


def minOperations(n: int) -> int:
    """
    This function takes an intager value 'n' and
    calculates the sum of its prime factors
    """
    prime_numbers = get_prime_numbers(n)

    prime_factors = []

    p = n

    while p not in prime_numbers:
        for i in prime_numbers:
            if p  % i == 0:
                p = p // i
                prime_factors.append(i)
                break

    prime_factors.append(p)
    return sum(prime_factors)


# print(timeit.timeit(minOperations(12)))
cProfile.run("minOperations(10000000)")

start = time.perf_counter()
minOperations(10000000)
stop = time.perf_counter()

print("Total Execution time", stop - start)
