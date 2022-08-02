memo = {0: 0, 1: 1, 2: 1}


def fibonacci(a):
    if a in memo:
        return memo[a]
    memo[a] = fibonacci(a - 2) + fibonacci(a - 1)
    return memo[a]


n = int(input())
print(fibonacci(n))
