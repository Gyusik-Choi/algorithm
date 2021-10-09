import sys


def get_sequence(idx):
    if idx == M:
        sys.stdout.write(' '.join(answer) + "\n")
    else:
        for i in range(N):
            if not answer:
                selected[i] = True
                answer.append(str(i + 1))
                get_sequence(idx + 1)
                selected[i] = False
                answer.pop()
            else:
                if not selected[i] and int(answer[-1]) < i + 1:
                    selected[i] = True
                    answer.append(str(i + 1))
                    get_sequence(idx + 1)
                    selected[i] = False
                    answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
selected = [False] * N
get_sequence(0)
