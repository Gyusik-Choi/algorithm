import sys


N = int(input())
wires = []
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    wires.append(nums)

# 전깃줄을 왼쪽 전봇대를 기준으로 정렬
wires = sorted(wires, key=lambda x: x[0])
dp = [1] * N

# LIS
max_num = dp[0]
for i in range(1, N):
    right_num = wires[i][1]
    for j in range(i - 1, -1, -1):
        left_num = wires[j][1]
        if right_num > left_num:
            dp[i] = max(dp[i], dp[j] + 1)

    if max_num < dp[i]:
        max_num = dp[i]

answer = N - max_num
print(answer)

# 참고
# https://sihyungyou.github.io/baekjoon-2565/
