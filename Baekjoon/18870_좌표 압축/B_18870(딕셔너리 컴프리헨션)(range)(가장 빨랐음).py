import sys


N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))

dic = {sorted_nums[i]: i for i in range(len(sorted_nums))}

for i in range(len(nums)):
    sys.stdout.write(str(dic[nums[i]]) + " ")
