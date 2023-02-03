# LIS
# 전투력 동일할 경우는?
import sys


def binary_search(start, end):
    if start == end:
        return end

    mid = (start + end) // 2
    if dp[mid] == soldier:
        return mid

    # 왼쪽 더 갈 수 있는지
    if dp[mid] < soldier:
        if mid > 0:
            if dp[mid - 1] < soldier:
                return binary_search(start, mid - 1)
            elif dp[mid - 1] == soldier:
                return mid - 1
        return mid
    # 오른쪽 더 갈 수 있는지
    else:
        if mid < len(dp) - 1:
            if dp[mid + 1] > soldier:
                return binary_search(mid + 1, end)
        return mid + 1


N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
dp = [soldiers[0]]

for i in range(1, len(soldiers)):
    soldier = soldiers[i]
    if dp[-1] > soldier:
        dp.append(soldier)
    else:
        if dp[-1] < soldier:
            idx = binary_search(0, len(dp) - 1)
            dp[idx] = soldier

print(N - len(dp))

# 12
# 12 2 5 3 2 10 8 7 15 5 4 3
# => 5

# 1
# 1
# => 0
