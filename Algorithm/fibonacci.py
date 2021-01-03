# memo = {0: 0, 1: 1, 2: 1}
#
#
# def memoization(num):
#     if num in memo:
#         return memo[num]
#     memo[num] = memoization(num - 1) + memoization(num - 2)
#     return memo[num]
#
#
# n = int(input())
# print(memoization(n))


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    num = fibonacci(num - 1) + fibonacci(num - 2)
    return num


n = int(input())
print(fibonacci(n))
