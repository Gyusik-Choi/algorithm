import sys


def get_max_subarray(numbers: list[int]) -> int:
    for i in range(1, len(numbers)):
        numbers[i] = max(numbers[i], numbers[i - 1] + numbers[i])
    return max(numbers)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(get_max_subarray(nums))
