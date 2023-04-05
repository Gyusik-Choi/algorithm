nums = [list(map(int, input().split())) for _ in range(9)]

max_num = nums[0][0]
max_i = 0
max_j = 0

for i, num_row in enumerate(nums):
    for j, num in enumerate(num_row):
        if num > max_num:
            max_num = num
            max_i = i
            max_j = j

print(max_num)
print(max_i + 1, max_j + 1)
