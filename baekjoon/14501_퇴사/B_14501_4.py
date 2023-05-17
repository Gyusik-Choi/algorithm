N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
for i in range(N):
    dp[i] = consult[i][1]

for i in range(1, N):
    for j in range(i):
        # 상담 불가능한 경우
        if i - j < consult[j][0]:
            continue

        # 수익이 기존 보다 더 작은 경우
        if consult[i][1] + dp[j] <= dp[i]:
            continue

        dp[i] = max(consult[i][1] + dp[j], dp[i])

answer = 0

for i in range(N):
    if i + consult[i][0] > N:
        continue

    answer = max(answer, dp[i])

print(answer)
