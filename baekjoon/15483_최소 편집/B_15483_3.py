A = input()
B = input()

dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

for i in range(len(A) + 1):
    dp[0][i] = i

for i in range(len(B) + 1):
    dp[i][0] = i

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if B[i - 1] == A[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

# print(dp[len(A)][len(B)])
# 인덱스 접근에 주의
# 위처럼 하면 런타임 에러(IndexError) 발생한다
print(dp[len(B)][len(A)])
