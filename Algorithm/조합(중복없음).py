import sys


def combinations(num, idx):
    if idx == M:
        sys.stdout.write(' '.join(answer) + "\n")
    else:
        for i in range(num, N):
            answer.append(str(i))
            combinations(i + 1, idx + 1)
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
combinations(0, 0)

# (중복없는) 조합
# 백준 15650 참고
