def memoization(n):
    if n in memo:
        return memo[n]
    memo[n] = memoization(n - 1) + memoization(n - 5)
    return memo[n]


N = int(input())
memo = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}
for i in range(N):
    num = int(input())
    print(memoization(num))
