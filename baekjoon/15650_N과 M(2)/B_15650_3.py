import sys


def get_sequence(idx, depth):
    if depth == M:
        sys.stdout.write(' '.join(answer) + "\n")
    else:
        for i in range(idx, N + 1):
            answer.append(str(i))
            get_sequence(i + 1, depth + 1)
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
get_sequence(1, 0)

# 참고
# https://st-lab.tistory.com/115
