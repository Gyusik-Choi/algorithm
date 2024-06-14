import sys


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
ranges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
answer = [str(sum(nums[r[0] - 1:r[1]])) + "\n" for r in ranges]
sys.stdout.write(''.join(answer))
