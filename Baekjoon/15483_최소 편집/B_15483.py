first_word = list(input())
second_word = list(input())

first_length = len(first_word)
second_length = len(second_word)

dp = [[0] * (second_length + 1) for _ in range(first_length + 1)]

for i in range(1, first_length + 1):
    dp[i][0] = dp[i - 1][0] + 1

for i in range(1, second_length + 1):
    dp[0][i] = dp[0][i - 1] + 1

for i in range(1, first_length + 1):
    for j in range(1, second_length + 1):
        if first_word[i - 1] == second_word[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[first_length][second_length])
