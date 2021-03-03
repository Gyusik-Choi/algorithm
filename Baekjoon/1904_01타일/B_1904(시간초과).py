import sys
sys.setrecursionlimit(1000000)


def fibonacci(n):
    if n in memo:
        return memo[n]
    memo[n] = (fibonacci(n - 2) + fibonacci(n - 1)) % 15746
    return memo[n]


N = int(input())
memo = {1: 1, 2: 2}
fibonacci(N)
print(memo[N])
