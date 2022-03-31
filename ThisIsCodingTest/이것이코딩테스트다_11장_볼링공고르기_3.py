N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums_cnt = [0] * (N + 1)

for num in nums:
    nums_cnt[num] += 1

total = 0
for cnt in nums_cnt:
    N -= cnt
    total += N * cnt

print(total)

# 5 3
# 1 3 2 3 2
# => 8

# 8 5
# 1 5 4 3 2 4 5 2
# => 25
