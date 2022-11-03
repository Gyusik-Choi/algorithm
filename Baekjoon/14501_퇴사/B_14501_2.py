def get_max_value_from_past(idx):
    max_val = 0
    for j in range(idx):
        if j + schedule[j][0] <= idx:
            max_val = max(max_val, dp[j])

    return max_val


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
for i in range(N):
    dp[i] = schedule[i][1]

answer = 0
for i in range(N):
    dp[i] += get_max_value_from_past(i)

    if N - i >= schedule[i][0]:
        answer = max(answer, dp[i])

print(answer)

# 반례
# 1
# 1 10
# => 10
