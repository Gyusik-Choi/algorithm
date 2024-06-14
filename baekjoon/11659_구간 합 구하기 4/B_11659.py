import sys


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
ranges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

sums = 0
acc_sums = [0] * (N + 1)
for idx, num in enumerate(nums):
    sums += num
    acc_sums[idx + 1] = sums

answer = []
for i, j in ranges:
    answer.append(str(acc_sums[j] - acc_sums[i - 1]) + "\n")
sys.stdout.write(''.join(answer))

# 참고
# https://www.acmicpc.net/board/view/131282
# https://wikidocs.net/206300
