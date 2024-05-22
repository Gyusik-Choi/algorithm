n = int(input())

dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n - 1])

# 참고
# https://coco-peter.tistory.com/53
# jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=597&sca=50&sfl=wr_subject&stx=%EB%AA%BB%EC%83%9D%EA%B8%B4&sop=and

# 0
# 0 0 0
# 2 3 5
# [1]

# 1
# 1 0 0
# 4 3 5
# [1, 2]

# 2
# 1 1 0
# 4 6 5
# [1, 2, 3]

# 3
# 2 1 0
# 6 6 5
# [1, 2, 3, 4]

# 4
# 2 1 1
# 6 6 10
# [1, 2, 3, 4, 5]

# 5
# 3 2 1
# 8 9 10
# [1, 2, 3, 4, 5, 6]
# 앞선 6 6 10 에서 dp[5] 인 6이
# next2, next3 와 같아서
# 2번 곱한다
# next2 = dp[i2] * 2
# next3 = dp[i3] * 3

# 6
# 4 2 1
# 16 9 10
# [1, 2, 3, 4, 5, 6, 8]
