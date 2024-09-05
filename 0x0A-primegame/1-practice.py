#!/usr/bin/python3
"""Find Prime Numbers"""


def get_primes(n):
    """Returns prime numbers between 1 and n included"""

    if n < 2: return 1

    marks = [True] * (n -1)
    print(marks)

    p = 2

    for i in range(2, n -1):
        if marks[p] is False: continue

        if i % 2 == 0 or i >= (p**2):
            marks[i] = False

        p = p + 1
        print(p)

    print(marks)
    return [i for i in range(2, len(marks)) if marks[i] is True]


print(get_primes(11))
