def factorial_by_recursion(n):
    if n < 2:
        return 1
    return n * factorial_by_recursion(n - 1)


N = int(input())
print(factorial_by_recursion(N))
