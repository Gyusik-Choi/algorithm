N = int(input())
schedule = []
for _ in range(N):
    t, p = map(int, input().split())
    schedule.append([t, p])

# 초기값을 일단 넣어서 dp 를 계산할때 반영될 수 있도록 하고
# 추후에 최대값을 구할때 조건에 맞는 값만 최대값 연산에 포함한다
dp = [0] * N
for i in range(N):
    dp[i] = schedule[i][1]

for i in range(1, N):
    for j in range(i):
        if i - j >= schedule[j][0]:
            dp[i] = max(dp[i], dp[j] + schedule[i][1])

max_sums = 0
for i in range(N):
    if i + schedule[i][0] < N + 1:
        max_sums = max(max_sums, dp[i])

print(max_sums)

# 참고
# https://mygumi.tistory.com/151
