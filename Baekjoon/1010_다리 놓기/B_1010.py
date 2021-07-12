import sys


def factorial(n):
    number = 1
    if n > 0:
        for i in range(1, n + 1):
            number *= i
    return number


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    ans = factorial(M) // factorial(N) // factorial(M - N)
    sys.stdout.write(str(ans) + "\n")
