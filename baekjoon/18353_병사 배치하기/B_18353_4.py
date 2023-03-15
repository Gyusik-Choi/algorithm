import sys


def binary_search(low, high, target):
    while low < high:
        mid = (low + high) // 2

        if dp[mid] <= target:
            high = mid
        else:
            low = mid + 1

    return low


N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
dp = [soldiers[0]]

for i in range(1, N):
    soldier = soldiers[i]

    if dp[-1] > soldier:
        dp.append(soldier)
    else:
        idx = binary_search(0, len(dp) - 1, soldier)
        dp[idx] = soldier

print(N - len(dp))

# 12
# 12 2 5 3 2 10 8 7 15 5 4 3
# => 5
