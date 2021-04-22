import sys


N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))

dic = {}
for idx, number in enumerate(sorted_nums):
    dic[number] = idx

for i, num in enumerate(nums):
    sys.stdout.write(str(dic[num]) + " ")
