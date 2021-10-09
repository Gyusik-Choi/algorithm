import sys


def get_sequence(num, idx):
    if idx == M:
        sys.stdout.write(' '.join(answer) + "\n")
    else:
        for i in range(num, N + 1):
            answer.append(str(i))
            get_sequence(i + 1, idx + 1)
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
get_sequence(1, 0)

# 참고
# https://st-lab.tistory.com/115
