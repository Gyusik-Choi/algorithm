import sys


def binary_search(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2

    if dp[mid] < target:
        return binary_search(start, mid, target)
    else:
        # 값이 같을 경우 덮어쓰도록 한다
        if dp[mid] == target:
            return mid
        return binary_search(mid + 1, end, target)


N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))

dp = [soldiers[0]]

for i in range(1, N):
    if dp[-1] > soldiers[i]:
        dp.append(soldiers[i])
    else:
        if dp[-1] < soldiers[i]:
            # end 는 dp 길이의 - 1
            idx = binary_search(0, len(dp) - 1, soldiers[i])
            dp[idx] = soldiers[i]

dp_length = len(dp)
print(N - dp_length)

# 반례
# 4
# 4 4 4 4
# => 3

# 5
# 3 4 5 6 1
# => 3

# 6
# 1 2 1 2 1 2
# => 4