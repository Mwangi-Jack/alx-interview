#!/usr/bin/python3
"""Prime Game"""


def get_primes(limit):
    """gets prime numbers"""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for mul in range(i * i, limit + 1, i):
                primes[mul] = False

    return primes


def count_prime_moves(n, primes):
    """counts the prime moves made by players"""
    moves = 0
    removed = [False] * (n + 1)

    for i in range(2, n + 1):
        if primes[i] and not removed[i]:
            moves += 1
            for mul in range(i, n + 1, i):
                removed[mul] = True

    return moves


def isWinner(x, nums):
    """gets the winner"""
    nums = nums[:x]
    max_n = max(nums)
    primes = get_primes(max_n)

    fixtures = {'maria': 0, 'ben': 0}

    for n in nums:
        prime_moves = count_prime_moves(n, primes)

        if prime_moves % 2 == 1:
            fixtures['maria'] += 1
        else:
            fixtures['ben'] += 1

    if fixtures['ben'] > fixtures['maria']:
        return 'Ben'
    else:
        return 'Maria'
