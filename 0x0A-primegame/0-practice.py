'''Practising Memoization'''

memo = {}

def fibonacciVal(n):
    """Calculates fibonacci"""
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibonacciVal(6))
