import sys


N = int(input())
nums = [0] * N
for i in range(N):
    num = int(sys.stdin.readline())
    nums[i] = num

nums = sorted(nums)
max_weight = 0
idx = 1
for i in range(len(nums) - 1, -1, -1):
    sums = nums[i] * idx
    idx += 1
    if max_weight < sums:
        max_weight = sums

print(max_weight)
