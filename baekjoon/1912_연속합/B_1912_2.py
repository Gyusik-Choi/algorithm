import sys


def get_max_subarray(numbers: list[int]) -> int:
    dp = [0] * len(numbers)
    dp[0] = numbers[0]
    for i in range(1, n):
        dp[i] = max(numbers[i] + dp[i - 1], numbers[i])
    return max(dp)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(get_max_subarray(nums))
