import sys


N, M = map(int, sys.stdin.readline().split())

s_map = dict()
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    s_map[s] = True

cnt = 0
for _ in range(M):
    m = sys.stdin.readline().rstrip()
    if m in s_map:
        cnt += 1

print(cnt)

# 참고
# https://yuna0125.tistory.com/75
