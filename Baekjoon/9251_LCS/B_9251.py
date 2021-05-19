first_word = input()
second_word = input()

max_num = 0
dp = [[0] * len(second_word) for _ in range(len(first_word))]
for i in range(len(first_word)):
    first_item = first_word[i]
    for j in range(len(second_word)):
        second_item = second_word[j]
        if first_item == second_item:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        if dp[i][j] > max_num:
            max_num = dp[i][j]

print(max_num)