A = input()
B = input()

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(len(A) + 1):
    dp[i][0] = i

for i in range(len(B) + 1):
    dp[0][i] = i

for a in range(1, len(A) + 1):
    for b in range(1, len(B) + 1):
        if A[a - 1] == B[b - 1]:
            dp[a][b] = dp[a - 1][b - 1]
        else:
            dp[a][b] = min(dp[a][b - 1], dp[a - 1][b - 1], dp[a - 1][b]) + 1

print(dp[len(A)][len(B)])
