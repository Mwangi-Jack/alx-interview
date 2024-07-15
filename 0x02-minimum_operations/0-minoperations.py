#!/usr/bin/env python3

"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    This function takes in an int variable 'n'
    and returns an integer value i.e the minimum number of
    operations needed (copy and or paste) to result to n characters
    of 'H'
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
