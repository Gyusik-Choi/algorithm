def factorial(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = n * factorial(n - 1)
        return memo[n]


N = int(input())
memo = {0: 1, 1: 1, 2: 2}
print(factorial(N))
