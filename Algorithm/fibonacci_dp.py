memo = {0: 0, 1: 1, 2: 1}


def memoization(num):
    if num in memo:
        return memo[num]
    memo[num] = memoization(num - 1) + memoization(num - 2)
    return memo[num]


n = int(input())
print(memoization(n))

