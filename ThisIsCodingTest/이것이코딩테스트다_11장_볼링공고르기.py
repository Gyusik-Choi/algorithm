def get_number_of_combination(n):
    number_of_combinations = 0
    for i in range(1, n):
        number_of_combinations += i

    return number_of_combinations


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

total = get_number_of_combination(N)

current_num = nums[0]
duplicate_cnt = []
temp_count = 1
for j in range(1, N):
    if current_num == nums[j]:
        temp_count += 1
    else:
        if temp_count > 1:
            duplicate_cnt.append(temp_count)
        current_num = nums[j]
        temp_count = 1

# 마지막에 더해지기만 하고
# duplicate_count 에 넣지 못한 경우에 넣어준다
if temp_count > 1:
    duplicate_cnt.append(temp_count)

total_number_of_combinations = get_number_of_combination(N)
for cnt in duplicate_cnt:
    total_number_of_combinations -= get_number_of_combination(cnt)

print(total_number_of_combinations)
