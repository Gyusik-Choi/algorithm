def get_number_of_combination(n):
    number_of_combinations = 0
    for i in range(1, n):
        number_of_combinations += i

    return number_of_combinations


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

total = get_number_of_combination(N)
duplicate_cnt = [0] * (N + 1)
for num in nums:
    duplicate_cnt[num] += 1

total_number_of_combinations = get_number_of_combination(N)
for cnt in duplicate_cnt:
    if cnt > 1:
        total_number_of_combinations -= get_number_of_combination(cnt)

print(total_number_of_combinations)
