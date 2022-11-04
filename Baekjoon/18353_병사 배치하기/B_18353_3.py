# LIS
# 전투력 동일할 경우는?
import sys


def binary_search(start, end):
    if start == end:
        return end

    mid = (start + end) // 2
    if dp[mid] == soldier:
        return mid

    if dp[mid] < soldier:
        return binary_search(start, mid)
    return binary_search(mid + 1, end)


N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
dp = [soldiers[0]]

for i in range(1, len(soldiers)):
    soldier = soldiers[i]
    if dp[-1] > soldier:
        dp.append(soldier)
    elif dp[-1] < soldier:
        idx = binary_search(0, len(dp) - 1)
        dp[idx] = soldier

print(N - len(dp))

# 12
# 12 2 5 3 2 10 8 7 15 5 4 3
# => 5

# 1
# 1
# => 0
